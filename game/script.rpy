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

# Position definitions

label start:
    call day0_hermit_backstory from _call_day0_hermit_backstory
    call day1_backstory_cutscene from _call_day1_backstory_cutscene
    call day1_combat_intro from _call_day1_combat_intro
    call day2_morning from _call_day2_morning
    call close from _call_close
    return

label close:
    "END OF FILE"
    return