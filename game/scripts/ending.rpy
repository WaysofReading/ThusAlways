label ending_the_truth:
    pass
    return

label ending_the_end_of_the_world:
    pass
    return

label ending_boss:
    pass
    return

label ending_choices:

    if hero1_score >= 2 and hero2_score >= 2 and hero3_score >= 2:
        call ending_good
    elif hero1_score <= -2 and hero2_score <= -2 and hero3_score <= -2:
        call ending_bad
    else:
        call ending_neutral

    label ending_good:
        pass
        return

    label ending_neutral:
        pass
        return

    label ending_bad:
        pass
        return

label ending_credits:
    pass
    return