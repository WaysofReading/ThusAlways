label day1_backstory_cutscene:
    
    scene fnc_cabing1_day1
    with dissolve
    
    guide 'The year is 4279. It\'s one of the only things I keep track of anymore.'
    guide 'Days, weeks, months, all are mostly irrelevant. News is meaningless when there will be no record of it kept. Faces seen and names spoken will not last more than another year or two.'
    guide 'Last year, the ocean sank another seven meters, and four more mountains collapsed in on themselves, taking their villages with them.'
    guide 'Trees continue to grow thinner and thinner.'
    guide 'No one has seen grass in ages.'
    guide 'It\'s a quiet morning, and this world is ending.'

    scene burnt_food
    with dissolve

    guide 'The vegetables in my garden barely make it to maturity these days.'
    guide 'Game is more plentiful, but the animals are starting to die out, too. Their foraging can only take them so far.'
    guide 'But breakfast today is a feast fit for a king.'

    scene fnc_cabing1_day1
    with dissolve

    guide 'I\'ve lived in this house for several years now. I\'ve been lucky.'
    guide 'Rare is the structure that has lasted more than a decade. Whoever lived here before took very good care of it.'
    guide 'Its close proximity to a surviving town isn\'t quite ideal, but it\'s certainly not the end of the world.'
    guide '... That\'s already happening.'
    guide 'But I\'m happy.'
    guide 'It\'s quiet here. It\'s peaceful.'
    guide 'The town is fortified on all sides by hills and mountains that haven\'t yet collapsed. Creatures take refuge from harsh sandy winds.'
    guide 'There\'s even a stream. Imagine that! A stream of water...'
    guide 'This is a good place to be in preparation for the end of the world.'

    scene stove_and_figure
    with dissolve

    guide 'It\'s been a long time coming. I was never meant to last this long, but even so, no one expected things to fall apart so quickly.'
    guide 'When it all started coming down, I\'d hoped someone would find me quickly. I\'d hoped someone would brandish their steel and take my head quickly; this all was something I never wanted to see.'
    guide 'But no one came for me.'
    guide 'No one has come.'
    guide 'At this rate, no one {i}is{/i} coming. They would have come by now.'
    guide 'Going out with the rest of the world is the only option left.'
    guide 'I hope the sun will be warm.'

    scene fnc_cabing1_day1
    with dissolve
    guide '... Let\'s see. Breakfast is made. The windows are open. The morning laundry is drying. Next, I--'
    
    play sound door_knock volume 1.0
    stop music fadeout 0.0
    pause 2.0
    play music bgm_drone fadein 0.0 volume 2.0

    guide '... Was... that... Did I hear..?'
    guide 'No. Certainly not. Just a stray rock. Or two.'

    play sound door_knock volume 1.5

    scene backdrop_white
    show gavin at linedup_center_pos1
    show lance at linedup_center_pos2
    show morgan at linedup_center_pos3
    show overlay_window

    guide '... No... {i}No{/i}...'

    scene fnc_cabing1_day1
    with screen_shake_mid

    guide 'Now? {i}Now?{/i} After all this time?'
    guide 'After all these years?'
    guide 'What kind of joke is this? Go away! No one is here! Your source was wrong!'
    guide 'Just... go home, live out the rest of your life happily!'
    guide 'Don\'t... don\'t let this...'
    
    gavin '"Hello? Is anyone home?"'
    lance '"He could be out hunting while it\'s cool..."'
    morgan '"Hunting? Hunting {i}what{/i}? Mice?"'

    menu:
        'Stay quiet':
            jump stay_quiet
        'Answer the door':
            jump answer_door

    label stay_quiet:
        guide 'I can\'t answer them.'
        guide 'I can\'t subject them to their fate.'
        guide 'This ends {i}now{/i}.'
        guide 'I\'ll wait for them to leave, then I\'ll have to move out. Go elsewhere. Far, far away where they won\'t follow me.'
        guide '...'
        guide '...'

        play sound footsteps

        guide '...'
        guide '... Thank the gods. Now I just need to --'

        scene backdrop_white
        show gavin happy at Position(xpos=0.2, ypos=0.0):
            zoom 3.0
        show overlay_window with screen_shake_mid
        
        guide 'GODS DAMN IT.'
        guide 'DOESN\'T THIS LITTLE TWERP KNOW BETTER THAN TO SNOOP IN PEOPLE\'S WINDOWS?!'
        guide '...'
        guide '... Damn it.'
        guide 'There\'s no getting out of this one now.'
        guide 'Unless...'

        menu:
            'Lie to the heroes':
                jump lie_to_heroes
            'Answer the door':
                jump answer_door
        
        
    label lie_to_heroes:
        show overlay_pain with screen_shake_mid
        hide overlay_pain
        
        guide '{b}You can\'t.{/b}'
        guide 'D-Damn it.'
        guide 'But if they meet me --'

        show overlay_pain with screen_shake_strong
        hide overlay_pain

        guide '{b}You can\'t.{/b}'
        guide '{b}Your sacred duty is to --{/b}'

        guide 'Oh for the love of -- {i}shut up{/i}.'
        guide '... This is it, then.'
        
    label answer_door:
        scene cabin_door_closed
        show guide at right
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
        show guide at right
        
        gavin '"It\'s you! You\'re --"'
        guide 'The man from your dream. I know.'
        gavin '"The man from my dream!"'
        guide 'I just said that.'
        gavin '"..."'
        guide '...'
        gavin '"..."'
        guide '...'
        lance '"... Does he... talk?"'
        guide 'Oh. Shit.'
        guide '"I -- ahem. I speak."'
        gavin '"Oh, great! Uh --"'
        
        play sound throat_clear
        pause 1.0

        gavin '"\'Oh great and mighty guide of times ancient, we are the Chosen Three, as ordained by the last vestiges of the Roots of the World.\'"'
        $ lance_name = 'Lance'
        lance '"\'I am [lance_name], arcanist and sworn defender of the Chosen.\'"'
        $ morgan_name = 'Morgan'
        morgan '"\'I\'m [morgan_name]. I keep them safe. And alive.\'"'
        
        show lance angry
        lance '{i}(angrily whispering){/i}\n([morgan_name], that\'s not your line!)'
        $ gavin_name = 'Gavin'
        gavin '"And I am [gavin_name], leader of the Chosen Three --"'
        lance '"{i}(whispering){/i}\n(We said we weren\'t going to have a leader?)"'
        gavin '"-- and banisher of the Hidden Darkness."'
        gavin '"We seek your greatest arts of swordsmanship, magic, and healing, in the pursuit of reclaiming this world from death."'
        gavin '"It is our sacred destiny."'
        gavin '"We are chosen. We are the heroes of destiny. We are the heroes who will save the world."'
        gavin '"We are the heroes who will banish the evil that plagues the planet, and live to --"'
        guide '"Good hell, I thought that spiel couldn\'t get any worse."'

        # Make sprites shake slightly?
        show gavin surprised at sprite_shake_light
        show lance surprised at sprite_shake_light
        show morgan surprised at sprite_shake_light

        guide '"Yeah, yeah, I know why you kids are here."'
        gavin '"You... do?"'
        gavin '"Er, of course you do! After all, you\'re so wise and --"'
        guide '"Let me go get my rod so I can kick your ass."'
        gavin '"You -- WHAT?"'

        play sound door_slam
        scene cabin_door_closed
        show guide at right
        pause 1.0
        scene fnc_cabing1_day1

        guide 'Well, this is it.'
        guide 'The beginning of the next.'
        guide '... It wasn\'t supposed to be this way.'
        guide '... I better make sure they\'re ready. Which they aren\'t. But at least I should get a good idea of their standing in combat.'
        guide '... Now, where\'d I leave that stupid thing...'

    return

label day1_combat_intro:
    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3
    show guide at right

    guide 'I haven’t brought out my combat equipment in a long, long time. Whoever owned this place last was also a fighter, though. I never did clean up their training dummies.'
    guide 'It’ll be useful for the kids in the long run, but ultimately, they’re fighting {i}me{/i}.'

    lance '“Sir? What is this all for?”'
    guide '“Don’t call me sir.”'
    lance '(annoyed)\n“... Dude?”'
    guide '{i}{b}Master.{/b}{/i}'
    guide '“Teacher. Wait -- Guide.”'
    $ guide_name = 'The Guide'
    lance '“\'Guide?\'”'
    lance '“Well... Guide... what exactly is happening here?”'
    guide '“What does it look like is happening?”'
    lance '(in a know-it-all tone)\n“It appears that you are preparing a training ground, in service of our education to banish the Hidden Darkness, but it’s rudimentary at best and insulting at worst.”'
    lance '“You have yet to ask about our experience in the slightest, and I can assure you we are more than capable to move on past basics into–”'
    guide '“Nope. You’re getting tested, whether you like it or not. Now, here’s what’s going to happen.”'
    guide '“The three of you are going to fight me. You’re going to use the full extent of your abilities and power, and I’ll have to counter that.”'
    gavin '(concerned)\n“Guide… we could seriously hurt you. If we take you down–”'
    guide '“That won’t be happening.”'
    morgan '“You’re just one guy.”'
    guide '“One guy who’s about to kick your asses.”'
    guide '“... Butts. You’re children. I keep forgetting.”'
    guide '“Draw your weapons, or prepare your spells, or… whatever it is you kids do.”'
    gavin '“If you’re sure, Guide...”'
    lance '“What a waste of time...”'

    return

label day1_combat:
    # Call to combat engine
    pass
    return

label day1_post_combat:
    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3
    show guide at right
    
    gavin '“Man, you really didn’t hold back, huh?”'

    guide '“Did you expect me to?”'

    guide '{b}Pathetic. They aren’t ready. They’re not strong enough. They’re wasting precious time. As usual, it falls to us to handle the responsibilities of the cycle.{/b}'

    guide '“The Hidden Darkness will not offer you such quarter.”'
    guide '“You wish to save this world? You wish to save humanity, and life itself?”'
    guide '“You know nothing about the gravity of the task you seek to undertake. You think your status as ‘Chosen’ grants you immunity from failure.”'
    guide '“Your assumptions could not be further from the truth.”'
    guide '“I did not hold back, but if you think defeating me will mean you are ready to fell the Hidden Darkness, you’re all more foolish and ignorant than I thought.”'

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

    hide morgan with easeoutleft
    pause 0.5
    hide lance with easeoutleft
    pause 1.0
    hide gavin with easeoutleft
    pause 0.5

    guide '{b}I’ve waited far too long for this. We won’t go easy on them.{/b}'

    guide 'I never planned to. But not for your sake.'

    guide '{b}It will all be the same in the end. Coddle them, abuse them– no matter your course, they will grow, and the cycle will repeat as it has always been meant to.{/b}'
    guide '{b}Change is impossible. All ages of man, age the same. All generations grow from the bones of the last.{/b}'
    guide '{b}Thus, always.{/b}'

    guide '...'