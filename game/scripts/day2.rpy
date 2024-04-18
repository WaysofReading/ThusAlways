define day2_morning_hero1_seen = False
define day2_morning_hero2_seen = False
define day2_morning_hero3_seen = False

define day2_morning_hero1_points = 0
define day2_morning_hero2_points = 0
define day2_morning_hero3_points = 0

label day2_morning:

    label day2_morning_hero_choice:
        menu:
            'hero 1':
                call day2_morning_hero1 from _call_day2_morning_hero1
            'hero 2':
                call day2_morning_hero2 from _call_day2_morning_hero2
            'hero 3':
                call day2_morning_hero3 from _call_day2_morning_hero3

        if not all([day2_morning_hero1_seen, day2_morning_hero2_seen, day2_morning_hero3_seen]):
            jump day2_morning_hero_choice


    label day2_morning_hero1:
        $ day2_morning_hero1_seen = True
        return

    label day2_morning_hero2:
        $ day2_morning_hero2_seen = True
        return

    label day2_morning_hero3:
        $ day2_morning_hero3_seen = True
        return

    return

label day2_morning_combat:
    pass
    return

label day2_morning_dinner:
    pass
    return