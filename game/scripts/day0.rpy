label day0_hermit_backstory:
    play music bgm_solemn fadein 1.0

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

    show hero1 at Position(xpos=0.2, ypos=0.7)
    show hero2 at Position(xpos=0.4, ypos=0.7)
    show hero3 at Position(xpos=0.6, ypos=0.7)
    show hero4 at Position(xpos=0.8, ypos=0.7)
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

label day0_backstory_cutscene:
    
    scene fnc_cabing1_day1
    with dissolve
    
    hermit "The year is 4279. It\'s one of the only things I keep track of anymore."
    hermit "Days, weeks, months, all are mostly irrelevant. News is meaningless when there will be no record of it kept. Faces seen and names spoken will not last more than another year or two."
    hermit "Last year, the ocean sank another seven meters, and four more mountains collapsed in on themselves, taking their villages with them."
    hermit "Trees continue to grow thinner and thinner."
    hermit "No one has seen grass in ages."
    hermit "It\'s a quiet morning, and this world is ending."

    scene burnt_food
    with dissolve

    hermit "The vegetables in my garden barely make it to maturity these days."
    hermit "Game is more plentiful, but the animals are starting to die out, too. Their foraging can only take them so far."
    hermit "But breakfast today is a feast fit for a king."

    scene fnc_cabing1_day1
    with dissolve

    hermit "I\'ve lived in this house for several years now. I\'ve been lucky."
    hermit "Rare is the structure that has lasted more than a decade. Whoever lived here before took very good care of it."
    hermit "Its close proximity to a surviving town isn\'t quite ideal, but it\'s certainly not the end of the world."
    hermit "... That's already happening."
    hermit "But I\'m happy."
    hermit "It\'s quiet here. It\'s peaceful."
    hermit "The town is fortified on all sides by hills and mountains that haven\'t yet collapsed. Creatures take refuge from harsh sandy winds."
    hermit "There\'s even a stream. Imagine that! A stream of water..."
    hermit "This is a good place to be in preparation for the end of the world."

    scene stove_and_figure
    with dissolve

    hermit "It\'s been a long time coming. I was never meant to last this long, but even so, no one expected things to fall apart so quickly."
    hermit "When it all started coming down, I\'d hoped someone would find me quickly. I\'d hoped someone would brandish their steel and take my head quickly; this all was something I never wanted to see."
    hermit "But no one came for me."
    hermit "No one has come."
    hermit "At this rate, no one {i}is{/i} coming. They would have come by now."
    hermit "Going out with the rest of the world is the only option left."
    hermit "I hope the sun will be warm."

    scene fnc_cabing1_day1
    with dissolve
    hermit "... Let\'s see. Breakfast is made. The windows are open. The morning laundry is drying. Next, I--"

    
    play sound door_knock volume 1.0
    stop music fadeout 0.0
    pause 2.0
    play music bgm_drone fadein 0.0 volume 2.0

    hermit "... Was... that... Did I hear..?"
    hermit "No. Certainly not. Just a stray rock. Or two."

    play sound door_knock volume 1.5

    scene backdrop_white
    show hero1 at Position(xpos=0.2, ypos=0.7)
    show hero2 at Position(xpos=0.4, ypos=0.7)
    show hero3 at Position(xpos=0.6, ypos=0.7)
    show hero4 at Position(xpos=0.8, ypos=0.7)
    show overlay_window

    hermit "... No... {i}No{/i}..."

    $ sshake = Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=10)
    scene fnc_cabing1_day1
    with sshake

    hermit "Now? {i}Now?{/i} After all this time?"
    hermit "After all these years?"
    hermit "What kind of joke is this? Go away! No one is here! Your source was wrong!"
    hermit "Just... go home, live out the rest of your life happily!"
    hermit "Don't... don't let this..."
    
    hero1 "\"Hello? Is anyone home?\""
    hero2 "\"He could be out hunting while it's cool...\""
    hero3 "\"Hunting? Hunting {i}what{/i}? Mice?\""

    menu:
        "Answer the door":
            jump answer_door
        "Stay quiet":
            jump stay_quiet

    label stay_quiet:
        hermit "I can\'t answer them."
        hermit "I can\'t subject them to their fate."
        hermit "This ends {i}now{/i}."
        hermit "I\'ll wait for them to leave, then I\'ll have to move out. Go elsewhere. Far, far away where they won\'t follow me."
        hermit "..."
        hermit "..."

        play sound footsteps

        hermit "..."
        hermit "... Thank the gods. Now I just need to --"

        scene backdrop_white
        show hero1 happy at Position(xpos=0.2, ypos=0.0):
            zoom 3.0
        show overlay_window with sshake
        
        hermit "GODS DAMN IT."
        hermit "DOESN'T THIS LITTLE TWERP KNOW BETTER THAN TO SNOOP IN PEOPLE\'S WINDOWS?!"
        hermit "..."
        hermit "... Damn it."
        hermit "There's no getting out of this one now."
        hermit "Unless..."

        menu:
            "Lie to the heroes":
                jump lie_to_heroes
            "Answer the door":
                jump answer_door
        
    label lie_to_heroes:
        show overlay_pain with sshake
        hide overlay_pain
        
        hermit "{b}You can't.{/b}"
        hermit "D-Damn it."
        hermit "But if they meet me --"

        $ sshake = Shake((0.5, 1.0, 0.5, 1.0), 1.0, dist=20)
        show overlay_pain with sshake
        hide overlay_pain

        hermit "{b}You can't.{/b}"
        hermit "{b}Your sacred duty is to --{/b}"

        hermit "Oh for the love of -- {i}shut up{/i}."
        hermit "... This is it, then."
        
    label answer_door:
        scene cabin_door_closed
        show hermit at right
        pause 2.0
        play sound door_opening
        pause 1.0
        scene backdrop_grass_sky
        show hero2 happy at Position(xpos=0.5, ypos=0.55):
            zoom 0.5
        show hero3 happy at Position(xpos=0.6, ypos=0.55):
            zoom 0.5
        show hero1 happy at Position(xpos=0.35, ypos=0.4):
            zoom 1.0
        show cabin_door_open
        show hermit at right
        
        hero1 "\"It's you! You're --\""
        hermit "The man from your dream. I know."
        hero1 "\"The man from my dream!\""
        hermit "I just said that."
        hero1 "..."
        hermit "..."
        hero1 "..."
        hermit "..."
        hero2 "\"... Does he... talk?\""
        # Copy uses no quotes, then quotes, for the next two lines -- clarify intent w/ Syd
        hermit "\"Oh. Shit.\""
        hermit "\"I -- ahem. I speak.\""
        hero1 "\"Oh, great! Uh --\""
        
        play sound throat_clear
        pause 1.0

        # Copy uses single quotes inside double quotes, here -- clarify intent w/ Syd
        hero1 "\"\'Oh great and mighty hermit of times ancient, we are the Chosen Three, as ordained by the last vestiges of the Roots of the World.\'\""
        hero2 "\"\'I am [hero2_name], arcanist and sworn defender of the Chosen.\'\""
        hero3 "\"\'I'm [hero3_name]. I keep them safe. And alive.\'\""
        
        # show hero2 angry
        hero2 "\"{i}(angrily whispering){/i}\n([hero3_name], that's not your line!)\""
        hero1 "\"And I am [hero1_name], leader of the Chosen Three --\""
        hero2 "\"{i}(whispering){/i}\n(We said we weren't going to have a leader?)\""
        hero1 "\"-- and banisher of the Hidden Darkness.\""
        hero1 "\"We seek your greatest arts of swordsmanship, magic, and healing, in the pursuit of reclaiming this world from death.\""
        hero1 "\"It is our sacred destiny.\""
        hero1 "\"We are chosen. We are the heroes of destiny. We are the heroes who will save the world.\""
        hero1 "\"We are the heroes who will banish the evil that plagues the planet, and live to --\""
        hermit "\"Good hell, I thought that spiel couldn\'t get any worse.\""

        # Make sprites shake slightly?
        show hero1 surprised
        show hero2 surprised
        show hero3 surprised

        hermit "\"Yeah, yeah, I know why you kids are here.\""
        hero1 "\"You... do?\""
        hero1 "\"Er, of course you do! After all, you're so wise and --\""
        hermit "\"Let me go get my rod so I can kick your ass.\""
        hero1 "\"You -- WHAT?\""

        play sound door_slam
        scene cabin_door_closed
        show hermit at right
        pause 1.0
        scene fnc_cabing1_day1

        hermit "Well, this is it."
        hermit "The beginning of the next."
        hermit "... It wasn't supposed to be this way."
        hermit "... I better make sure they're ready. Which they aren't. But at least I should get a good idea of their standing in combat."
        hermit "... Now, where'd I leave that stupid thing..."

        "END SCENE"
        return

    return
