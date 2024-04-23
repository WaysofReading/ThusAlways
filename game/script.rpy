
label start:
    # call combat_test
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
    call day4_dinner from _call_day4_dinner
    call day4_dream from _call_day4_dream

    call day5_morning from _call_day5_morning

    call ending_the_truth from _call_ending_the_truth
    call ending_the_end_of_the_world from _call_ending_the_end_of_the_world
    call ending_boss from _call_ending_boss

    call ending_credits from _call_ending_credits
    call close from _call_close
    return

label close:
    'END OF FILE'
    return

# Initialize game-scope variables

## Character variables

define guide = DynamicCharacter('guide_name')
define guide_name = '???'

define guide_dark = DynamicCharacter('guide_dark_name', what_prefix='{b}', what_suffix='{/b}')
define guide_dark_name = '???'

define gavin = DynamicCharacter('gavin_name')
define gavin_name = '???'
define gavin_score = 0

define lance = DynamicCharacter('lance_name')
define lance_name = '???'
define lance_score = 0

define morgan = DynamicCharacter('morgan_name')
define morgan_name = '???'
define morgan_score = 0

define radio = DynamicCharacter('radio_name', what_prefix='{i}', what_suffix='{/i}')
define radio_name = 'Radio'

define gwen = DynamicCharacter('gwen_name')
define gwen_name = 'Gwen'

define mother = DynamicCharacter('mother_name')
define mother_name = 'Mother'

define lucas = DynamicCharacter('lucas_name')
define lucas_name = 'Lucas'

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

## Custom screen effects

define screen_shake_light = Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=5)
define screen_shake_mid = Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
define screen_shake_strong = Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)

# https://lemmasoft.renai.us/forums/viewtopic.php?p=486793#p486793
transform sprite_shake_light(rate=0.03):
    linear rate xoffset 2 yoffset -6
    linear rate xoffset -2.8 yoffset -2
    linear rate xoffset 2.8 yoffset -2
    linear rate xoffset -2 yoffset -6
    linear rate xoffset +0 yoffset +0
    repeat 2

transform sprite_bounce_light(rate=0.1):
    linear rate xoffset 0 yoffset -6
    linear rate xoffset +0 yoffset +0
    repeat 2