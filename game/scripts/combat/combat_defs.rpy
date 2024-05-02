

init python:
    import copy
    import random

    class Skill(object):
        def __init__(self,
        name="default_skill",
        label="Default Skill",
        power=10,
        element=None,
        targeting="enemy",
        effect=False,
        img="0.png",
        description="This is the default skill. It has no attributes and doesn't do anything"
        ):
            self.name = name
            self.label = label
            self.power = power
            self.element = element
            self.targeting = targeting
            self.effect = effect
            self.img = img
            self.description = description
    
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
        desc="",
        img="0.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
        effects=[],
        skills=[],
        equipment=[],
        examined=False,
        is_dead=False,
        is_turn=False,
        controllable=True):
            self.name = name
            self.label = label
            self.desc = desc
            self.img = img
            self.stats = stats
            self.resists = resists
            self.effects = effects
            self.skills = skills
            self.equipment = equipment
            self.examined = examined
            self.is_dead = is_dead
            self.is_turn = is_turn
            self.controllable = controllable
            self.initialize_for_battle()

        def initialize_for_battle(self):
            self.is_dead = False
            self.is_turn = False
            self.current_hp = self.stats['hp']
            self.current_mp = self.stats['mp']
            self.stats_effective = copy.deepcopy(self.stats)
            return

    def populate_groups(cg):
        global enemies, party_members, combat_entities
        enemies = cg
        party_members = [party_gavin, party_lance, party_morgan]
        combat_entities = enemies + party_members

    def set_turn_order():
        global combat_entities, turn_order
        combat_entities = [p for p in party_members if not p.is_dead] + [e for e in enemies if not e.is_dead]
        turn_order = sorted(combat_entities, key=lambda e: e.stats['spd'], reverse=True)
        return

    def set_active_entity():
        turn_position = turn % len(turn_order)
        for mob in turn_order:
            mob.is_turn = False
        turn_order[turn_position].is_turn = True
        return turn_order[turn_position]

    def has_effect(effect_name, t):
        if effect_name in [eff.name for eff in t.effects]:
            return True
        return False

    def apply_skill(a, s, t):
        msg = "{} uses {}".format(a.label, s.label)

        resist = 0.0
        if s.element:
            resist = t.resists[s.element]
        
        # For each effect caused by the skill:
        #       (A) increase the charges if the effect already exists on the target
        # or,   (B) apply the effect (stat changes are effective immediately)
        for eff in s.effect:
            if eff in t.effects:
                t.effects.index(eff).charges += eff.charges 
                msg = msg + "\nStrengthened {} on {}".format(eff.label, t.label)
                continue
            
            msg = msg + "\nApplied {} to {}".format(eff.label, t.label)
            t.effects.append(copy.deepcopy(eff))

            if eff.name == "attack_up":
                t.stats_effective['atk'] *= 1 + eff.power
            elif eff.name == "accuracy_up":
                t.stats_effective['acc'] *= 1 + eff.power
            elif eff.name == "defense_up":
                t.stats_effective['def'] *= 1 + eff.power
            elif eff.name == "attack_down":
                t.stats_effective['atk'] *= 1 - eff.power
            elif eff.name == "accuracy_down":
                t.stats_effective['acc'] *= 1 - eff.power
            elif eff.name == "defense_down":
                t.stats_effective['def'] *= 1 - eff.power
            
        print("resist {}".format(resist))
        dmg = ((s.power + a.stats['str']) - t.stats['def']) * (1 - resist)
        t.current_hp -= dmg

        if dmg < 0:
            msg = "{} uses {}! Dealt {} healing!".format(a.label, s.label, dmg)
        elif dmg > 0:
            msg = "{} uses {}! Dealt {} damage!".format(a.label, s.label, dmg)
        else:
            msg = "{} uses {}!".format(a.label, s.label)


        if t.current_hp <= 0:
            kill_entity(t)
            msg = msg + " {} dies!".format(t.label)
        
        for e in s.effect:
            t.effects.append(copy.deepcopy(e))
            msg = msg + " {} is affected by {}!".format(t.label, e.label)

        return msg

    def apply_effect(e, t):
        t.effects.append(copy.deepcopy(e))
        return

    def calculate_effective_stats(e):
        return

    def update_effects(e):
        return

    def kill_entity(e):
        e.is_dead = True
        turn_order.remove(e)
        set_active_entity()
        return

    def level_up(e):
        for k, v in e.stats.items():
            e.stats[k] = int(e.stats[k] * random.randrange(1.3, 1.5))

    ### Combat field position definitions
    enemy_spacing_patterns = {
        5: [(0, 0), (256, 0), (512, 0), (768, 0), (1024, 0)],
        4: [(128, 0), (384, 0), (640, 0), (896, 0)],
        3: [(256, 0), (512, 0), (768, 0)],
        2: [(384, 0), (640, 0)],
        1: [(512, 0)]
        }

    party_spacing_patterns = {
        3: [(0, 0), (384, 0), (768, 0)],
        2: [(192, 0), (576, 0)],
        1: [(384, 0)]
    }

    ### Effect definitions

    effect_attack_up = Effect("attack_up", "Attack Up", "bonus", 10, 999, "images/combat/icons/icon_effect_attack_up.png", "Increase attack by [power] points")
    effect_accuracy_up = Effect("accuracy_up", "Accuracy Up", "bonus", 10, 999, "images/combat/icons/icon_effect_accuracy_up.png", "Increase accuracy by [power] points")
    effect_defense_up = Effect("defense_up", "Defense Up", "bonus", 10, 999, "images/combat/icons/icon_effect_defense_up.png", "Increase defense by [power] points")
    effect_attack_down = Effect("attack_down", "Attack Down", "malus", 10, 999, "images/combat/icons/icon_effect_attack_down.png", "Decrease attack by [power] points")
    effect_magic_attack_down = Effect("magic_attack_down", "Magic Attack Down", "malus", 10, 999, "images/combat/icons/icon_effect_magic_attack_down.png", "Decrease magic attack by [power] points")
    effect_defense_down = Effect("defense_down", "Defense Down", "malus", 10, 999, "images/combat/icons/icon_effect_defense_down.png", "Decrease defense by [power] points")
    effect_accuracy_down = Effect("accuracy_down", "Accuracy Down", "malus", 10, 999, "images/combat/icons/icon_effect_accuracy_down.png", "Decrease accuracy by [power] points")

    effect_parry = Effect("parry", "Parry", "bonus", None, 1, "images/combat/icons/icon_effect_parry.png", "Negate the next instance of physical damage and riposte")
    effect_shield = Effect("shield", "Shield", "bonus", None, 1, "images/combat/icons/icon_effect_shield.png", "Negate the next instance of physical damage")
    effect_taunt = Effect("taunt", "Taunt", "malus", None, 1, "images/combat/icons/icon_effect_taunt.png", "Must target Gavin")
    effect_negate_magic = Effect("negate_magic", "Negate Magic", "bonus", None, 2, "images/combat/icons/icon_effect_negate_magic.png", "Negate the next instance of magic damage")
    effect_negate_damage = Effect("negate_damage", "Negate Damage", "bonus", None, 1, "images/combat/icons/icon_effect_negate_damage.png", "Negate the next instance of damage of any type")
    effect_dodge = Effect("dodge", "Dodge", "bonus", None, 1, "images/combat/icons/icon_effect_dodge.png", "Dodge the next attack")
    
    effect_extra_action = Effect("extra_action", "Extra Action", "bonus", None, 1, "images/combat/icons/icon_effect_extra_action.png", "Take an extra action after this one")
    effect_lost_action = Effect("lost_action", "Lost Action", "malus", None, 1, "images/combat/icons/icon_effect_lost_action.png", "Next action has no effect")
    effect_lock_special = Effect("lock_special", "Lock Special", "malus", None, 999, "images/combat/icons/icon_effect_lock_special.png", "SPECIAL skill is blocked")
    effect_condemned = Effect("condemned", "Condemned", "malus", None, 3, "images/combat/icons/icon_effect_condemned.png", "Die in [charges] turns")
    effect_dispel = Effect("dispel", "Dispel", "malus", None, 1, "images/combat/icons/icon_effect_dispel.png", "When resolved, remove all bonuses on target")

    ### Skill definitions

    skill_swing = Skill("swing", "Swing", 30, "slash", "enemy", [], "images/icons/icon_placeholder.png", "Swing your sword to make a foe bleed. Slashing damage.")
    skill_jab = Skill("jab", "Jab", 30, "stab", "enemy", [], "images/icons/icon_placeholder.png", "Pierce a foe with your sword and rearrange their innards. Stabbing damage.")
    skill_parry = Skill("parry", "Parry", 0, "stab", "enemy", [], "images/icons/icon_placeholder.png", "Prepare to block an attack with a chance to riposte, dealing Stabbing damage to the attacker.")
    skill_shield = Skill("shield", "Shield", 0, None, "ally", [effect_shield], "images/icons/icon_placeholder.png", "Negate the next instance of physical damage against the selected party member.")
    skill_rally = Skill("rally", "Rally", 10, None, "all_allies", [effect_attack_up], "images/icons/icon_placeholder.png", "Encourage your partners, granting them +10 to Attack.")
    skill_antagonize = Skill("antagonize", "Antagonize", 0, None, "enemy", [effect_taunt], "images/icons/icon_placeholder.png", "Demand the attention of a foe, forcing them to attack you next turn.")
    skill_inner_focus = Skill("inner_focus", "Inner Focus", 0.5, None, "self", [effect_accuracy_up], "images/icons/icon_placeholder.png", "You have come to terms with your potential, for others and for yourself. Take a turn to focus, increasing your accuracy for the remainder of the battle.")
    skill_arcane_bolt = Skill("arcane_bolt", "Arcane Bolt", 30, "magic", "enemy", [], "images/icons/icon_placeholder.png", "Fire a concentrated bolt of magic. Magic damage.")
    skill_spirit_slice = Skill("spirit_slice", "Spirit Slice", 20, "magic", "all_enemies", [], "images/icons/icon_placeholder.png", "Run a razor thin line across all foes. Magic damage.")
    skill_fortify_will = Skill("fortify_will", "Fortify Will", 10, None, "all_allies", [effect_defense_up], "images/icons/icon_placeholder.png", "Increase all party members' Defense by 10 points.")
    skill_repel_aura = Skill("repel_aura", "Repel Aura", 0, None, "ally", [effect_negate_magic], "images/icons/icon_placeholder.png", "Negate the next 2 instances of magic damage against the selected party member.")
    skill_absorb_essence = Skill("absorb_essence", "Absorb Essence", 15, "magic", "enemy", [], "images/icons/icon_placeholder.png", "Steal energy from your foes, restoring some of your and your allies' HP. Magic damage.")
    skill_evaluate = Skill("evaluate", "Evaluate", 0, None, "enemy", [], "images/icons/icon_placeholder.png", "Observe a foe for a turn to learn its weakness.")
    skill_empathetic_relief = Skill("empathetic_relief", "Empathetic Relief", 0, None, "all_allies", [effect_negate_damage], "images/icons/icon_placeholder.png", "You understand the importance of protecting your friends from harm. You're able to shield them from all from the next instance of damage of any type.")
    skill_swing_staff = Skill("swing_staff", "Swing Staff", 15, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "Swing your staff, possibly damaging enemies to either side. Blunt damage.")
    skill_whack = Skill("whack", "Whack", 20, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "Bring your staff down on the head of your foe for more damage than a SWING. Blunt damage.")
    skill_drain = Skill("drain", "Drain", 10, "magic", "enemy", [], "images/icons/icon_placeholder.png", "Drain a foe of their health, using it to restore your own HP. Magic damage.")
    skill_evade = Skill("evade", "Evade", 0, None, "self", [effect_dodge], "images/icons/icon_placeholder.png", "Dodge an incoming attack.")
    skill_healing_touch = Skill("healing_touch", "Healing Touch", 20, None, "ally", [], "images/icons/icon_placeholder.png", "Heal yourself or a partner.")
    skill_restore_life = Skill("restore_life", "Restore Life", 10, None, "all_allies", [], "images/icons/icon_placeholder.png", "Heal every conscious member of your party a little bit.")
    skill_revitalize = Skill("revitalize", "Revitalize", 0, None, "ally", [], "images/icons/icon_placeholder.png", "Bring a downed partner back to consciousness with 25% of their max HP.")
    skill_awareness = Skill("awareness", "Awareness", 0, None, "all_allies", [effect_extra_action], "images/icons/icon_placeholder.png", "You get what this is all for, even if it doesn't make it less painful. Bring all downed partners back to consciousness, fully restore HP for all party members, and grant them 1 extra turn.")
    skill_assail = Skill("assail", "Assail", 30, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "Swing your staff and unleash a torrent of dagger-sharp projectiles. {b}Shred their skin.{/b} Blunt damage.")
    skill_maim = Skill("maim", "Maim", 20, "blunt", "enemy", [effect_accuracy_down], "images/icons/icon_placeholder.png", "{b}Go for the fingers and joints.{/b} Attack a target and decrease their accuracy. Blunt damage.")
    skill_crush = Skill("crush", "Crush", 15, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "{b}Break their ribs. Make them gurgle.{/b} Attack a target and cause them to skip their next turn. Blunt damage.")
    skill_shut_down = Skill("shut_down", "Shut Down", 0, None, "self", [], "images/icons/icon_placeholder.png", "Higher brain function stops for one turn, restoring all HP. {b}Voila! The pain is gone if you're not there to feel it.{/b}")
    skill_gaslight = Skill("gaslight", "Gaslight", 0, None, "self", [effect_lost_action], "images/icons/icon_placeholder.png", "You attacked me? {b}No you didn't. You imagined it.{/b} Negate the effects of all enemies' next action")
    skill_discourage = Skill("discourage", "Discourage", 0.5, None, "enemy", [effect_attack_down, effect_magic_attack_down], "images/icons/icon_placeholder.png", "{b}There's no point trying to change things.{/b} Silence the target's determination, reducing their Attack and Magic Attack.")
    skill_judgement = Skill("judgement", "Judgement", 0, None, "enemy", [effect_condemned], "images/icons/icon_placeholder.png", "{b}Make one target you deem inferior fall instantaneously in three turns with your power.{/b}")
    skill_psychic_bombardment = Skill("psychic_bombardment", "Psychic Bombardment", 15, "magic", "all_enemies", [effect_dispel], "images/icons/icon_placeholder.png", "{b}Overwhelm. Stress. Make them look stupid.{/b} Offensive magic that breaks the party's concentration, negating all positive status effects. Magic damage.")
    skill_annihilate = Skill("annihilate", "Annihilate", 15, None, "enemy", [effect_lock_special], "images/icons/icon_placeholder.png", "{b}Shatter them. Shatter everything they stand for. Make them KNEEL.{/b} Strip a hero of their newfound power, taking away their SPECIAL move.")
    skill_bite = Skill("bite", "Bite", 20, "stab", "enemy", [], "images/icons/icon_placeholder.png", "Attack with your teeth, seeking to eat the target alive. Stabbing damage.")
    skill_swipe = Skill("swipe", "Swipe", 10, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "With so many appendages, it's hard to know with which one it will strike. Multi-hit attack. Blunt damage.")
    skill_form_flux = Skill("form_flux", "Form Flux", 0.5, None, "self", [effect_defense_up], "images/icons/icon_placeholder.png", "Relax your form, sharply increasing your defense against damage.")
    skill_slam = Skill("slam", "Slam", 20, "blunt", "all_enemies", [], "images/icons/icon_placeholder.png", "The strategy: infiltrate and scatter. The enemy slams down its full weight into the center of the group, damaging everyone. Blunt damage.")
    skill_desolate = Skill("desolate", "Desolate", 20, "magic", "enemy", [], "images/icons/icon_placeholder.png", "The Corrupted only know two things: 'Take,' and 'Mine.' The target takes damage, and you restores half of that. Magic damage.")
    skill_mockery = Skill("mockery", "Mockery", 0.5, None, "enemy", [effect_attack_up, effect_defense_down, effect_accuracy_down], "images/icons/icon_placeholder.png", "The Corrupted doesn't understand why you're trying to change anything. It's laughing at you. Target's Attack increases, but their Defense and Accuracy decrease dramatically.")
    skill_slap = Skill("slap", "Slap", 10, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "... Ow? Blunt damage.")
    skill_scratch = Skill("scratch", "Scratch", 15, "slash", "enemy", [], "images/icons/icon_placeholder.png", "Okay, that hurts a little more. Slashing damage.")
    skill_headbutt = Skill("headbutt", "Headbutt", 20, "blunt", "enemy", [], "images/icons/icon_placeholder.png", "These dummies are fighting diriy! Blunt damage.")
    skill_shove = Skill("shove", "Shove", 10, None, "enemy", [effect_accuracy_down], "images/icons/icon_placeholder.png", "You push an attacker away, decreasing their Accuracy.")
    ### Entity definitions

    party_gavin = Entity(
        name="gavin",
        label="Gavin",
        desc="A boy with dark skin, curly dark-brown hair and a red cloak draped over one shoulder. There’s a sword at his hip, rusted along one side but otherwise in fairly decent condition.",
        img="images/sprites/gavin/gavin battle.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
        skills=[skill_swing, skill_jab, skill_parry, skill_shield, skill_rally, skill_antagonize, skill_inner_focus],
        equipment=[],
        controllable=True)

    party_lance = Entity(
        name="lance",
        label="Lance",
        desc="A boy with light skin, dark-blonde hair tied back in a bun, and a book strapped to his hip like a weapon.",
        img="images/sprites/lance/lance battle.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
        skills=[skill_arcane_bolt, skill_spirit_slice, skill_fortify_will, skill_repel_aura, skill_absorb_essence, skill_evaluate, skill_empathetic_relief],
        equipment=[],
        controllable=True)

    party_morgan = Entity(
        name="morgan",
        label="Morgan",
        desc="A girl with pale skin, black hair, and sunken eyes. She looks somehow drained of life, husk-like, and leans heavily on a metal pole used as a staff.",
        img="images/sprites/morgan/morgan battle.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.0, 'magic': 0.0},
        skills=[skill_swing, skill_whack, skill_drain, skill_evade, skill_healing_touch, skill_restore_life, skill_revitalize, skill_awareness],
        equipment=[],
        controllable=True)

    enemy_training_dummy = Entity(
        name="training_dummy",
        label="Training Dummy",
        desc="It’s just a bunch of trash made to look like an enemy. I guess you could say it’s... trashy.",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        resists={'slash': -0.1, 'stab': 0.0, 'blunt': 0.1, 'magic': 0.0},
        skills=[skill_slap, skill_evade],
        equipment=[],
        controllable=True)

    enemy_training_dummy_enhanced = Entity(
        name="training_dummy_enhanced",
        label="Training Dummy (Enhanced)",
        desc="A bunch of trash that packs a magic wallop. Watch out for tetanus!",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 2, 'hp': 150, 'mp': 20, 'str': 20, 'def': 20, 'mag': 20, 'mdef': 20, 'acc': 20, 'spd': 20},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
        skills=[skill_scratch, skill_headbutt, skill_evade, skill_shove],
        equipment=[],
        controllable=True)

    enemy_corrupted_weak = Entity(
        name="corrupted_weak",
        label="Corrupted (formless)",
        desc=" A corrupted sludge of bio-material. It’s pretty weak; clearly it hasn’t fed in a while. Sucks to be it.",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 3, 'hp': 250, 'mp': 50, 'str': 30, 'def': 30, 'mag': 30, 'mdef': 30, 'acc': 30, 'spd': 30},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
        skills=[skill_scratch, skill_headbutt, skill_evade, skill_shove],
        equipment=[],
        controllable=True)

    enemy_corrupted = Entity(
        name="corrupted",
        label="Corrupted (forming)",
        desc="A corrupted sludge of medium-sized  bio-material. It has more hands than it needs to grab at as much as it can. Watch your step.",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 4, 'hp': 350, 'mp': 75, 'str': 40, 'def': 40, 'mag': 40, 'mdef': 40, 'acc': 40, 'spd': 40},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
        skills=[skill_bite, skill_swipe, skill_evade, skill_form_flux],
        equipment=[],
        controllable=True)

    enemy_corrupted_strong = Entity(
        name="corrupted_strong",
        label="Corrupted (formed)",
        desc="A corrupted mass of bio-material. This thing has fed well, but it will never be sated. No running from it now.",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 6, 'hp': 600, 'mp': 125, 'str': 60, 'def': 60, 'mag': 60, 'mdef': 60, 'acc': 60, 'spd': 60},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
        skills=[skill_bite, skill_swipe, skill_slam, skill_evade, skill_form_flux, skill_desolate, skill_mockery],
        equipment=[],
        controllable=True)

    enemy_hermit = Entity(
        name="hermit",
        label="The Hermit",
        desc="It’s you! Not much else on the surface; need I say more?",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 9, 'hp': 999, 'mp': 999, 'str': 75, 'def': 35, 'mag': 75, 'mdef': 35, 'acc': 75, 'spd': 35},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
        skills=[skill_bite, skill_swipe, skill_slam, skill_evade, skill_form_flux, skill_desolate, skill_mockery],
        equipment=[],
        controllable=True) 

    enemy_hidden_darkness = Entity(
        name="hidden_darkness",
        label="The Hidden Darkness",
        desc="The ultimate reason for the extinction of humanity. Greed, ignorance, cowardice, apathy -- it’s all here, manifested in physical form. It wants us to feel like we’re looking in a mirror; don’t let it get to you.",
        img="images/combat/mobs/training_dummy.png",
        stats={'lvl': 10, 'hp': 999, 'mp': 999, 'str': 100, 'def': 50, 'mag': 100, 'mdef': 50, 'acc': 100, 'spd': 50},
        resists={'slash': 0.0, 'stab': 0.0, 'blunt': 0.15, 'magic': 0.15},
        skills=[skill_assail, skill_maim, skill_crush, skill_shut_down, skill_gaslight, skill_discourage, skill_judgement, skill_psychic_bombardment, skill_annihilate],
        equipment=[],
        controllable=True)

    ### Enemy group definitions

    enemy_group_hermit = [
        copy.deepcopy(enemy_hermit)]

    enemy_group_training_dummies = [
        copy.deepcopy(enemy_training_dummy),
        copy.deepcopy(enemy_training_dummy),
        copy.deepcopy(enemy_training_dummy),
        copy.deepcopy(enemy_training_dummy)]

    enemy_group_training_dummies_enhanced = [
        copy.deepcopy(enemy_training_dummy_enhanced),
        copy.deepcopy(enemy_training_dummy_enhanced),
        copy.deepcopy(enemy_training_dummy_enhanced),
        copy.deepcopy(enemy_training_dummy_enhanced)]

    enemy_group_corrupted_weak = [
        copy.deepcopy(enemy_corrupted_weak),
        copy.deepcopy(enemy_corrupted_weak),
        copy.deepcopy(enemy_corrupted_weak)]

    enemy_group_corrupted = [
        copy.deepcopy(enemy_corrupted),
        copy.deepcopy(enemy_corrupted),
        copy.deepcopy(enemy_corrupted)]

    enemy_group_corrupted_strong = [
        copy.deepcopy(enemy_corrupted_strong),
        copy.deepcopy(enemy_corrupted_strong),
        copy.deepcopy(enemy_corrupted_strong)]

    enemy_group_hidden_darkness = [
        copy.deepcopy(enemy_hidden_darkness)]

    ### Group definitions

    enemies = []
    party_members = []
    combat_entities = []
    turn_order = []
    import copy
    turn = 0
    turn_order = []
