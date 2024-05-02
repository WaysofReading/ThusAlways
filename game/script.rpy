
label start:
    call screen debug_menu

    call day0_guide_backstory from _call_day0_guide_backstory
    
    call day1_backstory_cutscene from _call_day1_backstory_cutscene
    call day1_combat_intro from _call_day1_combat_intro
    call day1_post_combat from _call_day1_post_combat

    call day2_morning from _call_day2_morning
    call day2_combat from _call_day2_combat
    call day2_dinner from _call_day2_dinner
    call day2_dream from _call_day2_dream

    call day3_morning from _call_day3_morning
    call day3_combat from _call_day3_combat
    call day3_dinner from _call_day3_dinner
    call day3_dream from _call_day3_dream
    call day3_night_combat from _call_day3_night_combat

    call day4_morning from _call_day4_morning
    call day4_combat from _call_day4_combat
    call day4_dream from _call_day4_dream

    call day5_morning from _call_day5_morning

    call ending_the_truth from _call_ending_the_truth
    call ending_last_scene from _call_ending_last_scene
    call ending_credits from _call_ending_credits

    call close from _call_close
    return

label close:
    'The End'
    return

label debug_menu:
    call screen debug_menu

label end_scene_fade_to_black:
    scene backdrop_black
    stop music fadeout 1.0
    stop music_extra fadeout 1.0
    stop sound fadeout 1.0
    stop sound_extra fadeout 1.0
    return

label end_scene_fade_to_black_instant:
    scene backdrop_black
    stop music fadeout 0.0
    stop music_extra fadeout 0.0
    stop sound fadeout 0.0
    stop sound_extra fadeout 0.0
    return

screen debug_menu():
    fixed:
        xpos 0 ypos 0
        hbox:
            xpos 0 ypos 0
            spacing 20
            vbox:
                textbutton "Play Full Game" action Return()
        hbox:
            xpos 0 ypos 300
            spacing 20
            vbox:
                textbutton "Day 0 - Guide Backstory" action Jump("day0_guide_backstory")
            vbox:
                textbutton "Day 1 - Backstory Cutscene" action Jump("day1_backstory_cutscene")
                textbutton "Day 1 - Combat Introduction" action Jump("day1_combat_intro")
                textbutton "Day 1 - Post-Combat" action Jump("day1_post_combat")
            vbox:
                textbutton "Day 2 - Morning (NA)" action Jump("day2_morning")
                textbutton "Day 2 - Combat" action Jump("day2_combat")
                textbutton "Day 2 - Dinner" action Jump("day2_dinner")
                textbutton "Day 2 - Dream" action Jump("day2_dream")
        hbox:
            xpos 0 ypos 600
            spacing 20
            vbox:
                textbutton "Day 3 - Morning (NA)" action Jump("day3_morning")
                textbutton "Day 3 - Combat" action Jump("day3_combat")
                textbutton "Day 3 - Dinner" action Jump("day3_dinner")
                textbutton "Day 3 - Dream" action Jump ("day3_dream")
                textbutton "Day 3 - Night Combat" action Jump ("day3_night_combat")
            vbox:
                textbutton "Day 4 - Morning (NA)" action Jump("day4_morning")
                textbutton "Day 4 - Combat" action Jump("day4_combat")
                textbutton "Day 4 - Dream" action Jump("day4_dream")
            vbox:
                textbutton "Day 5 - Morning" action Jump("day5_morning")
                textbutton "Ending - The Truth" action Jump("ending_the_truth")
                textbutton "Ending - Last Scene" action Jump("ending_last_scene")
                textbutton "Ending - Credits" action Jump("ending_credits")

## Character variables
# Set defaults to real names and change to '???' in day0/day1
define guide = DynamicCharacter('guide_name')
define guide_name = 'Guide'

define guide_dark = DynamicCharacter('guide_dark_name', what_prefix='{b}{cps=20}', what_suffix='{/cps}{/b}')
define guide_dark_name = 'Guide (?)'

define gavin = DynamicCharacter('gavin_name')
define gavin_name = 'Gavin'
define gavin_score = 0

define lance = DynamicCharacter('lance_name')
define lance_name = 'Lance'
define lance_score = 0

define morgan = DynamicCharacter('morgan_name')
define morgan_name = 'Morgan'
define morgan_score = 0

define radio = DynamicCharacter('radio_name', what_prefix='{i}', what_suffix='{/i}')
define radio_name = 'Radio'

define gwen = DynamicCharacter('gwen_name')
define gwen_name = 'Gwen'

define mother = DynamicCharacter('mother_name')
define mother_name = 'Mother'

define lucas = DynamicCharacter('lucas_name')
define lucas_name = 'Lucas'

define mordred = DynamicCharacter('mordred_name')
define mordred_name = 'General Mordred'

## Custom sprite positions

define grouped_left_pos1 = Position(xpos=0.2, ypos=0.65)
define grouped_left_pos2 = Position(xpos=0.3, ypos=0.7)
define grouped_left_pos3 = Position(xpos=0.4, ypos=0.65)

define grouped_center_pos1 = Position(xpos=0.4, ypos=0.65)
define grouped_center_pos2 = Position(xpos=0.5, ypos=0.7)
define grouped_center_pos3 = Position(xpos=0.6, ypos=0.65)

define grouped_right_pos1 = Position(xpos=0.6, ypos=0.65)
define grouped_right_pos2 = Position(xpos=0.7, ypos=0.7)
define grouped_right_pos3 = Position(xpos=0.8, ypos=0.7)

define linedup_center_pos1 = Position(xpos=0.35, ypos=0.7)
define linedup_center_pos2 = Position(xpos=0.5, ypos=0.7)
define linedup_center_pos3 = Position(xpos=0.65, ypos=0.7)
