label ending_the_truth:
    'ENDING - THE TRUTH'
    ## Sound of FOOTSTEPS. A DRONING AMBIANCE. A KEYCARD. A MECHANICAL DOOR.
    return

label ending_the_end_of_the_world:
    'ENDING - THE END OF THE WORLD'
    return

label ending_boss:
    'ENDING - BOSS COMBAT'
    return

label ending_choices:
    'ENDING - CHOICE TREE'
    if gavin_score >= 2 and lance_score >= 2 and morgan_score >= 2:
        call ending_good from _call_ending_good
    elif gavin_score <= -2 and lance_score <= -2 and morgan_score <= -2:
        call ending_bad from _call_ending_bad
    else:
        call ending_neutral from _call_ending_neutral

    label ending_good:
        'ENDING - GOOD'
        return

    label ending_neutral:
        'ENDING - NEUTRAL'
        return

    label ending_bad:
        'ENDING - BAD'
        return

label ending_credits:
    'ENDING - CREDITS'
    return