# Initialization

# Character definitions

define hermit = DynamicCharacter("hermit_name")
define hermit_name = "???"

define hero1 = DynamicCharacter("hero1_name")
define hero1_name = "Hero 1"
define hero1_score = 0

define hero2 = DynamicCharacter("hero2_name")
define hero2_name = "Hero 2"
define hero2_score = 0

define hero3 = DynamicCharacter("hero3_name")
define hero3_name = "Hero 3"
define hero3_score = 0

define hero4 = DynamicCharacter("hero4_name")
define hero4_name = "Hero 4"

# Position definitions

label start:
    call day0_hermit_backstory from _call_day0_hermit_backstory
    call day1_backstory_cutscene from _call_day1_backstory_cutscene
    call day1_combat_intro from _call_day1_combat_intro

    call day2_morning
    call day2_combat
    call day2_dinner
    call day2_dream

    call day3_morning
    call day3_combat
    call day3_dinner
    call day3_dream

    call day4_morning
    call day4_combat
    call day4_dinner
    call day4_dream

    call day5_morning

    call ending_the_truth
    call ending_the_end_of_the_world
    call ending_boss

    call ending_credits
    call close
    return

label close:
    "END OF FILE"
    return