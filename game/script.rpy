# The script of the game goes in this file.

# Initialization

init:
    $ read_gameplay_tutorial = False
    $ read_battle_tutorial = False
    $ read_all_tutorials = False

# Character definitions

define hermit = DynamicCharacter("hermit_name")
define hermit_name = "???"

define hero1 = DynamicCharacter("hero1_name")
define hero1_name = "Hero 1"

define hero2 = DynamicCharacter("hero2_name")
define hero2_name = "Hero 2"

define hero3 = DynamicCharacter("hero3_name")
define hero3_name = "Hero 3"

define hero4 = DynamicCharacter("hero4_name")
define hero4_name = "Hero 4"

label start:
    call day0_hermit_backstory from _call_day0_hermit_backstory
    call day0_backstory_cutscene from _call_day0_backstory_cutscene

    "Would you like to learn how to play?"

    menu:
        "Yes!":
            call tutorial from _call_tutorial
            if read_gameplay_tutorial and read_battle_tutorial:
                $ read_all_tutorials = True
        "No, I want to play the game!":
            pass
    
    return


label day1_combat_intro:
    pass
    return

label day2_morning:
    pass
    return

label day2_hero1:
    pass
    return

label day2_hero2:
    pass
    return

label day2_hero3:
    pass
    return



label tutorial_gameplay:
    $ read_gameplay_tutorial = True
    "This scene provides instructions on how to play the VN part of the game"
    return

label tutorial_battle:
    $ read_battle_tutorial = True
    "This scene provides instructions on how to play the battle part of the game"
    return