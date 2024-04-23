label day5_morning:
    ## FADE IN CABIN INTERIOR

    guide '“Chosen. Come.”'

    ## All three HEROES slide on screen from the same side. Or fade in, whichever you think looks/fits better.

    guide '“It’s time.”'

    lance '“It -- now? Really? But it’s only been like...”'

    guide '“You’re ready. I can feel it.”'
    guide '“And I know you feel it, too.”'

    ## The HEROES hesitate.

    gavin '“You’re right.”'
    gavin '“It is time.”'

    morgan '“What should we bring?”'

    guide '“Everything you want to.”'
    guide '“You won’t be coming back.”'

    lance '“We won’t? Why?”'

    guide '{b}“You don’t belong here.{/b}”'

    ## There’s a pause.

    gavin '“It was always going to be this way, wasn’t it?”'

    ## LANCE and MORGAN are confused.

    gavin '“Let’s just go.”'

    ## LANCE and MORGAN slide off screen. Only GAVIN is left.

    gavin '“But first...”'
    gavin '“Are you happy with yourself?”'

    menu day5_morning_choice:
        "It was always":
            jump day5_morning_choice_reconvene
        "going to be":
            jump day5_morning_choice_reconvene
        "this way.":
            jump day5_morning_choice_reconvene

    label day5_morning_choice_reconvene:

        ## FADE OUT

        ## END SCENE

        return
