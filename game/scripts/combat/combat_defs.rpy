init python:
    status = {''}

    class Skill(object):
        def __init__(self,
        ):
            pass
    
    class Effect(object):
        def __init__(self):
            pass

    class Equipment(object):
        def __init__(self):
            pass

    class Mob(object):
        def __init__(self,
        name="default_mob",
        label="Default Mob",
        img="0.png",
        stats={'lvl': 0, 'hp': 0, 'mp': 0, 'atk': 0, 'def': 0, 'mag':0, 'mdef':0, 'acc': 0, 'spd': 0},
        effects=[],
        skills={},
        equipment={},
        is_dead=True,
        is_turn=False):
            self.name = name
            self.label = label
            self.img = img
            self.stats = stats
            self.stat_mods = stat_mods
            self.effects = effects
            self.skills = skills
            self.equipment = equipment
            self.is_dead = is_dead
            self.is_turn = is_turn
