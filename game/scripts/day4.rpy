define day4_morning_hero1_seen = False
define day4_morning_hero2_seen = False
define day4_morning_hero3_seen = False

label day4_morning:

    label day4_morning_hero_choice:
        menu:
            'hero 1':
                call hero1_path
                $ day4_morning_hero1_seen = True
            'hero 2':
                call hero2_path
                $ day4_morning_hero2_seen = True
            'hero 3':
                call hero3_path
                $ day4_morning_hero3_seen = True

        if not all([day4_morning_hero1_seen, day4_morning_hero2_seen, day4_morning_hero3_seen]):
            jump day4_morning_hero_choice

    return

label day4_combat:
    pass
    return

label day4_dinner:
    pass
    return

label day4_dream:
    pass
    return