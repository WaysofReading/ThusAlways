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
    guide 'Hopefully, I can make them last, so long as these kids aren’t–'

    lance '“See, this? This is just insulting.”'

    guide '– rough on them.'

    guide '“You failed your task yesterday, which was basic. So, we’re going back to the basics.”'

    lance '“You said you were testing us, not that we were supposed to win. I doubt you planned on that outcome anyway.”'
    lance '“Besides, I hardly expect us to learn anything if our opponents are nothing more than inanimate sacks of straw and sand.”'

    gavin '“And bucket helmets.”'

    lance '“Yes, and bucket helmets. Astutely observed, Gavin.”'

    guide 'Where did this kid learn to talk? A dictionary? Where would he even find a book of that size?'
    guide 'Annoying as it is, at least he talks enough for himself and the girl.'
    guide 'Come to think of it… I think I’ve hardly heard her speak ten words.'

    guide '“Girl.”'

    show morgan at sprite_shake_light

    guide '“Have you no input?”'

    morgan '“...”'

    guide 'I can see in her eyes this world has not been kind to her.'

    guide '{b}It will not get any kinder. It is not our job to make it nice and cushiony for her.{/b}'

    guide '“If you are to speak to anyone, at least speak with your partners.”'
    guide '“If your mission is to ‘keep them alive,’ you will have to communicate with them.”'

    show gavin angry

    gavin '“She’s fine. Morgan doesn’t have to use her words to communicate with us.”'
    gavin '“She talks when she needs to, and she can hear us fine.”'

    guide '{b}Defiant and ignorant. She will need to adjust to the common conventions of teamwork if she is to achieve anything.{/b}'

    guide 'We can deal with that later. For now, they just need to be able to fight without going down.'

    guide '{b}Survival? Survival is not sufficient. They must conform–{/b}'

    guide '“Show me your techniques, all of you.”'

    ## BEGIN COMBAT with Training Dummy
    ## AFTER COMBAT, the HEROES are bored and unimpressed.

    scene fnc_cabinfp_day1 with fade
    show gavin sad at grouped_left_pos1
    show lance angry at grouped_left_pos2
    show morgan at grouped_left_pos3
    show guide at right
    
    lance '“Is this supposed to be a joke to you?!”'

    gavin '“Lance–”'

    lance '“You strike us down without any hesitation, and now you have us playing with dolls!”'
    lance '“I demand to be taken seriously! How are we supposed to save the world if you just have us playing pretend in the wastes?!”'
    lance '“We’re Chosen heroes! We’re not babies! Why are you two going along with this?!”'

    morgan '“Lance, if we jump too hastily into more advanced fights than we’re ready for, we might get hurt!”'

    guide '{b}I like the tall one. The others would do well to learn from him.{/b}'

    guide 'He’s brash and arrogant. He’s going to get them in trouble. It’s like he forgot all about yesterday’s loss.'

    guide '{b}He wants to grow. He wants to become powerful. We need that.{/b}'

    guide '“…”'
    guide '“You want more of a fight? Fine.”'

    guide 'It’s been a while since I cast this spell…'
    guide 'Spells were more Gwen’s thing. We’ll see if I remember…'

    ## BEGIN COMBAT with Training Dummy (Enhanced)
    ## AFTER COMBAT, LANCE is far more satisfied.

    scene fnc_cabinfp_day1 with fade
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3
    show guide at right

    lance '“Better. We actually used our skills a bit.”'

    gavin '“I guess that was pretty fun, actually.”'
    gavin '“But Guide, why didn’t you do that before?”'

    guide '“I hoped you’d give up and leave.”'
    guide '“Your friend’s conviction is very… persuasive.”'

    show lance happy at sprite_bounce_light

    lance '“Almost like I was leading by example.”'

    guide 'Oh, brother.'

    guide '{b}He shows the most promise of any of them. He is a leader, by my standards.{/b}'
    guide '{b}As far as I’m concerned, their success lies squarely with him, for the time being.{/b}'
    guide '{b}Maybe he’s the one who will renew the cycle.{/b}'

    guide 'Gods, why didn’t they just leave?'

    guide '“Enough. You’ve succeeded in proving to me you’re more capable in combat than I thought.”'
    guide '“But there will be more to your success than your ability to tear enemies apart.”'
    guide '“We’ll continue tomorrow. Rest for a moment, then you all will help me in the garden and we’ll look for game for dinner.”'

    gavin '“You have a garden? Oh, cool! Can I see it now? Can you tell me how you take care of it? Where did you find the seeds?”'

    guide '“I–”'

    gavin '“How long have you had it? How did you fertilize the soil? One time, I saw a garden that was fertilized with–”'

    guide '“Hush, boy.”'

    gavin 'and the others are surprised by the [guide_name]’s tone. It’s harsher than they’re used to.'

    guide '“... Come to the garden and I’ll tell you.”'

    ## GAVIN goes off screen.
    hide gavin with easeoutleft
    hide guide with easeoutright

    ## FADE OUT to black
    scene backdrop_black with dissolve

    ## END SCENE
    return

label day2_dinner:
    # No FADE IN yet. Just a black screen as the GUIDE gives some exposition.
    scene backdrop_black

    guide 'Gavin was surprisingly knowledgeable about gardening and agriculture. I suppose I should expect the children left in this world to know more about survival than those I’ve known in the past.'
    guide 'But the extent of his knowledge speaks to a need greater than a boy his age would have need of with the right support.'
    guide 'And Morgan, being quiet as a mouse, is quite the little hunter. I thought something was wrong when she came and urgently tugged on my sleeve, until she showed me the rope trap and the coyote dangling from it.'
    guide 'Even though Lance didn’t help much, it was surprisingly refreshing to see something he’s lacking in.'
    guide 'Though it does beg the question how he survived for as long as he has.'

    # FADE IN to CABIN INTERIOR. For the sake of time, for now this is just the three HEROES directly in front of the screen side by side.
    scene fnc_cabing1_day1 with fade
    show gavin at linedup_center_pos1
    show lance at linedup_center_pos2
    show morgan at linedup_center_pos3
    show guide at right

    gavin '“... And we didn’t even have to mix in clay or shredded bark for substance!”'

    guide '“I thought that practice died years ago.”'

    lance '“It did, but it got picked back up with the decrease in animal population.”'

    guide 'A harrowing thought. Though the implication that they haven’t resorted to cannibalism yet is promising.'
    guide 'However, I know little else about them, these children in my home. I know it’s common courtesy to make polite conversation; I haven’t forgotten my manners.'
    guide 'But knowing what’s to come, it feels pointless to ask.'
    guide '… Then again, it would be better than this awkward silence.'

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

    # MORGAN is clearly uncomfortable.
    show morgan uncomfortable

    morgan '“...”'

    gavin '“She… doesn’t like to talk about the time before she was with me.”'

    guide '{b}Not that it matters. None of their little stories matter.{/b}'
    guide '{b}What matters is what they will become.{/b}'

    guide 'We can’t properly direct them if we don’t know to some extent where they’ve come from or who they are.'

    guide '“I presume you all have faced great loss in some form in your lives.”'
    guide '“It would be rather shocking if you haven’t.”'

    lance '“You want our sob stories now?”'

    guide '“I want to know if you know what to expect with this duty you pursue.”'

    # The three HEROES just look among themselves quietly.
    show morgan
    show lance
    show gavin

    guide '{b}They’re clueless. Ignorant. Good. We can embellish a little.{/b}'

    guide 'We already do them disservice enough by nature of trapping them in the cycle. I will not deceive them as to the gravity of what they will accomplish.'

    guide '{b}If that is your choice, it is better to tell them nothing at all. Let them live their little lie of saving the world.{/b}'

    menu:
        'You won’t understand':
            jump day2_dinner_wont_understand
        'Tell them':
            jump day2_dinner_tell_them

    label day2_dinner_wont_understand:
        guide '“The finer details don’t matter, I suppose. It may be too complex for you to fully comprehend.”'

        gavin '“This is our sacred mission! We know we have to fight the Hidden Darkness… uh, and I guess the ‘hidden’ part means we have to find it.”'
        gavin '“Which I figured you’d help us with when we’re ready.”'
        gavin '“But we don’t know how to find it, or how to fight it.”'
        gavin '“If we’re Chosen, there must be something special about us that no one else has, otherwise, someone else would have found and destroyed it by now, right?”'

        guide '“Not an incorrect assumption. But it’s more complex than that.”'

        lance '“Then tell us. We need to be as prepared as possible to win that fight when it happens.”'
        lance '“You won’t know if we won’t understand unless you try to tell us.”'

        guide '{b}You could let me out to tell them. I’ll tell them just enough.{/b}'

        guide 'No. Get out of my throat.'

    label day2_dinner_tell_them:
        guide '“Very well, then.”'
        guide '“The Hidden Darkness is indeed a malevolent force you must find, but its origin may be closer to that which you understand than you might hope.”'
        guide '“It started with one person. Just one.”'
        guide '“It wasn’t born out of malice, or hate. It wasn’t created intentionally, but it didn’t come from nothing, either. The Hidden Darkness is a monster, yes, but it was a monster no one wished upon anyone.”'
        guide '“The Hidden Darkness was born from sorrow, distrust, and a loss of faith and hope.”'
        guide '“The Hidden Darkness was born as a response to the moral corruption of the world, and the people in it. When the corruption became too great, and the forces of good became too scattered and weak to oppose it, that is what birthed the Darkness. Guide “When leaders failed their people beyond retribution, when nature teetered too far to one side of extinction, and when love and trust became commodities rather than gifts…”'
        guide '“The combination of those failures were the catalyst for a heartbreak too great to mend. And thus, that was the catalyst that brought life to the Darkness, and in the shadows it began to spread.”'
        guide '“Not only did it feed off of the negative energy that pervaded the world, it empowered it. The feedback loop enabled the Darkness to spread like a disease– and it presented itself as such.”'
        guide '“Whatever it touched, it infected, or killed outright. And those that it infected, it changed.”'
        guide '“No doubt you have seen it.”'

        lance '“The Corrupted.”'

        guide '“Yes.”'
        guide '“Tell me what you know about them.”'

        lance '“The Corrupted–”'

        morgan '“They’re mutated masses of dangerous energy and necrotic aura.”'
        morgan '“They’re hostile to any and all life– human, animal, fungi– all of it.”'
        morgan '“And it would rather die than flee from a fight… because it knows if it can hurt you and get in your blood, even if it’s dead… it can kill you.”'

        guide '“I’m impressed.”'

        gavin '“So if the Corrupted are part of the Hidden Darkness, then destroying the Darkness would destroy all the corrupted, too?”'

        guide '“Of that, I’m not entirely sure. In a sense, I suppose the answer is yes…”'

        gavin '“Then how do we find it? How do we defeat it? The sooner we can do that, the sooner we can save everyone!”'

        guide 'Were it so simple…'

        guide '{b}They will fight it. It is their destiny.{/b}'

        guide '“There will come a day when you will look upon someone, something, or even just a shadow in a corner… and you will know.”'
        guide '“One day, all it will take is a glance, and you will see it.”'
        guide '“It’s the ‘Hidden Darkness’ for a reason, after all.”'
        guide '“As for its defeat…”'
        guide '“... I don’t know.”'

        lance '“You don’t know?”'
        lance '“Well, if the Roots didn’t know, I guess you wouldn’t.”'

        guide '“It’s getting late. If you’re all finished with dinner, you should rest.”'
        guide '“But clean your plates first.”'

    # The HEROES leave.
    hide gavin
    hide lance
    hide morgan
    with easeoutleft
    
    guide '{b}Those poor children…{/b}'
    guide '{b}They’ll be in for quite the shock when their eyes finally open.{/b}'
    guide '{b}I remember when you saw it for the first time–{/b}'

    guide 'I have no intention of thinking about that right now.'
    guide 'My only intention is to sleep.'

    ## FADE OUT
    scene backdrop_black with dissolve

    ## END SCENE
    return

label day2_dream:
    "DAY 2 - DREAM"
    return