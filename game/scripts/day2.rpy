define day2_morning_hero1_seen = False
define day2_morning_hero2_seen = False
define day2_morning_hero3_seen = False

label day2_morning:

    label day2_morning_hero_choice:
        menu:
            'hero 1':
                call hero1_path
                $ day2_morning_hero1_seen = True
            'hero 2':
                call hero2_path
                $ day2_morning_hero2_seen = True
            'hero 3':
                call hero3_path
                $ day2_morning_hero3_seen = True

        if not all([day2_morning_hero1_seen, day2_morning_hero2_seen, day2_morning_hero3_seen]):
            jump day2_morning_hero_choice

    return

label day2_combat:
    pass
    return

label day2_dinner:
    pass
    return

label day2_dream:
    pass
    return