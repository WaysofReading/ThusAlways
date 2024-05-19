label day1_backstory_cutscene:
    ## NEW SCENE: Hermit Backstory Introduction
    ## FADE IN sound of FIREPLACE first, then FADE IN to CABIN, INTERIOR. Description pending. FADE IN new music track.
    play music_extra foley_fireplace fadein 1.0 volume 0.5
    scene cabin_interior with dissolve
    play music bgm_solemn fadein 2.0
    
    guide "The year is 4279. It’s one of the only things I keep track of, anymore."
    guide "It helps me to know the end is that much closer."
    guide "Last year, the ocean sank another seven meters, and four more mountains collapsed in on themselves, taking their villages with them."
    guide "Trees continue to grow thinner and thinner."
    guide "No one has seen grass in ages."
    guide "I miss the feel of it. I miss the sound of birds. I miss when the sky was blue."
    guide "It’s a quiet morning, and this world is ending."
    guide "And I intend to end with it."

    ## FADE IN kitchen 1
    scene kitchen_1 with dissolve
    guide "It’s because I’m going with it that I’m happy."
    guide "It’s quiet here. It’s peaceful."
    guide "And so long as it stays quiet, so long as I stay unbothered..."
    guide "So long as my dreams do not come to fruition, and the fate of the world falls out of my hands..."
    guide "Then this suffering can end."
    guide "This is a good place to be in preparation for the end of the world."

    ## A shot of the PROTAGONIST -- mostly just a robed figure -- hunched over a small stove, next to a flickering electric light.
    scene kitchen_2 with dissolve

    guide "I was never meant to last this long. It’s been a long time coming, but even so, no one expected things to fall apart so quickly."
    guide "At first, I’d hoped someone would brandish their steel and take my head quickly; this all was something I never wanted to see."
    guide "But as time went on, and the heroes I expected to mentor never came, I realized... I want to remain."
    guide "I want to be the last one left when the stars all go out and the sun dims, even if it means being alone. Even if it means agony. And insanity."
    guide "Going out with the rest of the world is the only option left."
    guide "I hope the sun will be warm today."

    ## Return to CABIN INTERIOR
    scene cabin_interior with dissolve

    guide "... Let’s see. Breakfast is made. The windows are open. The laundry is drying. Next, I --"

    ## There’s a KNOCK at the door. The music and fireplace sfx stop abruptly, replaced with a sinister droning tone.
    play sound door_knock volume 1.0
    stop music fadeout 0.0
    play music bgm_drone fadein 0.0
    pause 3.0
    guide "... Was... that... Did I hear...?"
    guide "No. Certainly not. Just a stray rock. Or two."
    guide "No one knows I live here. The nearest settlement is miles away."

    ## The KNOCK returns.
    play sound door_knock volume 1.5
    
    guide "... It {i}can’t{/i} be..."

    ## The PROTAGONIST stands and peers out through a crack in the door. In the prototype this can be the same shot as the shot of the heroes in the DREAM INTRO.
    scene door_and_window_background
    show lance:
        anchor (0.0, 1.0)
        xpos 0.45
        ypos 1.0
    show morgan:
        anchor (0.0, 1.0)
        xpos 0.55
        ypos 1.0
    show gavin:
        anchor (0.0, 1.0)
        xpos 0.25
        ypos 1.0
    show cabin_window

    guide "... No... {i}No{/i}..."

    ## The shot returns to CABIN INTERIOR, shaking to symbolize the PROTAGONIST stumbling backwards.
    scene cabin_interior with screen_shake_mid

    guide "Now? {i}Now?{/i} After all this time?"
    guide "After all these years?"
    guide "What kind of joke is this? Go away! No one is here! Your source was wrong! There’s no one here who can teach you anything!"
    guide "Just... go home, and live out what remains of your lives happily!"
    
    ## One of the children calls through the door.
    
    gavin "“Hello? Is anyone home?”"
    lance "“He could be out hunting while it’s still cool...”"
    morgan "“Hunting? Hunting {i}what?{/i} Mice?”"
    
    ## CHOICE:
    ## > Answer the door
    ## > Stay quiet.
    ## > Stay quiet:

    menu:
        "Answer the door.":
            jump day1_choice_answer_door
        "Stay quiet.":
            jump day1_choice_stay_quiet
        
    label day1_choice_stay_quiet:
        guide "I can’t answer them."
        guide "I can’t subject them to their fate."
        guide "This ends {i}now{/i}. This horrid cycle ends {i}here{/i}."
        guide "I’ll wait for them to leave, then I’ll have to move out. Go elsewhere. Far, far away where they won’t follow me."
        guide "It’s for their own good. For everyone’s."
        guide "{cps=30}...{/cps}"
        guide "{cps=30}...{/cps}"

        ## There are FOOTSTEPS as it sounds like the children walk away.
        play sound footsteps

        guide "{cps=30}...{/cps}"
        guide "... Thank the gods. Now I just need to --"

        ## Cut to shot of one of the children looking through the window with a big smile. A loud sound effect plays and the screen shakes a little, but this isn’t necessarily a jumpscare.
        scene door_and_window_background
        show gavin happy:
            anchor (0.0, 1.0)
            xpos 0.2
            ypos 1.65
            zoom 1.5
        play sound jumpscare
        show cabin_window with screen_shake_mid

        guide "GODS DAMN IT."
        guide "DOESN'T THIS LITTLE TWERP KNOW BETTER THAN TO SNOOP IN PEOPLE’S WINDOWS?!"

        ## Return shot to CABIN INTERIOR
        scene cabin_interior

        guide "{cps=30}...{/cps}"
        guide "... Damn it."
        guide "There’s no getting out of this one now."
        guide "Unless..."

        ## CHOICE:
        ## >Lie to the heroes
        ## >Answer the door

        menu:
            "Lie to the heroes.":
                jump day1_choice_lie
            "Answer the door.":
                jump day1_choice_answer_door
        
        ## >Lie to the heroes:        
        label day1_choice_lie:

            ## The edges of the screen flash red. There’s a grunt of pain. CONSIDER: Maybe every instance of the Hidden Darkness should be typewriter effect?
            $ quick_menu = False
            show overlay_red onlayer foremost at flash_overlay with screen_shake_mid
            $ quick_menu = True
            guide_dark "You can’t."
            guide "D-Damn it. It’s already starting..."
            guide "But if they meet me --"

            ## The screen flashes red again, more powerful this time.
            $ quick_menu = False
            show overlay_red onlayer foremost at flash_overlay with screen_shake_mid
            $ quick_menu = True
            guide_dark "You can’t."
            guide_dark "Your sacred duty is to --"
            guide "Oh for the love of -- {i}shut up{/i}."
            guide "... This is it, then."
            jump day1_choice_answer_door            

    ## >Answer the door:
    label day1_choice_answer_door:
        ## A shot of the PROTAGONIST in front of the closed door, then, with the door open. Three HEROES stand on the front porch, all children hardly older than ten or twelve. HERO 1 is a boy with dark skin, curly dark-brown hair and a red cloak draped over one shoulder. There’s a sword at his hip, rusted along one side but otherwise in fairly decent condition. HERO 2 is a boy with light skin, dark-blonde hair tied back in a bun, and a book strapped to his hip like a weapon. HERO 3 is a girl with pale skin, black hair, and sunken eyes. She looks somehow drained of life, husk-like, and leans heavily on a metal pole used as a staff.
        scene cabin_door_closed
        play music bgm_movie_score_a fadein 1.0
        pause 0.5
        play sound door_opening
        pause 1.0
        hide cabin_door_closed
        show door_and_window_background
        show morgan:
            xpos 0.55
            ypos 0.55
            zoom 0.5
        show lance:
            xpos 0.48
            ypos 0.55
            zoom 0.5
        show gavin:
            anchor (0.0, 1.0)
            xpos 0.3
            ypos 1.2
            zoom 1.0
        show cabin_door_open
        pause 0.5
        show gavin happy with dissolve
        gavin "“It’s you! You’re --”"
        guide "The man from your dream. I know."
        gavin "“The man from my dream!”"
        guide "I just said that."
        gavin "“{cps=30}...{/cps}”"
        guide "{cps=30}...{/cps}"

        show gavin neutral with dissolve
        gavin "“{cps=30}...{/cps}”"
        guide "{cps=30}...{/cps}"
        lance "“... Does he... talk?”"
        guide "Oh. Shit."
        guide "“I – ahem. I speak.”"

        show gavin happy with dissolve
        gavin "“Oh, great! Uh --”"
        
        ## HERO 1 clears his throat.
        play sound throat_clear
        pause 1.0

        show gavin neutral with dissolve
        gavin "“‘Oh great and mighty hermit of times ancient, we are the Chosen Three, as ordained by the last vestiges of the Roots of the World.’”"

        $ lance_name = "Lance"
        show lance at sprite_bounce_light
        lance "“‘I am Lance, arcanist and sworn defender of the Chosen.’”"

        $ morgan_name = "Morgan"
        show morgan at sprite_bounce_light
        morgan "“I’m Morgan. I keep them safe. And alive.”"

        show lance annoyed with dissolve
        lance "“(Morgan, that’s not your line!)”"

        $ gavin_name = "Gavin"
        show gavin at sprite_bounce_light
        gavin "“‘And I am Gavin, leader of the Chosen Three --’”"

        show lance annoyed with dissolve
        lance "“(We said we weren’t going to have a leader?)”"
        gavin "“‘-- and banisher of the Hidden Darkness.’”"
        
        show lance neutral with dissolve
        gavin "“‘We seek your greatest arts of swordsmanship, magic, and healing, in the pursuit of reclaiming this world from death.’”"
        gavin "“‘It is our sacred destiny.’”"
        gavin "“‘We are Chosen. We are the heroes of destiny. We are the heroes who will save the world.’”"
        gavin "“‘We are the heroes who will banish the evil that plagues the planet, and live to --’”"
        guide "“Good hell, I thought this spiel couldn’t get any worse.”"
        stop music fadeout 0.0
        
        ## All three HEROES are shocked (SP Sprites) by the callous interruption
        show lance surprised
        show gavin surprised
        show morgan surprised
        guide "“Yeah, yeah, I know why you kids are here.”"
        gavin "“You... do?”"

        show gavin neutral with dissolve
        gavin "“Er, of course you do! After all, you’re so wise and --”"
        guide "“Let me go get my staff so I can kick your ass.”"
        
        show gavin surprised
        gavin "“You -- {i}WHAT{/i}?”"
        
        ## The door slams shut. Return to CABIN, INTERIOR
        play sound door_slam
        scene cabin_door_closed
        pause 1.0
        scene cabin_interior
        guide "Well, this is it."
        guide "The beginning of the next cycle, when it should have been the beginning of the end."
        guide "... It wasn’t supposed to be this way."
        guide "There’s no way they are ready. But I suppose I should at least get an idea of their standing in combat."
        guide "Now, where’d I leave that damn weapon..."
        
        ## FADE OUT to black
        ## FADE OUT music/sfx
        call end_scene_fade_to_black from _call_end_scene_fade_to_black_1

    ## END SCENE
    return

label day1_combat_intro:
    ## NEW SCENE: Combat Introduction
    ## FADE IN to BACK OF CABIN. FADE IN music. Combat has not been initiated yet. The HEROES all stand in a line in front of the HERMIT
    scene cabin_exterior with fade
    play music bgm_frozen_landscape fadein 1.0
    show gavin at grouped_center_gavin
    show lance at grouped_center_lance
    show morgan at grouped_center_morgan
    guide "I haven’t brought out my combat equipment in a long, long time. Whoever owned this place last was also a fighter, though. I never {i}did{/i} clean up their training dummies."
    guide "This will be useful for the kids in the long run; but ultimately, they’re fighting {i}me{/i}."
    lance "“Sir? What is this all for?”"
    guide "“Don’t call me sir.”"
    
    show lance annoyed
    lance "“... Dude?”"
    
    show overlay_red onlayer foremost at flash_overlay
    guide_dark "{i}Master{/i}."
    guide "“Teacher. Wait -- Guide.”"
    lance "“‘Guide?’”"
    lance "“Well... {i}Guide{/i}... what exactly is happening here?”"
    $ guide_name = 'The Guide'
    $ guide_dark_name = 'The Guide (?)'
    guide "“What does it look like?”"
    lance "“It {i}appears{/i} that you’re preparing a training grounds, in service of our education to banish the Hidden Darkness, but it’s rudimentary at best and insulting at worst.”"
    lance "“You have yet to ask about our experience in the {i}slightest{/i}. I can assure you we are more than capable enough to move past basics into --”"
    guide "“Nope.”"

    ## GAVIN and MORGAN SP sprites
    show gavin surprised
    show morgan surprised
    show lance angry
    lance "“‘{i}Nope!?{/i}’”"
    guide "“Nope. You’re getting tested, whether you like it or not. Now, here’s what’s going to happen.”"
    guide "“The three of you are going to fight {i}me{/i}. You’re going to use the full extent of your abilities and power, and I’ll have to counter that.”"

    ## MORGAN and LANCE N sprites
    ## SPRITE GAVIN U
    show morgan neutral
    show lance neutral
    show gavin uncomfortable
    gavin "“Guide... we could seriously hurt you. If we take you down --”"
    guide "“That won’t be happening.”"
    
    show morgan uncomfortable
    morgan "“You’re just one guy.”"
    guide "“One guy who’s about to kick your asses.”"
    guide "“... Butts. You’re children. I keep forgetting.”"
    guide "“Draw your weapons, or prepare your spells, or... whatever it is you kids do.”"
    gavin "“If you’re sure, Guide...”"

    show lance annoyed
    lance "“What a waste of time...”"

    ## BEGIN COMBAT.
    call combat_encounter_hermit from _call_combat_encounter_hermit

    ## AFTER COMBAT, the HEROES are all licking their wounds and complaining.
    scene cabin_exterior with dissolve
    play music bgm_frozen_landscape fadein 1.0
    show gavin sad at grouped_center_gavin
    show lance sad at grouped_center_lance
    show morgan sad at grouped_center_morgan
    with dissolve
    call restore_from_combat from _call_restore_from_combat
    gavin "“Man, you really didn’t hold back, huh?”"
    guide "“Did you expect me to?”"
    guide_dark "Pathetic. They aren’t ready. They’re not strong enough. They’re wasting precious time. As usual, it falls to me to handle the responsibilities of this cycle."
    guide "“The Hidden Darkness will offer you no such quarter.”"
    guide "“You wish to save this world? You wish to save humanity, and life itself?”"
    guide "“You know nothing about the gravity of the task you seek to undertake. You think your status as ‘Chosen’ grants you immunity from failure.”"
    guide "“Your assumptions could not be further from the truth.”"
    guide "“I did not hold back, but if you think defeating me will mean you are ready to fell the Hidden Darkness, you’re all more foolish and ignorant than I thought.”"
    lance "“You’re rejecting us, then. You’re not even giving us a chance.”"
    guide "“I am not rejecting you.”"
    guide "“I {i}am{/i} saying that we’re going to have a {i}lot{/i} of work on our hands.”"
    
    show gavin neutral
    show morgan surprised
    show lance neutral
    guide "“Get off the ground. Clean yourselves up. Unpack, make yourselves comfortable. Your fates are as intertwined with mine as the Roots of the World are with life and death.”"
    guide "“I can’t turn you away. It’s literally impossible for me to.”"
    lance "“You tried to pretend you weren’t home.”"
    guide "“For good reason.”"
    guide "They’ll find out that reason in time. They should have stayed home."
    guide "“Go.”"

    ## The HEROES depart, one by one, leaving the GUIDE alone outside.
    hide gavin with easeoutleft
    hide lance with easeoutleft
    hide morgan with easeoutleft
    stop music fadeout 1.0
    guide_dark "I’ve waited far too long for this. We won’t go easy on them."
    guide "I never planned to. But not for {i}your{/i} sake."
    guide_dark "It will all be the same in the end. Coddle them, abuse them -- no matter your course, they will grow, and the cycle will repeat as it has always been meant to."
    guide_dark "Change is impossible. The ages of man all age the same. All generations grow from the bones of the last."
    guide_dark "Thus, always."
    guide "{cps=30}...{/cps}"

    ## FADE OUT
    ## FADE OUT music/sfx
    call end_scene_fade_to_black from _call_end_scene_fade_to_black_2

    ## END SCENE
    return
