
label start:
    # call screen debug_menu
    
    call day0_guide_backstory from _call_day0_guide_backstory
    
    call day1_backstory_cutscene from _call_day1_backstory_cutscene
    call day1_combat_intro from _call_day1_combat_intro

    call day2_combat from _call_day2_combat
    call day2_dinner from _call_day2_dinner
    call day2_dream from _call_day2_dream

    call day3_combat from _call_day3_combat
    call day3_dinner from _call_day3_dinner
    call day3_dream from _call_day3_dream
    call day3_night_combat from _call_day3_night_combat

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
default guide = DynamicCharacter('guide_name')
default guide_name = '???'

default guide_dark = DynamicCharacter('guide_dark_name', what_prefix='{b}{cps=30}', what_suffix='{/cps}{/b}')
default guide_dark_name = '???'

default gavin = DynamicCharacter('gavin_name')
default gavin_name = '???'
default gavin_score = 0

default lance = DynamicCharacter('lance_name')
default lance_name = '???'
default lance_score = 0

default morgan = DynamicCharacter('morgan_name')
default morgan_name = '???'
default morgan_score = 0

default radio = DynamicCharacter('radio_name', what_prefix='{i}', what_suffix='{/i}')
default radio_name = 'Radio'

default gwen = DynamicCharacter('gwen_name')
default gwen_name = 'Gwen'

default mother = DynamicCharacter('mother_name')
default mother_name = 'Mother'

default lucas = DynamicCharacter('lucas_name')
default lucas_name = 'Lucas'

default mordred = DynamicCharacter('mordred_name')
default mordred_name = '???'

## Custom transitions
default transition_hold_seconds = 1.0

label restore_from_combat:
    window show
    $ config.allow_skipping = True
    $ quick_menu = True
    $ _skipping = True
    $ _rollback = True
    return

label end_scene_fade_to_black:
    $ quick_menu = False
    window hide
    scene backdrop_black with dissolve
    stop music fadeout 1.0
    stop music_extra fadeout 1.0
    stop music_extra2 fadeout 1.0
    stop sound fadeout 1.0
    stop sound_extra fadeout 1.0
    $ quick_menu = True
    return

label end_scene_fade_to_black_pause:
    $ quick_menu = False
    window hide
    scene backdrop_black with dissolve
    stop music fadeout 1.0
    stop music_extra fadeout 1.0
    stop music_extra2 fadeout 1.0
    stop sound fadeout 1.0
    stop sound_extra fadeout 1.0
    pause transition_hold_seconds
    $ quick_menu = True
    $ transition_hold_seconds = 1.0
    return

label end_scene_fade_to_black_instant:
    $ quick_menu = False
    window hide
    scene backdrop_black with None
    call cut_music_and_sfx from _call_cut_music_and_sfx
    $ quick_menu = True
    return

label end_scene_fade_to_black_instant_pause:
    $ quick_menu = False
    scene backdrop_black
    call cut_music_and_sfx from _call_cut_music_and_sfx_1
    pause transition_hold_seconds
    $ quick_menu = True
    $ transition_hold_seconds = 1.0
    return

label cut_music_and_sfx:
    stop music fadeout 0.0
    stop music_extra fadeout 0.0
    stop music_extra2 fadeout 0.0
    stop sound fadeout 0.0
    stop sound_extra fadeout 0.0
    return

label cutscene_darkness_possesses_gavin:
    window hide
    $ quick_menu = False
    pause 1.0
    scene backdrop_black
    show ending_1 with Dissolve(2.0)
    pause 3.0
    hide ending_1
    show ending_2 with Dissolve(2.0)
    pause 3.0
    hide ending_2
    show ending_3 with Dissolve(2.0)
    pause 3.0
    hide ending_3
    show ending_4 with Dissolve(2.0)
    pause 3.0
    hide ending_4
    show ending_5 with Dissolve(2.0)
    pause 3.0
    hide ending_5
    show ending_6 with Dissolve(2.0)
    pause 3.0
    hide ending_6 with Dissolve(2.0)
    pause 1.5
    $ quick_menu = True
    window show
    return

label cutscene_morgan_presses_button:
    window hide
    $ quick_menu = False
    pause 1.0
    scene backdrop_black
    show end_morgan_1 with Dissolve(2.0)
    pause 3.0
    hide end_morgan_1
    show end_morgan_2 with Dissolve(2.0)
    pause 3.0
    hide end_morgan_2
    show end_morgan_3 with Dissolve(2.0)
    pause 3.0
    hide end_morgan_3 with Dissolve(2.0)
    pause 1.5
    $ quick_menu = True
    window show
    return

## Screen effects
transform flash_overlay:
        alpha 0.0
        linear 0.3 alpha 0.8
        linear 1.0 alpha 0.0

transform flash_overlay_quick_bright:
        alpha 0.0
        linear 0.3 alpha 1.0
        pause 0.3
        linear 0.4 alpha 0.0

transform flash_overlay_quick_bright_hold:
    alpha 0.0
    linear 0.2 alpha 1.0
    "backdrop_black" with dissolve

## Custom sprite positions
# Left grouping
transform grouped_left_gavin:
    anchor (0.0, 1.0)
    xpos 0.00
    ypos 1.15

transform grouped_left_lance:
    anchor (0.0, 1.0)
    xpos 0.18
    ypos 1.15

transform grouped_left_morgan:
    anchor (0.0, 1.0)
    xpos 0.36
    ypos 1.15

# Center grouping
transform grouped_center_gavin:
    anchor (0.5, 1.0)
    xpos 0.33
    ypos 1.15

transform grouped_center_lance:
    anchor (0.5, 1.0)
    xpos 0.5
    ypos 1.15

transform grouped_center_morgan:
    anchor (0.5, 1.0)
    xpos 0.67
    ypos 1.15

# Right grouping
transform grouped_right_gavin:
    anchor (1.0, 1.0)
    xpos 0.62
    ypos 1.15

transform grouped_right_lance:
    anchor (1.0, 1.0)
    xpos 0.80
    ypos 1.15

transform grouped_right_morgan:
    anchor (1.0, 1.0)
    xpos 0.98
    ypos 1.15

# Lined up separate center
transform linedup_center_gavin:
    anchor (0.5, 1.0)
    xpos 0.25
    ypos 1.0
    zoom 0.9

transform linedup_center_lance:
    anchor (0.5, 1.0)
    xpos 0.5
    ypos 1.0
    zoom 0.9

transform linedup_center_morgan:
    anchor (0.5, 1.0)
    xpos 0.75
    ypos 1.0
    zoom 0.9

## Special screens


