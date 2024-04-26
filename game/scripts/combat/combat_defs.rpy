init python:
    turn = 0
    turn_order = []

    class Skill(object):
        def __init__(self,
        name="default_skill",
        label="Default Skill",
        img="0.png",
        power=10,
        dmg_type=None,
        num_targets=1,
        description="This is the default skill. It has no attributes and doesn't do anything"
        ):
            self.name = name
            self.label = label
            self.img = img
            self.power = power
            self.dmg_type = dmg_type
            self.num_targets = num_targets
            self.description = description
    
    class Effect(object):
        def __init__(self):
            pass

    class Equipment(object):
        def __init__(self):
            pass

    class Entity(object):
        def __init__(self,
        name="default_entity",
        label="Default Entity",
        img="0.png",
        stats={'lvl': 1, 'hp': 50, 'mp': 10, 'str': 10, 'def': 10, 'mag': 10, 'mdef': 10, 'acc': 10, 'spd': 10},
        effects=[],
        skills=[],
        equipment={},
        position=0,
        is_dead=False,
        is_turn=False,
        controllable=True):
            self.name = name
            self.label = label
            self.img = img
            self.stats = stats
            self.effects = effects
            self.skills = skills
            self.equipment = equipment
            self.is_dead = is_dead
            self.is_turn = is_turn
            self.controllable = controllable

            self.current_hp = self.stats['hp']
            self.current_mp = self.stats['mp']

    def set_turn_order():
        global entities, turn_order
        entities = [p for p in party_members if not p.is_dead] + [e for e in enemies if not e.is_dead]
        turn_order = entities
        return

    def set_active_entity():
        turn_position = turn % len(turn_order)
        for mob in turn_order:
            mob.is_turn = False
        turn_order[turn_position].is_turn = True
        return turn_order[turn_position]

    def apply_damage(a, s, t):
        dmg = (s.power + a.stats['str']) - t.stats['def']
        print(t.label, s.label, s.power, a.stats['str'], t.stats['def'], dmg)
        t.current_hp -= dmg
        if t.current_hp <= 0:
            kill_entity(t)
        return

    def kill_entity(e):
        e.is_dead = True
        turn_order.remove(e)
        set_active_entity()
        return

default enemy_spacing_patterns = {
    5: [(0, 0), (256, 0), (512, 0), (768, 0), (1024, 0)],
    4: [(128, 0), (384, 0), (640, 0), (896, 0)],
    3: [(256, 0), (512, 0), (768, 0)],
    2: [(384, 0), (640, 0)],
    1: [(512, 0)]
    }

default party_spacing_patterns = {
    3: [(0, 0), (384, 0), (768, 0)],
    2: [(192, 0), (576, 0)],
    1: [(384, 0)]
}

default no_skill = Skill("none", "None", "images/icons/icon_sword.png")
default arcane_bolt = Skill("arcane_bolt", "Arcane Bolt", "images/icons/icon_arcane_bolt.png")
default strike = Skill("strike", "Strike", "images/icons/icon_staff.png")
default slash = Skill("slash", "Slash", "images/icons/icon_sword.png")

default training_dummy_skills = [strike, slash]

default training_dummy_1 = Entity("training_dummy_1", "Training Dummy 1", "images/mobs/training_dummy.png", skills=training_dummy_skills)
default training_dummy_2 = Entity("training_dummy_2", "Training Dummy 2", "images/mobs/training_dummy.png", skills=training_dummy_skills)
default training_dummy_3 = Entity("training_dummy_3", "Training Dummy 3", "images/mobs/training_dummy.png", skills=training_dummy_skills)
default training_dummy_4 = Entity("training_dummy_4", "Training Dummy 4", "images/mobs/training_dummy.png", skills=training_dummy_skills, is_dead=True)
default training_dummy_5 = Entity("training_dummy_5", "Training Dummy 5", "images/mobs/training_dummy.png", skills=training_dummy_skills)

default enemies = [training_dummy_1, training_dummy_2, training_dummy_3, training_dummy_4, training_dummy_5]

default gavin_skills = [slash]
default lance_skills = [strike, slash, arcane_bolt]
default morgan_skills = [strike]

default party_gavin = Entity("gavin", "Gavin", "images/sprites/gavin/gavin battle.png", skills=gavin_skills)
default party_lance = Entity("lance", "Lance", "images/sprites/lance/lance battle.png", skills=lance_skills)
default party_morgan = Entity("morgan", "Morgan", "images/sprites/morgan/morgan battle.png", skills=morgan_skills)

default party_members = [party_gavin, party_lance, party_morgan]
