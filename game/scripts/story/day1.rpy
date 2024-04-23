label day1_backstory_cutscene:
    ## FADE IN to CABIN, INTERIOR. Description pending. FADE IN new music track.
    scene fnc_cabing1_day1
    with dissolve
    # music bgm_plaintive fadein 2.0
    
    guide 'The year is 4279. It’s one of the only things I keep track of anymore.'
    guide 'It helps me to know how much closer the end may be. Whether days, weeks, or months from now, it’s coming all the same.'
    guide 'Last year, the ocean sank another seven meters, and four more mountains collapsed in on themselves, taking their villages with them.'
    guide 'Trees continue to grow thinner and thinner.'
    guide 'No one has seen grass in ages.'
    guide 'I miss the feel of it. I miss the sound of birds. I miss when the sky was blue.'
    guide 'It’s a quiet morning, and this world is ending.'
    guide 'And I intend to end with it.'

    guide 'But it’s because I’m going with it that I’m happy.'
    guide 'It’s quiet here. It’s peaceful.'
    guide 'And so long as it stays quiet, so long as I stay unbothered...'
    guide 'So long as my dreams do not come to fruition, and the fate of the world falls out of my hands...'
    guide 'The suffering will end.'
    guide 'This is a good place to be in preparation for the end of the world.'

    ## A shot of the PROTAGONIST -- mostly just a robed figure -- hunched over a small stove, next to a flickering electric light.
    scene stove_and_figure
    with dissolve

    guide 'It’s been a long time coming. I was never meant to last this long, but even so, no one expected things to fall apart so quickly.'
    guide 'At first, I’d hoped someone would brandish their steel and take my head quickly; this all was something I never wanted to see.'
    guide 'But as time went on, and the heroes I expected to mentor never came, I realized... I want to remain.'
    guide 'I want to be the last one left when the stars all go out and the sun dims, even if it means being alone. Even if it means agony. If it means insanity.'
    guide 'Going out with the rest of the world is the only option left.'
    guide 'I hope the sun will be warm.'

    ## Return to CABIN INTERIOR
    scene fnc_cabing1_day1
    with dissolve
    guide '... Let’s see. Breakfast is made. The windows are open. The morning laundry is drying. Next, I --'
    
    ## There’s a KNOCK at the door. The music stops abruptly, replaced with a sinister droning tone.    
    play sound door_knock volume 1.0
    stop music fadeout 0.0
    play music bgm_drone fadein 2.0

    guide '... Was... that... Did I hear..?'
    guide 'No. Certainly not. Just a stray rock. Or two.'
    guide 'No one knows I live here. The nearest settlement is miles away.'

    ## The KNOCK returns.
    play sound door_knock volume 1.5

    guide '... It {i}can’t{/i} be...'

    ## The PROTAGONIST stands and peers out through a crack in the door. In the prototype this can be the same shot as the shot of the heroes in the DREAM INTRO.
    scene backdrop_white
    show gavin at linedup_center_pos1
    show lance at linedup_center_pos2
    show morgan at linedup_center_pos3
    show overlay_window

    guide '... No... {i}No{/i}...'

    ## The shot returns to CABIN INTERIOR, shaking to symbolize the PROTAGONIST stumbling backwards.
    scene fnc_cabing1_day1
    with screen_shake_mid

    guide 'Now? {i}Now?{/i} After all this time?'
    guide 'All these years?'
    guide 'What kind of joke is this? Go away! No one is here! Your source was wrong! There’s no one here who can teach you anything!'
    guide 'Just... go home, live out what remains of your lives happily!'
    
    ## One of the children calls through the door.
    gavin '"Hello? Is anyone home?"'
    lance '"He could be out hunting while it\'s cool..."'
    morgan '"Hunting? Hunting {i}what{/i}? Mice?"'

    ## (NOTE: This choice doesn’t matter. “Stay quiet” is just additional dialogue before going into the “Answer the door” choice.)
    menu day1_choice1:
        'Stay quiet':
            jump stay_quiet
        'Answer the door':
            jump answer_door

    label stay_quiet:
        guide 'I can’t answer them.'
        guide 'I can’t subject them to their fate.'
        guide 'This ends {i}now{/i}. This horrid cycle ends {i}here{/i}.'
        guide 'I’ll wait for them to leave, then I’ll have to move out. Go elsewhere. Far, far away where they won’t follow me.'
        guide 'It’s for their own good. For everyone’s.'
        guide '...'
        guide '...'

        ## There are FOOTSTEPS as it sounds like the children walk away.
        play sound footsteps

        guide '...'
        guide '... Thank the gods. Now I just need to --'

        ## Cut to shot of one of the children looking through the window with a big smile. A loud sound effect plays and the screen shakes a little, but this isn’t necessarily a jumpscare.
        scene backdrop_white
        show gavin happy at Position(xpos=0.2, ypos=0.0):
            zoom 3.0
        show overlay_window with screen_shake_mid
        
        guide 'GODS DAMN IT.'
        guide 'DOESN’T THIS LITTLE TWERP KNOW BETTER THAN TO SNOOP IN PEOPLE’S WINDOWS?!'
        guide '...'
        guide '... Damn it.'
        guide 'There’s no getting out of this one now.'
        guide 'Unless...'

        menu day1_choice2:
            'Lie to the heroes':
                jump lie_to_heroes
            'Answer the door':
                jump answer_door
        
    label lie_to_heroes:
        ## The edges of the screen flash red. There’s a grunt of pain.
        show overlay_pain with screen_shake_mid
        hide overlay_pain
        
        guide_dark 'You can’t.'
        guide 'D-Damn it. It’s already starting.'
        guide 'But if they meet me --'
        
        ## The screen flashes red again, more powerful this time.
        show overlay_pain with screen_shake_strong
        hide overlay_pain

        guide_dark 'You can’t.'
        guide_dark 'Your sacred duty is to --'

        guide 'Oh for the love of -- {i}shut up{/i}.'
        guide '... This is it, then.'
        stop music fadeout 1.0
        
    label answer_door:
        ## A shot of the PROTAGONIST in front of the closed door, then, with the door open. Three HEROES stand on the front porch, all children hardly older than ten or twelve. HERO 1 is a boy with dark skin, curly dark-brown hair and a red cloak draped over one shoulder. There’s a sword at his hip, rusted along one side but otherwise in fairly decent condition. HERO 2 is a boy with light skin, dark-blonde hair tied back in a bun, and a book strapped to his hip like a weapon. HERO 3 is a girl with pale skin, black hair, and sunken eyes. She looks somehow drained of life, husk-like, and leans heavily on a metal pole used as a staff.

        scene cabin_door_closed
        pause 0.5
        play sound door_opening
        pause 1.0
        scene backdrop_grass_sky
        show lance happy at Position(xpos=0.5, ypos=0.55):
            zoom 0.5
        show morgan happy at Position(xpos=0.6, ypos=0.55):
            zoom 0.5
        show gavin happy at Position(xpos=0.35, ypos=0.4):
            zoom 1.0
        show cabin_door_open
        
        gavin '“It’s you! You’re --”'

        guide 'The man from your dream. I know.'
        gavin '“The man from my dream!”'

        guide 'I just said that.'
        gavin '“...”'

        guide '...'
        gavin '“...”'

        guide '...'
        lance '“... Does he... talk?”'

        guide 'Oh. Shit.'
        guide '“I -- ahem. I speak.”'
        gavin '“Oh, great! Uh --”'
        
        play sound throat_clear
        pause 1.0

        gavin '“‘Oh great and mighty hermit of times ancient, we are the Chosen Three, as ordained by the last vestiges of the Roots of the World.’”'
        $ lance_name = 'Lance'
        lance '“‘I am [lance_name], arcanist and sworn defender of the Chosen.’”'
        $ morgan_name = 'Morgan'
        morgan '“I’m [morgan_name]. I keep them safe. And alive.”'
        show lance angry
        lance '(angrily whispering)\n“([morgan_name], that’s not your line!)”'

        $ gavin_name = 'Gavin'
        gavin '“‘And I am [gavin_name], leader of the Chosen Three --’”'

        lance '(whispering)\n“(We said we weren’t going to have a leader?)”'

        gavin '“‘-- and banisher of the Hidden Darkness.’”'
        gavin '“‘We seek your greatest arts of swordsmanship, magic, and healing, in the pursuit of reclaiming this world from death.’”'
        gavin '“‘It is our sacred destiny.’”'
        gavin '“‘We are chosen. We are the heroes of destiny. We are the heroes who will save the world.’”'
        gavin '“‘We are the heroes who will banish the evil that plagues the planet, and live to --’”'
        guide '“Good hell, I thought that spiel couldn’t get any worse.”'

        ## All three HEROES are shocked by the callous interruption.
        show gavin surprised at sprite_shake_light
        show lance surprised at sprite_shake_light
        show morgan surprised at sprite_shake_light

        guide '“Yeah, yeah, I know why you kids are here.”'
        gavin '“You... do?”'
        gavin '“Er, of course you do! After all, you’re so wise and --”'
        guide '“Let me go get my rod so I can kick your ass.”'
        gavin '(shocked, as are the others)\n“You -- WHAT?”'

        play sound door_slam
        scene cabin_door_closed
        pause 1.0
        scene fnc_cabing1_day1

        guide 'Well, this is it.'
        guide 'The beginning of the next, when it should have been the beginning of the end.'
        guide '... It wasn’t supposed to be this way.'
        guide '... I better make sure they’re ready. Which they aren’t. But at least I should get a good idea of their standing in combat.'
        guide 'Now, where’d I leave that stupid weapon...'

    ## FADE OUT to black
    scene backdrop_black
    with fade

    ## END SCENE
    return

label day1_combat_intro:
    ## FADE IN to BACK OF CABIN. Combat has not been initiated yet. The HEROES all stand in a line in front of the HERMIT
    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3

    guide 'I haven’t brought out my combat equipment in a long, long time. Whoever owned this place last was also a fighter, though. I never {i}did{/i} clean up their training dummies.'
    guide 'It’ll be useful for the kids in the long run, but ultimately, they’re fighting {i}me{/i}.'

    lance '“Sir? What is this all for?”'
    guide '“Don’t call me sir.”'
    lance '(annoyed)\n“... Dude?”'
    guide_dark '{i}Master.{/i}'
    guide '“Teacher. Wait -- Guide.”'
    $ guide_name = 'The Guide'
    $ guide_dark_name = 'The Guide (?)'
    lance '“‘Guide?’”'
    lance '“Well... {i}Guide{/i}... what exactly is happening here?”'
    guide '“What does it look like is happening?”'
    lance '(in a know-it-all tone)\n“It {i}appears{/i} that you are preparing a training ground, in service of our education to banish the Hidden Darkness, but it’s rudimentary at best and insulting at worst.”'
    lance '“You have yet to ask about our experience in the slightest, and I can assure you we are more than capable to move on past basics into --”'
    guide '“Nope.”'
    lance '“‘{i}Nope{/i}!?’”'
    guide '“Nope. You’re getting tested, whether you like it or not. Now, here’s what’s going to happen.”'
    guide '“The three of you are going to fight {i}me{/i}. You’re going to use the full extent of your abilities and power, and I’ll have to counter that.”'
    gavin '(concerned)\n“Guide... we could seriously hurt you. If we take you down --”'
    guide '“That won’t be happening.”'
    morgan '“You’re just one guy.”'
    guide '“One guy who’s about to kick your asses.”'
    guide '“... Butts. You’re children. I keep forgetting.”'
    guide '“Draw your weapons, or prepare your spells, or... whatever it is you kids do.”'
    gavin '“If you’re sure, Guide...”'
    lance '“What a waste of time...”'

    ## FADE OUT to black
    scene backdrop_black
    with fade

    ## END SCENE
    return

label day1_combat:
    ## BEGIN COMBAT.
    # call combat guide_player
    return

label day1_post_combat:
    ## AFTER COMBAT, the HEROES are all licking their wounds and complaining.
    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3
    
    gavin '“Man, you really didn’t hold back, huh?”'

    guide '“Did you expect me to?”'

    guide_dark 'Pathetic. They aren’t ready. They’re not strong enough. They’re wasting precious time. As usual, it falls to us to handle the responsibilities of the cycle.'

    guide '“The Hidden Darkness will not offer you such quarter.”'
    guide '“You wish to save this world? You wish to save humanity, and life itself?”'
    guide '“You know nothing about the gravity of the task you seek to undertake. You think your status as ‘Chosen’ grants you immunity from failure.”'
    guide '“Your assumptions could not be further from the truth.”'
    guide '“I did not hold back, but if you think defeating me will mean you are ready to fell the Hidden Darkness, you’re all more foolish and ignorant than I thought.”'

    ## The HEROES all look dejected.
    show gavin sad
    show lance sad
    show morgan sad

    lance '“You’re rejecting us, then. You’re not even giving us a chance.”'

    guide '“I am not rejecting you.”'
    guide '“I am saying, we are going to have a lot of work on our hands.”'
    guide '“Get up. Clean yourselves up. Unpack, make yourselves comfortable. Your fate is as intertwined with mine as the Roots of the World are entangled with life and death.”'
    guide '“I can’t turn you away. It’s literally impossible for me to.”'

    lance '“You tried to pretend you weren’t home.”'

    guide '“For good reason.”'

    guide 'They’ll find out, in time. They should have stayed home.'

    guide '“Go.”'

    ## The HEROES depart, one by one, leaving the GUIDE alone outside.
    hide morgan with easeoutleft
    pause 0.5
    hide lance with easeoutleft
    pause 1.0
    hide gavin with easeoutleft
    pause 0.5

    guide_dark 'I’ve waited far too long for this. We won’t go easy on them.'

    guide 'I never planned to. But not for your sake.'

    guide_dark 'It will all be the same in the end. Coddle them, abuse them -- no matter your course, they will grow, and the cycle will repeat as it has always been meant to.'
    guide_dark 'Change is impossible. All ages of man, age the same. All generations grow from the bones of the last.'
    guide_dark 'Thus, always.'

    guide '...'

    ## FADE OUT to black
    scene backdrop_black
    with fade

    ## END SCENE
    return
