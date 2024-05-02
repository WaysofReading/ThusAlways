label day5_morning:
    ## NEW SCENE: Day 5 Morning
    ## FADE IN CABIN INTERIOR
    show cabin_interior with fade
    play music bgm_transient fadein 1.0
    guide "“Chosen. Come.”"

    ## All three HEROES slide on screen from the same side. Or fade in, whichever you think looks/fits better.
    ## SPRITES Gavin SD, Morgan SD, Lance N
    show gavin sad at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan sad at grouped_left_pos3
    with easeinleft
    guide "“It’s time.”"

    ## SPRITES Morgan SP, Lance SP
    show morgan surprised
    show lance surprised
    lance "“It -- now? Really? But it’s only been, like --”"
    guide "“You’re ready. I can feel it.”"
    guide "“And I know you feel it, too.”"

    ## SPRITES Gavin A, Morgan SD, Lance N
    ## The HEROES hesitate.
    show gavin annoyed
    show morgan sad
    pause 0.5
    gavin "“You’re right.”"
    gavin "“It is time.”"
    morgan "“What should we bring?”"
    guide "“Everything you want to.”"
    guide "“You won’t be coming back.”"
    lance "“We won’t? Why?”"
    guide "“You don’t belong here.”"

    ## SPRITES Morgan SP, Lance A
    ## There’s a pause.
    show morgan surprised
    show lance annoyed
    pause 0.5

    ## SPRITE Gavin SD
    show gavin sad
    gavin "“It was always going to be this way, wasn’t it?”"

    ## SPRITES Morgan SP, Lance N
    ## LANCE and MORGAN are confused.
    ## SPRITE Gavin A
    show morgan surprised
    show lance neutral
    show gavin annoyed
    gavin "“Let’s just go.”"

    ## LANCE and MORGAN slide off screen. Only GAVIN is left.
    hide lance
    hide morgan
    with easeoutleft
    gavin "“But first...”"
    gavin "“Are you happy with yourself, Guide?”"

    ## CHOICE
    ## >It was always
    ## >going to be
    ## >this way.

    menu:
        "It was always":
            jump day5_morning_end
        "going to be":
            jump day5_morning_end
        "this way.":
            jump day5_morning_end

    label day5_morning_end:
        ## FADE OUT
        call end_scene_fade_to_black
    
    ## END SCENE
    return
