init python:
    import copy
    import random
    import math

    class Skill(object):
        def __init__(self,
        name="default_skill",
        label="Default Skill",
        power=10,
        element=None,
        kinds=["damage"],
        targeting="enemy",
        effect=[],
        enabled=True,
        description="This is the default skill. It has no attributes and doesn't do anything",
        img="0.png",
        sound="",
        animation=""
        ):
            self.name = name
            self.label = label
            self.power = power
            self.element = element
            self.kinds = kinds
            self.targeting = targeting
            self.effect = effect
            self.enabled = enabled
            self.img = img
            self.description = description
            self.sound = sound
            self.animation = animation
    
    class Effect(object):
        def __init__(self,
        name,
        label,
        alignment,
        power,
        charges,
        img,
        description
        ):
            self.name = name
            self.label = label
            self.alignment = alignment
            self.power = power
            self.charges = charges
            self.img = img
            self.description = description

    class Equipment(object):
        def __init__(self):
            pass

    class Entity(object):
        def __init__(self,
        name="default_entity",
        label="Default Entity",
        description="",
        img="0.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
        effects=[],
        skills=[],
        equipment=[],
        side="enemy",
        examined=False,
        is_dead=False,
        is_turn=False,
        controllable=True):
            self.name = name
            self.label = label
            self.description = description
            self.img = img
            self.stats = stats
            self.resists = resists
            self.effects = effects
            self.skills = skills
            self.equipment = equipment
            self.side = side
            self.examined = examined
            self.is_dead = is_dead
            self.is_turn = is_turn
            self.controllable = controllable
            self.initialize_for_battle()

        def initialize_for_battle(self):
            self.is_dead = False
            self.is_turn = False
            self.effects = []
            self.current_hp = self.stats['hp']
            self.current_mp = self.stats['mp']
            self.stats_effective = copy.deepcopy(self.stats)
            return

    def create_enemy_group(enemy, count):
        global enemies
        eg = []
        for i in range(0, count):
            eg.append(copy.deepcopy(enemy))
        enemies = eg

    def create_party_group():
        global party_members, party_gavin, party_lance, party_morgan
        party_gavin.initialize_for_battle()
        party_lance.initialize_for_battle()
        party_morgan.initialize_for_battle()
        party_members = [party_gavin, party_lance, party_morgan]
        print(party_members)

    def set_combat_entities():
        global combat_entities, party_members, enemies
        combat_entities = [p for p in party_members if not p.is_dead] + [e for e in enemies if not e.is_dead]
        return

    def set_turn_order():
        global combat_entities, turn_order
        turn_order = sorted(combat_entities, key=lambda e: e.stats['spd'], reverse=True)
        return

    def set_active_entity():
        global turn, turn_order
        turn_position = turn % len(turn_order)
        for mob in turn_order:
            mob.is_turn = False
        turn_order[turn_position].is_turn = True
        return turn_order[turn_position]

    def push_message(m):
        global combat_log, message_bar_text
        combat_log.append(m)
        mb_text = ""
        for log_entry in combat_log[-15:]:
            mb_text = mb_text + log_entry + "\n"
        message_bar_text = mb_text
        renpy.pause(0.66)
        return

    def set_tooltip(f):
        global tooltip_title, tooltip_description, tooltip_detail
        if isinstance(f, Entity):
            tooltip_title = f.label
            tooltip_description = f.description
            detail_string = ""
            tooltip_detail = "Entity details TBI"
        elif isinstance(f, Skill):
            tooltip_title = f.label
            tooltip_description = f.description
            tooltip_detail = "Skill details TBI"
        elif isinstance(f, Effect):
            tooltip_title = f.label
            tooltip_description = f.description
            tooltip_detail = "Effect details TBI"
        else:
            tooltip_title = "Skip Combat"
            tooltip_description = "If combat is unwinnable, use this button to win and continue the game.\n\nIf combat crashes, click 'Rollback' on the crash menu and use this button.\n\nIf you're just eager to get on with the story... well, you get the picture."
        return

    def unset_tooltip():
        global tooltip_title, tooltip_description, tooltip_detail
        tooltip_title = ""
        tooltip_description = ""
        tooltip_detail = ""
        return

    def apply_skill(a, s, t):
        global shutdown_used
        # special case for entities under the effect of Lost Action (from Gaslight)
        if "lost_action" in [_.label for _ in a.effects]:
            push_message("{} tries to use {} but fails to act!".format(a.label, s.label))
            return
        else:
            push_message("{} uses {}!".format(a.label, s.label))

        ### EFFECT APPLICATION
        for eff in s.effect:
            # If the effect already exists on the target, strengthen it by +1 charge
            if eff.label in [_.label for _ in t.effects]:
                push_message("... but {} already had {} applied".format(t.label, eff.label))
                continue
            # Otherwise, add the effect to the targeted entity (no resisting effects)
            else:
                push_message("Applied {} to {}".format(eff.label, t.label))
                eff_copy = copy.deepcopy(eff)

                t.effects.append(copy.deepcopy(eff))

            # Stat and skill modifying effects apply immediately
            if eff.name == "attack_up":
                t.stats_effective['str'] += eff.power
                push_message("{}'s strength is now {}!".format(t.label, t.stats_effective['str']))
            elif eff.name == "accuracy_up":
                t.stats_effective['acc'] += eff.power
                push_message("{}'s accuracy is now {}!".format(t.label, t.stats_effective['acc']))
            elif eff.name == "defense_up":
                t.stats_effective['def'] += eff.power
                push_message("{}'s defense is now {}!".format(t.label, t.stats_effective['def']))
            elif eff.name == "attack_down":
                t.stats_effective['str'] += eff.power
                push_message("{}'s strength is now {}!".format(t.label, t.stats_effective['str']))
            elif eff.name == "accuracy_down":
                t.stats_effective['acc'] += eff.power
                push_message("{}'s accuracy is now {}!".format(t.label, t.stats_effective['acc']))
            elif eff.name == "defense_down":
                t.stats_effective['def'] += eff.power
                push_message("{}'s defense is now {}!".format(t.label, t.stats_effective['def']))
            elif eff.name == "lock_special":
                if t.name in ["gavin", "lance", "morgan"]:
                    t.skills[-1].enabled = False
                    push_message("{}'s {} skill is locked!".format(t.label, t.skills[-1].label))
            elif eff.name == "dispel":
                for active_effect in t.effects:
                    if active_effect.alignment == "bonus":
                        t.effects.remove(active_effect)
                push_message("Positive effects on {} are removed!".format(t.label))
            elif eff.name == "resurrect_weak":
                t.is_dead = False
            elif eff.name == "resurrect_strong":
                t.is_dead = False
                t.can_act = True


        ### DAMAGE CALCULATION
        if "damage" in s.kinds:
            ## Check current effects for damage cancellation
            damage_cancelled = False
            for eff in t.effects:
                if eff.name in ["negate_damage", "shield"]:
                    push_message("{} blocks the damage!".format(eff.label))
                    eff.charges -= 1
                    damage_cancelled = True
                elif eff.name == "negate_magic" and s.element == "magic":
                    push_message("{} blocks the magic damage!".format(eff.label))
                    eff.charges -= 1
                    damage_cancelled = True
                elif eff.name == "dodge" and s.element in ["blunt", "slash", "stab"]:
                    push_message("{} quickly dodges!".format(t.label))
                    eff.charges -= 1
                    damage_cancelled = True
                elif eff.name == "parry" and s.element in ["blunt", "slash", "stab"]:
                    a.current_hp -= 20
                    push_message("{} parries the attack and ripostes for {} damage".format(t.label, 20))

                
                if eff.charges == 0:
                    t.effects.remove(eff)
                
                if damage_cancelled:
                    break
            
            if not damage_cancelled:
                # Calculate resists
                resist = 0.0
                if s.element:
                    resist = t.resists[s.element]
                
                dmg = int(max(0, ((s.power + a.stats_effective['str']) - t.stats_effective['def']) * (1 - resist)))
                t.current_hp -= dmg
                push_message("{} deals {} damage to {}!".format(a.label, dmg, t.label))
        
        if "healing" in s.kinds:
            dmg = -(s.power + a.stats_effective['mag'])
            if s.name == "shut_down" and not shutdown_used:
                dmg = -t.stats['hp']
                shutdown_used = True # HACK
            t.current_hp = min(t.stats['hp'], t.current_hp - dmg)
            push_message("{} heals {} for {}!".format(a.label, t.label, -dmg))
        
        if t.current_hp <= 0:
            kill_entity(t)

        return

    def select_random_skill(a):
        return random.choice(a.skills)

    def select_random_target(a, s):
        global combat_entities
        target = None
        friendly_side = "enemy" if a.side == "enemy" else "party"
        hostile_side = "party" if a.side == "enemy" else "enemy"

        if s.targeting == "enemy" or s.targeting == "all_enemies":
            valid_targets = [e for e in combat_entities if e.side == hostile_side]
            target = random.choice(valid_targets)
        elif s.targeting == "ally" or s.targeting == "all_allies":
            valid_targets = [e for e in combat_entities if e.side == friendly_side]
            target = random.choice(valid_targets)
        elif s.targeting == "self":
            target = a

        # target is Gavin if taunt effect is active
        for active_effect in a.effects:
            if active_effect.name == "taunt":
                target = [e for e in combat_entities if e.name == "gavin"][0]
                a.effects.remove(active_effect)
        
        return target

    def update_active_effects(e):
        global turn
        for eff in e.effects:
            eff.charges -= 1
            if eff.name == "condemn" and eff.charges == 0:
                kill_entity(e)
            if eff.name == "extra_action":
                turn -= 1
                push_message("{} prepares to take another action!".format(e.label))
                
        return

    def kill_entity(e):
        global turn, turn_order, combat_entities
        e.is_dead = True
        turn_order.remove(e)
        combat_entities.remove(e)
        set_active_entity()
        push_message("{} falls!".format(e.label))
        return

    def level_up(e):
        e.stats['lvl'] += 1
        for k, v in e.stats.items():
            if k == "lvl":
                continue
            e.stats[k] = int(e.stats[k] * random.uniform(1.3, 1.5))
        push_message("{} reaches level {}!".format(e.label, e.stats['lvl']))

### Combat field position definitions
default enemy_spacing_patterns = {
    3: [(0, 0), (512, 0), (1024, 0)],
    2: [(256, 0), (768, 0)],
    1: [(512, 0)]}

default party_spacing_patterns = {
    3: [(32, 0), (512, 0), (852, 0)],
    2: [(256, 0), (768, 0)],
    1: [(512, 0)]}

### Effect definitions
default effect_attack_up = Effect("attack_up", "Attack Up", "bonus", 10, 999, "images/combat/icons/icon_effect_attack_up.png", "Increase attack by 10 points")
default effect_accuracy_up = Effect("accuracy_up", "Accuracy Up", "bonus", 10, 999, "images/combat/icons/icon_effect_accuracy_up.png", "Increase accuracy by 10 points")
default effect_defense_up = Effect("defense_up", "Defense Up", "bonus", 10, 999, "images/combat/icons/icon_effect_defense_up.png", "Increase defense by 10 points")
default effect_attack_down = Effect("attack_down", "Attack Down", "malus", 10, 999, "images/combat/icons/icon_effect_attack_down.png", "Decrease attack by 10 points")
default effect_magic_attack_down = Effect("magic_attack_down", "Magic Attack Down", "malus", 10, 999, "images/combat/icons/icon_effect_magic_attack_down.png", "Decrease magic attack by 10 points")
default effect_defense_down = Effect("defense_down", "Defense Down", "malus", 10, 999, "images/combat/icons/icon_effect_defense_down.png", "Decrease defense by 10 points")
default effect_accuracy_down = Effect("accuracy_down", "Accuracy Down", "malus", 10, 999, "images/combat/icons/icon_effect_accuracy_down.png", "Decrease accuracy by 10 points")

default effect_parry = Effect("parry", "Parry", "bonus", None, 1, "images/combat/icons/icon_effect_parry.png", "Negate the next instance of physical damage and riposte")
default effect_shield = Effect("shield", "Shield", "bonus", None, 1, "images/combat/icons/icon_effect_shield.png", "Negate the next instance of physical damage")
default effect_taunt = Effect("taunt", "Taunt", "malus", None, 1, "images/combat/icons/icon_effect_taunt.png", "Must target Gavin")
default effect_negate_magic = Effect("negate_magic", "Negate Magic", "bonus", None, 2, "images/combat/icons/icon_effect_negate_magic.png", "Negate the next instance of magic damage")
default effect_negate_damage = Effect("negate_damage", "Negate Damage", "bonus", None, 1, "images/combat/icons/icon_effect_negate_damage.png", "Negate the next instance of damage of any type")
default effect_dodge = Effect("dodge", "Dodge", "bonus", None, 1, "images/combat/icons/icon_effect_dodge.png", "Dodge the next attack")

default effect_extra_action = Effect("extra_action", "Extra Action", "bonus", None, 1, "images/combat/icons/icon_effect_extra_action.png", "Take an extra action after this one")
default effect_lost_action = Effect("lost_action", "Lost Action", "malus", None, 1, "images/combat/icons/icon_effect_lost_action.png", "Next action has no effect")
default effect_lock_special = Effect("lock_special", "Lock Special", "malus", None, 999, "images/combat/icons/icon_effect_lock_special.png", "SPECIAL skill is blocked")
default effect_condemned = Effect("condemned", "Condemned", "malus", None, 3, "images/combat/icons/icon_effect_condemned.png", "Die in [charges] turns")
default effect_dispel = Effect("dispel", "Dispel", "malus", None, 1, "images/combat/icons/icon_effect_dispel.png", "When resolved, remove all bonuses on target")

### Skill definitions

default skill_swing = Skill(name="swing", label="Swing", power=30, element="slash", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Swing your sword to make a foe bleed. Slashing damage.", img="images/combat/icons/icon_skill_swing.png", sound="dagger-scrape-and-hit-185443", animation="")
default skill_jab = Skill(name="jab", label="Jab", power=30, element="stab", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Pierce a foe with your sword and rearrange their innards. Stabbing damage.", img="images/combat/icons/icon_skill_jab.png", sound="metal-hit-22-193289", animation="")
default skill_parry = Skill(name="parry", label="Parry", power=0, element="stab", kinds=["status"], targeting="enemy", effect=[effect_parry], enabled=True, description="Prepare to block an attack with a chance to riposte, dealing Stabbing damage to the attacker.", img="images/combat/icons/icon_skill_parry.png", sound="sword_draw", animation="")
default skill_arcane_bolt = Skill(name="arcane_bolt", label="Arcane Bolt", power=30, element="magic", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Fire a concentrated bolt of magic. Magic damage.", img="images/combat/icons/icon_skill_arcane_bolt.png", sound="abstract-magic-whoosh-03-204485", animation="")
default skill_spirit_slice = Skill(name="spirit_slice", label="Spirit Slice", power=20, element="magic", kinds=["damage"], targeting="all_enemies", effect=[], enabled=True, description="Run a razor thin line across a foe. Magic damage.", img="images/combat/icons/icon_skill_spirit_slice.png", sound="dagger-scrape-and-hit-185443", animation="")
default skill_absorb_essence = Skill(name="absorb_essence", label="Absorb Essence", power=15, element="magic", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Steal energy from your foes. Magic damage.", img="images/combat/icons/icon_skill_absorb_essence.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_evaluate = Skill(name="evaluate", label="Evaluate", power=0, element="None", kinds=["status"], targeting="enemy", effect=[], enabled=True, description="[NO EFFECT] Observe a foe for a turn to learn its weakness", img="images/combat/icons/icon_skill_evaluate.png", sound="N/A", animation="")
default skill_swing_staff = Skill(name="swing_staff", label="Swing Staff", power=15, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Swing your staff. Blunt damage.", img="images/combat/icons/icon_skill_swing_staff.png", sound="power-punch-192118", animation="")
default skill_whack = Skill(name="whack", label="Whack", power=20, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Bring your staff down on the head of your foe for more damage than a SWING. Blunt damage.", img="images/combat/icons/icon_skill_whack.png", sound="metal-hit-22-193289", animation="")
default skill_drain = Skill(name="drain", label="Drain", power=10, element="magic", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Drain a foe of their health. Magic damage.", img="images/combat/icons/icon_skill_drain.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_healing_touch = Skill(name="healing_touch", label="Healing Touch", power=20, element="None", kinds=["healing"], targeting="ally", effect=[], enabled=True, description="Heal yourself or a partner.", img="images/combat/icons/icon_skill_healing_touch.png", sound="mystical-chime-196405", animation="")
default skill_restore_life = Skill(name="restore_life", label="Restore Life", power=10, element="None", kinds=["healing"], targeting="all_allies", effect=[], enabled=True, description="Heal a member of your party a little bit.", img="images/combat/icons/icon_skill_restore_life.png", sound="mystical-chime-196405", animation="")
default skill_revitalize = Skill(name="revitalize", label="Revitalize", power=0, element="None", kinds=["healing"], targeting="ally", effect=[], enabled=True, description="[NO EFFECT]", img="images/combat/icons/icon_skill_revitalize.png", sound="mystical-chime-196405", animation="")
default skill_assail = Skill(name="assail", label="Assail", power=30, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Swing your staff and unleash a torrent of dagger-sharp projectiles. {b}Shred their skin.{/b} Blunt damage.", img="images/icons/icon_placeholder.png", sound="metal-hit-22-193289", animation="")
default skill_crush = Skill(name="crush", label="Crush", power=15, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="{b}Break their ribs. Make them gurgle.{/b} Attack a target and cause them to skip their next turn. Blunt damage.", img="images/icons/icon_placeholder.png", sound="power-punch-192118", animation="")
default skill_shut_down = Skill(name="shut_down", label="Shut Down", power=0, element="None", kinds=["healing"], targeting="self", effect=[], enabled=True, description="Higher brain function stops for one turn, restoring all HP. {b}Voila! The pain is gone if you're not there to feel it.{/b}", img="images/icons/icon_placeholder.png", sound="cringe-scare-47561", animation="")
default skill_bite = Skill(name="bite", label="Bite", power=20, element="stab", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Attack with your teeth, seeking to eat the target alive. Stabbing damage.", img="images/icons/icon_placeholder.png", sound="power-punch-192118", animation="")
default skill_swipe = Skill(name="swipe", label="Swipe", power=10, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="With so many appendages, it's hard to know with which one it will strike. Multi-hit attack. Blunt damage.", img="images/icons/icon_placeholder.png", sound="power-punch-192118", animation="")
default skill_slam = Skill(name="slam", label="Slam", power=20, element="blunt", kinds=["damage"], targeting="all_enemies", effect=[], enabled=True, description="The strategy: infiltrate and scatter. The enemy slams down its full weight into the center of the group, damaging everyone. Blunt damage.", img="images/icons/icon_placeholder.png", sound="abstract-magic-whoosh-03-204485", animation="")
default skill_desolate = Skill(name="desolate", label="Desolate", power=20, element="magic", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="The Corrupted only know two things: 'Take,' and 'Mine.' The target takes damage, and you restore half of that. Magic damage.", img="images/combat/icons/icon_skill_desolate.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_slap = Skill(name="slap", label="Slap", power=10, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="... Ow? Blunt damage.", img="images/icons/icon_skill_slap.png", sound="power-punch-192118", animation="")
default skill_scratch = Skill(name="scratch", label="Scratch", power=15, element="slash", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="Okay, that hurts a little more. Slashing damage.", img="images/icons/icon_placeholder.png", sound="power-punch-192118", animation="")
default skill_headbutt = Skill(name="headbutt", label="Headbutt", power=20, element="blunt", kinds=["damage"], targeting="enemy", effect=[], enabled=True, description="These dummies are fighting diriy! Blunt damage.", img="images/icons/icon_placeholder.png", sound="power-punch-192118", animation="")
default skill_maim = Skill(name="maim", label="Maim", power=20, element="blunt", kinds=["damage"], targeting="enemy", effect=[effect_accuracy_down], enabled=True, description="{b}Go for the fingers and joints.{/b} Attack a target and decrease their accuracy. Blunt damage.", img="images/icons/icon_placeholder.png", sound="power-punch-192118", animation="")
default skill_shove = Skill(name="shove", label="Shove", power=10, element="None", kinds=["status"], targeting="enemy", effect=[effect_accuracy_down], enabled=True, description="You push an attacker away, decreasing their Accuracy.", img="images/combat/icons/icon_skill_shove.png", sound="power-punch-192118", animation="")
default skill_inner_focus = Skill(name="inner_focus", label="Inner Focus", power=10, element="None", kinds=["status"], targeting="self", effect=[effect_accuracy_up], enabled=True, description="You have come to terms with your potential, for others and for yourself. Take a turn to focus, increasing your accuracy for the remainder of the battle.", img="images/combat/icons/icon_skill_inner_focus.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_discourage = Skill(name="discourage", label="Discourage", power=10, element="None", kinds=["status"], targeting="enemy", effect=[effect_attack_down, effect_magic_attack_down], enabled=True, description="{b}There's no point trying to change things.{/b} Silence the target's determination, reducing their Attack and Magic Attack.", img="images/combat/icons/icon_skill_discourage.png", sound="N/A", animation="")
default skill_mockery = Skill(name="mockery", label="Mockery", power=10, element="None", kinds=["status"], targeting="enemy", effect=[effect_attack_up, effect_defense_down, effect_accuracy_down], enabled=True, description="The Corrupted doesn't understand why you're trying to change anything. It's laughing at you. Target's Attack increases, but their Defense and Accuracy decrease dramatically.", img="images/icons/icon_placeholder.png", sound="monster_roar", animation="")
default skill_rally = Skill(name="rally", label="Rally", power=10, element="None", kinds=["status"], targeting="all_allies", effect=[effect_attack_up], enabled=True, description="Encourage one of your partners, granting them +10 to Attack.", img="images/combat/icons/icon_skill_rally.png", sound="sword_draw", animation="")
default skill_judgement = Skill(name="judgement", label="Judgement", power=0, element="None", kinds=["status"], targeting="enemy", effect=[effect_condemned], enabled=True, description="{b}Make one target you deem inferior fall instantaneously in three turns with your power.{/b}", img="images/combat/icons/icon_skill_judgement.png", sound="N/A", animation="")
default skill_fortify_will = Skill(name="fortify_will", label="Fortify Will", power=10, element="None", kinds=["status"], targeting="all_allies", effect=[effect_defense_up], enabled=True, description="Increase all party members' Defense by 10 points.", img="images/combat/icons/icon_skill_fortify_will.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_form_flux = Skill(name="form_flux", label="Form Flux", power=20, element="None", kinds=["status"], targeting="self", effect=[effect_defense_up], enabled=True, description="Relax your form, sharply increasing your defense against damage.", img="images/combat/icons/icon_skill_form_flux.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_psychic_bombardment = Skill(name="psychic_bombardment", label="Psychic Bombardment", power=15, element="magic", kinds=["damage"], targeting="all_enemies", effect=[effect_dispel], enabled=True, description="{b}Overwhelm. Stress. Make them look stupid.{/b} Offensive magic that breaks the party's concentration, negating all positive status effects. Magic damage.", img="images/combat/icons/icon_skill_psychic_bombardment.png", sound="sword_draw", animation="")
default skill_evade = Skill(name="evade", label="Evade", power=0, element="None", kinds=["status"], targeting="self", effect=[effect_dodge], enabled=True, description="Dodge an incoming attack.", img="images/combat/icons/icon_skill_evade.png", sound="N/A", animation="")
default skill_awareness = Skill(name="awareness", label="Awareness", power=0, element="None", kinds=["healing"], targeting="all_allies", effect=[effect_extra_action], enabled=True, description="[NO EFFECT] You get what this is all for, even if it doesn't make it less painful. Bring all downed partners back to consciousness, fully restore HP for all party members, and grant them 1 extra turn.", img="images/combat/icons/icon_skill_awareness.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_annihilate = Skill(name="annihilate", label="Annihilate", power=15, element="None", kinds=["damage"], targeting="enemy", effect=[effect_lock_special], enabled=True, description="{b}Shatter them. Shatter everything they stand for. Make them KNEEL.{/b} Strip a hero of their newfound power, taking away their SPECIAL move.", img="images/icons/icon_placeholder.png", sound="laughter-01-105588", animation="")
default skill_gaslight = Skill(name="gaslight", label="Gaslight", power=0, element="None", kinds=["status"], targeting="self", effect=[effect_lost_action], enabled=True, description="[NO EFFECT] You attacked me? {b}No you didn't. You imagined it.{/b} Negate the effects of all enemies' next action", img="images/combat/icons/icon_skill_gaslight.png", sound="abstract-magic-whoosh-03-204485", animation="")
default skill_empathetic_relief = Skill(name="empathetic_relief", label="Empathetic Relief", power=0, element="None", kinds=["status"], targeting="all_allies", effect=[effect_negate_damage], enabled=True, description="You understand the importance of protecting your friends from harm. You're able to shield them from all from the next instance of damage of any type.", img="images/combat/icons/icon_skill_empathetic_relief.png", sound="atmospheric-metallic-swipe-11-195754", animation="")
default skill_repel_aura = Skill(name="repel_aura", label="Repel Aura", power=0, element="None", kinds=["status"], targeting="ally", effect=[effect_negate_magic], enabled=True, description="Negate the next 2 instances of magic damage against the selected party member.", img="images/combat/icons/icon_skill_repel_aura.png", sound="abstract-magic-whoosh-03-204485", animation="")
default skill_shield = Skill(name="shield", label="Shield", power=0, element="None", kinds=["status"], targeting="ally", effect=[effect_shield], enabled=True, description="Negate the next instance of physical damage against the selected party member.", img="images/combat/icons/icon_skill_shield.png", sound="metal-hit-22-193289", animation="")
default skill_antagonize = Skill(name="antagonize", label="Antagonize", power=0, element="None", kinds=["status"], targeting="enemy", effect=[effect_taunt], enabled=True, description="Demand the attention of a foe, forcing them to attack you next turn.", img="images/combat/icons/icon_skill_antagonize.png", sound="atmospheric-metallic-swipe-11-195754", animation="")

### Entity definitions

default party_gavin = Entity(
    name="gavin",
    label="Gavin",
    description="A boy with dark skin, curly dark-brown hair and a red cloak draped over one shoulder. There’s a sword at his hip, rusted along one side but otherwise in fairly decent condition.",
    img="images/sprites/gavin/gavin battle.png",
    stats={'lvl': 1, 'hp': 100, 'mp': 20, 'str': 15, 'def': 15, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
    effects=[],
    skills=[skill_swing, skill_jab, skill_parry, skill_shield, skill_antagonize, skill_rally, skill_inner_focus],
    equipment=[],
    side="party",
    examined=True,
    controllable=True)

default party_lance = Entity(
    name="lance",
    label="Lance",
    description="A boy with light skin, dark-blonde hair tied back in a bun, and a book strapped to his hip like a weapon.",
    img="images/sprites/lance/lance battle.png",
    stats={'lvl': 1, 'hp': 75, 'mp': 40, 'str': 10, 'def': 10, 'mag': 15, 'mdef': 15, 'acc': 10, 'spd': 10},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
    effects=[],
    skills=[skill_arcane_bolt, skill_spirit_slice, skill_fortify_will, skill_repel_aura, skill_absorb_essence, skill_evaluate, skill_empathetic_relief],
    equipment=[],
    side="party",
    examined=True,
    controllable=True)

default party_morgan = Entity(
    name="morgan",
    label="Morgan",
    description="A girl with pale skin, black hair, and sunken eyes. She looks somehow drained of life, husk-like, and leans heavily on a metal pole used as a staff.",
    img="images/sprites/morgan/morgan battle.png",
    stats={'lvl': 1, 'hp': 75, 'mp': 30, 'str': 10, 'def': 12, 'mag': 10, 'mdef': 15, 'acc': 10, 'spd': 15},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
    effects=[],
    skills=[skill_swing_staff, skill_whack, skill_drain, skill_evade, skill_healing_touch, skill_restore_life, skill_revitalize, skill_awareness],
    equipment=[],
    side="party",
    examined=True,
    controllable=True)

default enemy_training_dummy = Entity(
    name="training_dummy",
    label="Training Dummy",
    description="It’s just a bunch of trash made to look like an enemy. I guess you could say it’s... trashy.",
    img="images/combat/mobs/enemy_training_dummy.png",
    stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
    resists={'slash': -0.1, 'stab': 0.0, 'blunt': 0.1, 'magic': 0.0},
    effects=[],
    skills=[skill_slap, skill_evade],
    equipment=[],
    side="enemy",
    controllable=False)

default enemy_training_dummy_enhanced = Entity(
    name="training_dummy_enhanced",
    label="Training Dummy (Enhanced)",
    description="A bunch of trash that packs a magic wallop. Watch out for tetanus!",
    img="images/combat/mobs/enemy_training_dummy_enhanced.png",
    stats={'lvl': 2, 'hp': 150, 'mp': 20, 'str': 20, 'def': 20, 'mag': 20, 'mdef': 20, 'acc': 20, 'spd': 20},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
    effects=[],
    skills=[skill_scratch, skill_headbutt, skill_evade, skill_shove],
    equipment=[],
    side="enemy",
    controllable=False)

default enemy_corrupted_weak = Entity(
    name="corrupted_weak",
    label="Corrupted (formless)",
    description=" A corrupted sludge of bio-material. It’s pretty weak; clearly it hasn’t fed in a while. Sucks to be it.",
    img="images/combat/mobs/enemy_corrupted_weak.png",
    stats={'lvl': 3, 'hp': 250, 'mp': 50, 'str': 30, 'def': 30, 'mag': 30, 'mdef': 30, 'acc': 30, 'spd': 30},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
    effects=[],
    skills=[skill_scratch, skill_headbutt, skill_evade, skill_shove],
    equipment=[],
    side="enemy",
    controllable=False)

default enemy_corrupted = Entity(
    name="corrupted",
    label="Corrupted (forming)",
    description="A corrupted sludge of medium-sized  bio-material. It has more hands than it needs to grab at as much as it can. Watch your step.",
    img="images/combat/mobs/enemy_corrupted.png",
    stats={'lvl': 4, 'hp': 350, 'mp': 75, 'str': 40, 'def': 40, 'mag': 40, 'mdef': 40, 'acc': 40, 'spd': 40},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
    effects=[],
    skills=[skill_bite, skill_swipe, skill_evade, skill_form_flux],
    equipment=[],
    side="enemy",
    controllable=False)

default enemy_corrupted_strong = Entity(
    name="corrupted_strong",
    label="Corrupted (formed)",
    description="A corrupted mass of bio-material. This thing has fed well, but it will never be sated. No running from it now.",
    img="images/combat/mobs/enemy_corrupted_strong.png",
    stats={'lvl': 6, 'hp': 600, 'mp': 125, 'str': 60, 'def': 60, 'mag': 60, 'mdef': 60, 'acc': 60, 'spd': 60},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
    effects=[],
    skills=[skill_bite, skill_swipe, skill_slam, skill_evade, skill_form_flux, skill_desolate, skill_mockery],
    equipment=[],
    side="enemy",
    controllable=False)

default enemy_hermit = Entity(
    name="hermit",
    label="The Hermit",
    description="It’s you! Not much else on the surface; need I say more?",
    img="images/combat/mobs/enemy_hermit.png",
    stats={'lvl': 9, 'hp': 999, 'mp': 999, 'str': 75, 'def': 35, 'mag': 75, 'mdef': 35, 'acc': 75, 'spd': 5},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
    effects=[],
    skills=[skill_swing_staff, skill_whack, skill_fortify_will, skill_repel_aura, skill_judgement],
    equipment=[],
    side="enemy",
    controllable=False) 

default enemy_hidden_darkness = Entity(
    name="hidden_darkness",
    label="The Hidden Darkness",
    description="The ultimate reason for the extinction of humanity. Greed, ignorance, cowardice, apathy -- it’s all here, manifested in physical form. It wants us to feel like we’re looking in a mirror; don’t let it get to you.",
    img="images/combat/mobs/enemy_hidden_darkness.png",
    stats={'lvl': 10, 'hp': 999, 'mp': 999, 'str': 100, 'def': 50, 'mag': 100, 'mdef': 50, 'acc': 100, 'spd': 50},
    resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
    effects=[],
    skills=[skill_assail, skill_maim, skill_crush, skill_shut_down, skill_gaslight, skill_discourage, skill_judgement, skill_psychic_bombardment, skill_annihilate],
    equipment=[],
    side="enemy",
    controllable=False)
