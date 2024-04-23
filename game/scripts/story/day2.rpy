label day2_morning:
    "DAY 2 - MORNING"
    call hero_paths_choice
    return

label day2_combat:
    ## FADE IN to BACK OF CABIN again. OFF SCREEN the GUIDE is setting up training dummies.
    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3

    guide 'Alright, it’s time to put these dummies to use. We’ll start slow and work our way up to more complex tactics and maneuvers.'
    guide 'Or, maybe they’ll get insulted and bored, and leave.'
    guide 'Hopefully, I can make them last, so long as these kids aren’t --'

    lance '“See, this? This is just insulting.”'

    guide ' -- rough on them.'

    guide '“You failed your task yesterday, which was basic. So, we’re going back to the basics.”'

    lance '“You said you were testing us, not that we were supposed to win. I doubt you planned on that outcome anyway.”'
    lance '“Besides, I hardly expect us to learn anything if our opponents are nothing more than inanimate sacks of straw and sand.”'

    gavin '“And bucket helmets.”'

    lance '“Yes, and bucket helmets. Astutely observed, Gavin.”'

    guide 'Where did this kid learn to talk? A dictionary? Where would he even find a book of that size?'
    guide 'Annoying as it is, at least he talks enough for himself and the girl.'
    guide 'Come to think of it... I think I’ve hardly heard her speak ten words.'

    guide '“Girl.”'

    show morgan at sprite_shake_light

    guide '“Have you no input?”'

    morgan '“...”'

    guide 'I can see in her eyes this world has not been kind to her.'

    guide_dark 'It will not get any kinder. It is not our job to make it nice and cushiony for her.'

    guide '“If you are to speak to anyone, at least speak with your partners.”'
    guide '“If your mission is to ‘keep them alive,’ you will have to communicate with them.”'

    show gavin angry

    gavin '“She’s fine. Morgan doesn’t have to use her words to communicate with us.”'
    gavin '“She talks when she needs to, and she can hear us fine.”'

    guide_dark 'Defiant and ignorant. She will need to adjust to the common conventions of teamwork if she is to achieve anything.'

    guide 'We can deal with that later. For now, they just need to be able to fight without going down.'

    guide_dark 'Survival? Survival is not sufficient. They must conform --'

    guide '“Show me your techniques, all of you.”'

    ## BEGIN COMBAT with Training Dummy

    # call combat_training_dummy

    ## AFTER COMBAT, the HEROES are bored and unimpressed.

    scene fnc_cabinfp_day1 with fade
    show gavin sad at grouped_left_pos1
    show lance angry at grouped_left_pos2
    show morgan at grouped_left_pos3
    
    lance '“Is this supposed to be a joke to you?!”'

    gavin '“Lance --”'

    lance '“You strike us down without any hesitation, and now you have us playing with dolls!”'
    lance '“I demand to be taken seriously! How are we supposed to save the world if you just have us playing pretend in the wastes?!”'
    lance '“We’re Chosen heroes! We’re not babies! Why are you two going along with this?!”'

    morgan '“Lance, if we jump too hastily into more advanced fights than we’re ready for, we might get hurt!”'

    guide_dark 'I like the tall one. The others would do well to learn from him.'

    guide 'He’s brash and arrogant. He’s going to get them in trouble. It’s like he forgot all about yesterday’s loss.'

    guide_dark 'He wants to grow. He wants to become powerful. We need that.'

    guide '“...”'
    guide '“You want more of a fight? Fine.”'

    guide 'It’s been a while since I cast this spell...'
    guide 'Spells were more Gwen’s thing. We’ll see if I remember...'

    ## BEGIN COMBAT with Training Dummy (Enhanced)

    # call combat_training_dummy_enhanced

    ## AFTER COMBAT, LANCE is far more satisfied.

    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3

    lance '“Better. We actually used our skills a bit.”'

    show gavin happy
    gavin '“I guess that was pretty fun, actually.”'
    show gavin
    gavin '“But Guide, why didn’t you do that before?”'

    guide '“I hoped you’d give up and leave.”'
    guide '“Your friend’s conviction is very... persuasive.”'

    show lance happy at sprite_bounce_light

    lance '“Almost like I was leading by example.”'

    guide 'Oh, brother.'

    guide_dark 'He shows the most promise of any of them. He is a leader, by my standards.'
    guide_dark 'As far as I’m concerned, their success lies squarely with him, for the time being.'
    guide_dark 'Maybe he’s the one who will renew the cycle.'

    guide 'Gods, why didn’t they just leave?'

    guide '“Enough. You’ve succeeded in proving to me you’re more capable in combat than I thought.”'
    guide '“But there will be more to your success than your ability to tear enemies apart.”'
    guide '“We’ll continue tomorrow. Rest for a moment, then you all will help me in the garden and we’ll look for game for dinner.”'

    gavin '“You have a garden? Oh, cool! Can I see it now? Can you tell me how you take care of it? Where did you find the seeds?”'

    guide '“I --”'

    gavin '“How long have you had it? How did you fertilize the soil? One time, I saw a garden that was fertilized with --”'

    guide '“Hush, boy.”'

    ## GAVIN and the others are surprised by the GUIDE’s tone. It’s harsher than they’re used to.'
    guide '“... Come to the garden and I’ll tell you.”'

    ## GAVIN goes off screen.
    hide gavin with easeoutleft
    hide guide with easeoutright

    ## FADE OUT to black
    scene backdrop_black with dissolve

    ## END SCENE
    return

label day2_dinner:
    ## No FADE IN yet. Just a black screen as the GUIDE gives some exposition.
    scene backdrop_black

    guide 'Gavin was surprisingly knowledgeable about gardening and agriculture. I suppose I should expect the children left in this world to know more about survival than those I’ve known in the past.'
    guide 'But the extent of his knowledge speaks to a need greater than a boy his age would have need of with the right support.'
    guide 'And Morgan, being quiet as a mouse, is quite the little hunter. I thought something was wrong when she came and urgently tugged on my sleeve, until she showed me the rope trap and the coyote dangling from it.'
    guide 'Even though Lance didn’t help much, it was surprisingly refreshing to see something he’s lacking in.'
    guide 'Though it does beg the question how he survived for as long as he has.'

    ## FADE IN to CABIN INTERIOR. For the sake of time, for now this is just the three HEROES directly in front of the screen side by side.
    scene fnc_cabing1_day1 with fade
    show gavin at linedup_center_pos1
    show lance at linedup_center_pos2
    show morgan at linedup_center_pos3

    gavin '“... And we didn’t even have to mix in clay or shredded bark for substance!”'

    guide '“I thought that practice died years ago.”'

    lance '“It did, but it got picked back up with the decrease in animal population.”'

    guide 'A harrowing thought. Though the implication that they haven’t resorted to cannibalism yet is promising.'
    guide 'However, I know little else about them, these children in my home. I know it’s common courtesy to make polite conversation; I haven’t forgotten my manners.'
    guide 'But knowing what’s to come, it feels pointless to ask.'
    guide '... Then again, it would be better than this awkward silence.'

    guide '“... Was it the process of being Chosen that brought you together?”'

    gavin '“Well, that’s how we met Lance. Morgan and I traveled together before that.”'
    gavin '“I’ve sort of shuffled around from group to group for almost as long as I can remember. I think I was eight when I met Morgan, and we’ve stuck together ever since.”'
    gavin '“It’s been nice to have a friend with me!”'

    show morgan happy
    guide '“Where did you come from then, Lance?”'

    lance '“My family lives just outside the other end of the valley.”'
    lance '“They pushed me to seek out more arcane power at the Roots of the World. Gavin and Morgan showed up at the same time I did.”'

    guide '“And why did Gavin and Morgan go?”'

    morgan '“... I had a dream about it.”'

    guide '“Of course.”'
    guide '“And your origin?”'

    ## MORGAN is clearly uncomfortable.
    show morgan uncomfortable

    morgan '“...”'

    gavin '“She... doesn’t like to talk about the time before she was with me.”'

    guide_dark 'Not that it matters. None of their little stories matter.'
    guide_dark 'What matters is what they will become.'

    guide 'We can’t properly direct them if we don’t know to some extent where they’ve come from or who they are.'

    guide '“I presume you all have faced great loss in some form in your lives.”'
    guide '“It would be rather shocking if you haven’t.”'

    lance '“You want our sob stories now?”'

    guide '“I want to know if you know what to expect with this duty you pursue.”'

    ## The three HEROES just look among themselves quietly.
    show morgan
    show lance
    show gavin

    guide_dark 'They’re clueless. Ignorant. Good. We can embellish a little.'
    guide 'We already do them disservice enough by nature of trapping them in the cycle. I will not deceive them as to the gravity of what they will accomplish.'
    guide_dark 'If that is your choice, it is better to tell them nothing at all. Let them live their little lie of saving the world.'

    menu:
        'You won’t understand':
            jump day2_dinner_wont_understand
        'Tell them':
            jump day2_dinner_tell_them

    label day2_dinner_wont_understand:
        guide '“The finer details don’t matter, I suppose. It may be too complex for you to fully comprehend.”'

        gavin '“This is our sacred mission! We know we have to fight the Hidden Darkness... uh, and I guess the ‘hidden’ part means we have to find it.”'
        gavin '“Which I figured you’d help us with when we’re ready.”'
        gavin '“But we don’t know how to find it, or how to fight it.”'
        gavin '“If we’re Chosen, there must be something special about us that no one else has, otherwise, someone else would have found and destroyed it by now, right?”'

        guide '“Not an incorrect assumption. But it’s more complex than that.”'

        lance '“Then tell us. We need to be as prepared as possible to win that fight when it happens.”'
        lance '“You won’t know if we won’t understand unless you try to tell us.”'

        guide 'You could let me out to tell them. I’ll tell them just enough.'

        guide 'No. Get out of my throat.'

    label day2_dinner_tell_them:
        guide '“Very well, then.”'
        guide '“The Hidden Darkness is indeed a malevolent force you must find, but its origin may be closer to that which you understand than you might hope.”'
        guide '“It started with one person. Just one.”'
        guide '“It wasn’t born out of malice, or hate. It wasn’t created intentionally, but it didn’t come from nothing, either. The Hidden Darkness is a monster, yes, but it was a monster no one wished upon anyone.”'
        guide '“The Hidden Darkness was born from sorrow, distrust, and a loss of faith and hope.”'
        guide '“The Hidden Darkness was born as a response to the moral corruption of the world, and the people in it. When the corruption became too great, and the forces of good became too scattered and weak to oppose it, that is what birthed the Darkness.”'
        guide '“When leaders failed their people beyond retribution, when nature teetered too far to one side of extinction, and when love and trust became commodities rather than gifts...”'
        guide '“The combination of those failures were the catalyst for a heartbreak too great to mend. And thus, that was the catalyst that brought life to the Darkness, and in the shadows it began to spread.”'
        guide '“Not only did it feed off of the negative energy that pervaded the world, it empowered it. The feedback loop enabled the Darkness to spread like a disease -- and it presented itself as such.”'
        guide '“Whatever it touched, it infected, or killed outright. And those that it infected, it changed.”'
        guide '“No doubt you have seen it.”'

        lance '“The Corrupted.”'

        guide '“Yes.”'
        guide '“Tell me what you know about them.”'

        lance '“The Corrupted --”'

        morgan '“They’re mutated masses of dangerous energy and necrotic aura.”'
        morgan '“They’re hostile to any and all life -- human, animal, fungi -- all of it.”'
        morgan '“And it would rather die than flee from a fight... because it knows if it can hurt you and get in your blood, even if it’s dead... it can kill you.”'

        guide '“I’m impressed.”'

        gavin '“So if the Corrupted are part of the Hidden Darkness, then destroying the Darkness would destroy all the corrupted, too?”'

        guide '“Of that, I’m not entirely sure. In a sense, I suppose the answer is yes...”'

        gavin '“Then how do we find it? How do we defeat it? The sooner we can do that, the sooner we can save everyone!”'

        guide 'Were it so simple...'

        guide 'They will fight it. It is their destiny.'

        guide '“There will come a day when you will look upon someone, something, or even just a shadow in a corner... and you will know.”'
        guide '“One day, all it will take is a glance, and you will see it.”'
        guide '“It’s the ‘Hidden Darkness’ for a reason, after all.”'
        guide '“As for its defeat...”'
        guide '“... I don’t know.”'

        lance '“You don’t know?”'
        lance '“Well, if the Roots didn’t know, I guess you wouldn’t.”'

        guide '“It’s getting late. If you’re all finished with dinner, you should rest.”'
        guide '“But clean your plates first.”'

    ## The HEROES leave.
    hide gavin
    hide lance
    hide morgan
    with easeoutleft
    
    guide_dark 'Those poor children...'
    guide_dark 'They’ll be in for quite the shock when their eyes finally open.'
    guide_dark 'I remember when you saw it for the first time --'

    guide 'I have no intention of thinking about that right now.'
    guide 'My only intention is to sleep.'

    ## FADE OUT
    scene backdrop_black with dissolve

    ## END SCENE
    return

label day2_dream:
    ## FADE IN to misty background.
    scene backdrop_mist
    with fade
    
    ## RADIO sound effect (with unintelligible dialogue) in the background.
    play music bgm_radio_chatter

    radio '“... The promised aid to the west has been postponed for another month due to shortages in both food and fuel across the coast. Reports state that if help does not arrive in time, another few thousand lives will be lost.”'
    radio '“In other news, the epidemic in the chain islands has reached its all-time peak, with the number of infected totaling over half of its population...”'

    mother '“Please, turn that thing off. I won’t want to hear about it.”'

    guide '“Sorry, Mom.”'

    ## The RADIO sound effect ends. GWEN, friend to the GUIDE, is with him, wherever he currently is.
    stop music fadeout 2.0

    gwen '“I mean, we could go listen to it elsewhere?”'

    mother '“I don’t want you kids worrying about that kind of stuff. Let that be our job. Your job is to focus on your schoolwork, play outside when the sun shines, and go to bed at a reasonable hour.”'

    guide 'Even then, I knew the reason the world was in such a state was because the leaders of our world hadn’t been concerned about what mattered to begin with.'
    guide 'And I knew that my mother knew.'
    guide 'What she didn’t know, was that I knew. That I wasn’t a fool. That Gwen wasn’t a fool.'
    guide 'We all knew something was wrong before things got worse.'

    gwen '“Ma’am, you say that as if going to bed at a reasonable hour has ever been a reasonable request.”'
    gwen '“These essays don’t type themselves.”'

    guide '“Gwen, you can hardly type the word ‘the’ without looking down at the keyboard. Doesn’t your mom still help you?”'

    gwen '“Oh, shut up.”'

    mother '“Gwen, we don’t use that language in this house.”'

    gwen '“Sorry, ma’am.”'

    guide_dark 'Mother always was precious like that.'

    guide 'I don’t need your sarcasm. It’s bad enough you decided to wake up the moment those kids were on my doorstep.'

    guide_dark 'Don’t lie to yourself. You know I was awake long before that.'

    guide '“We could go to the park across the street or something.”'

    mother '“If you’re going to the park, ask Lucas next door if he can go too.”'

    guide '“Lucas? Lucas is always sick, Mom.”'

    mother '“That doesn’t mean you shouldn’t ask.”'
    mother '“Besides, I know you kids go over there to just sit on the grass anyways. That’s not out of Lucas’ capabilities.”'

    guide 'She didn’t know Lucas hadn’t been out of the house in three weeks.'
    guide 'The air quality was just too hard on his lungs.'

    guide_dark 'It’s amazing, then, what the bombs dropping did for his body, isn’t it? All it took was a little war to get him running.'

    guide 'He barely made it from one day to the next! If his family had been able to afford his medical treatments in the first place, he --!'
    guide '...'
    guide 'I am not humoring you.'

    guide_dark 'I don’t need you to.'
    guide_dark 'You and I both know well the start of the end of the world was the greatest medicine Lucas ever received.'
    guide_dark 'So much of it was all in his head...'
    guide_dark 'When all the king’s horses and all the king’s men couldn’t put Humpty together again, and then the king and his men vanished one by one and the world became free...'
    guide_dark 'You remember how nice the air was then, don’t you?'

    guide 'People died. Hundreds of thousands -- millions.'
    guide 'The death of corrupt officials and governments could never justify that level of loss.'
    guide 'What was left behind for the next generations?'
    guide 'Nothing.'

    guide_dark '{i}Opportunity.{/i}'

    guide 'Opportunity?!'

    menu day2_dream_choices:
        "It was trauma.":
            jump day2_dream_choices_trauma
        "It was ruins.":
            jump day2_dream_choices_ruins
        "It was the cycle.":
            jump day2_dream_choices_cycle

    label day2_dream_choices_trauma:
        guide 'It was the retraction of everything they’d ever promised us.'
        guide 'Security, safety, a future. Family.'
        guide 'They told us stories of the wars they fought, and the wars their parents fought, and they promised how we’d never go through what they went through.'
        guide 'They told us that’s exactly what they fought for. And maybe that’s what they were told, too.'
        guide 'But that was never what all those wars were for.'
        guide 'It was all... worthless.'
        jump day2_dream_choices_reconvene

    label day2_dream_choices_ruins:
        guide 'Everything they’d built up for us, for themselves, was on fracturing foundations already, but with the end of the world, all of it was torn down overnight.'
        guide 'Nothing was left to rebuild with. There was nothing to take the opportunity of.'
        guide 'There were no institutions to continue or reform, no communities to reunite. All the good there was, was stripped bare and destroyed indiscriminately with the bad. '
        guide 'Even our morals were shattered; what were they worth if they couldn’t keep everything together to begin with?'
        jump day2_dream_choices_reconvene

    label day2_dream_choices_cycle:
        guide 'It was the byproduct of the cycle that has been repeating itself since time immemorial. '
        guide 'A broken promise here, a shifting of the goalposts there.'
        guide 'The delusion of endless growth could only sustain itself until there was nothing left to grow with.'
        guide 'Empires rose, and then when things could settle down, become simple in a life of plenty, a false scarcity was imposed.'
        guide 'And then when the false scarcity became true because they starved themselves to death in their self-imposed emotional celibacy, they fell.'
        guide 'When true scarcity arrived, and there was no one and nothing left to reverse it, it could only mean certain death.'
        jump day2_dream_choices_reconvene

    label day2_dream_choices_reconvene:
        guide 'There was no opportunity in that.'

        guide_dark 'As always, you miss the bigger picture.'
        guide_dark 'Every generation has its growing pains. That’s what makes them stronger than the last, and those that aren’t were never meant to continue regardless.'
        guide_dark 'For Lucas, those growing pains gave him his future. How delusional for you not to see that!'

        guide 'It broke him.'

        guide_dark 'And reformed him into something that could survive.'
        guide_dark 'You don’t think this will end the same way?'

        guide 'To what end?'
        guide '...'

    ## FADE TO BLACK
    scene backdrop_black with dissolve

    guide 'Does it always have to be this way?'

    ## END SCENE
    return