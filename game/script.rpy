# The script of the game goes in this file.

# Initialization

init:
    $ rosterfarleft = Position(xpos=0.2, ypos=0.7)
    $ rosterleft = Position(xpos=0.4, ypos=0.7)
    $ rosterright = Position(xpos=0.6, ypos=0.7)
    $ rosterfarright = Position(xpos=0.8, ypos=0.7)
    $ read_gameplay_tutorial = False
    $ read_battle_tutorial = False
    $ read_all_tutorials = False

# Character definitions

define hermit = DynamicCharacter("hermit_name")
define hermit_name = "???"

define hero1 = DynamicCharacter("hero1_name")
define hero1_name = "A"

define hero2 = DynamicCharacter("hero2_name")
define hero2_name = "B"

define hero3 = DynamicCharacter("hero3_name")
define hero3_name = "C"

define hero4 = DynamicCharacter("hero4_name")
define hero4_name = "D"

label start:
    call opening_cutscene from _call_opening_cutscene
    call backstory_cutscene from _call_backstory_cutscene

    "Would you like to learn how to play?"

    menu:
        "Yes!":
            call tutorial from _call_tutorial
            if read_gameplay_tutorial and read_battle_tutorial:
                $ read_all_tutorials = True
        "No, I want to play the game!":
            pass
    
    return

label opening_cutscene:
    scene backdrop_black
    with fade

    hermit "I remember when the world was young."
    
    scene backdrop_mist
    with fade

    hermit "I still dream of it sometimes. I still dream of that foggy, half-solid air that cloyed thick in our lungs, before it rushed out from us as we took our first tentative steps into the unknown."
    hermit "I remember how the grass sprung up. I remember how the trees shot skyward, almost too tall for their own survival. I remember the flooding streams, the exploding rocks."
    hermit "I remember the way we looked at each other, and smiled..."
    hermit "Even in the wake of everything we'd left behind."
    hermit "..."
    hermit "I remember how we thought, \"This time, things will be different.\""
    hermit "I dream of it."
    hermit "I dream of that promise."

    scene backdrop_black
    with fade

    hermit "It\'s not the only thing I dream of."
    hermit "I wish it was."

    scene backdrop_white
    with dissolve

    show hero1 at rosterfarleft
    show hero2 at rosterleft
    show hero3 at rosterright
    show hero4 at rosterfarright
    with dissolve

    hermit "I dream of four heroes, heroes I don\'t recognize. I don\'t know who they are, or what they look like. All I know is that they are chosen."
    hermit "For what?"
    hermit "..."
    hermit "They come to me."
    hermit "They come to me, and they tell me, \"We are chosen. We are the heroes of destiny. We are the heroes who will save the world.\""
    hermit "\"We are the heroes who will banish the evil that plagues the planet, and live to tell the tale.\""
    hermit "..."

    scene backdrop_black
    with dissolve

    hermit "... I pray I never see them."

    return

label backstory_cutscene:
    "This cutscene introduces the backstory/lore"
    return

label tutorial:
    "This is the game tutorial. What do you want to learn about?"

    label tutorial_menu:
        menu:
            "How do I play?":
                call tutorial_gameplay from _call_tutorial_gameplay
            "How do I fight?":
                call tutorial_battle from _call_tutorial_battle
            "Nevermind...":
                pass
    
    "Would you like to learn about something else?"

    menu:
        "Yes":
            jump tutorial_menu
        "No":
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