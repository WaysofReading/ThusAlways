define day3_morning_hero1_seen = False
define day3_morning_hero2_seen = False
define day3_morning_hero3_seen = False

label day3_morning:

    label day3_morning_hero_choice:
        menu:
            'hero 1':
                call hero1_path
                $ day3_morning_hero1_seen = True
            'hero 2':
                call hero2_path
                $ day3_morning_hero2_seen = True
            'hero 3':
                call hero3_path
                $ day3_morning_hero3_seen = True

        if not all([day3_morning_hero1_seen, day3_morning_hero2_seen, day3_morning_hero3_seen]):
            jump day3_morning_hero_choice

    return

label day3_combat:
    pass
    return

label day3_dinner:
    pass
    return

label day3_dream:
    pass
    return