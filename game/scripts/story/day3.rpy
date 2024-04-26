label day3_morning:
    'DAY 3 - MORNING - IF TIME'
    call hero_paths_choice
    return

label day3_combat:
    ## FADE IN to WASTELAND. Hollow wind or desert sound.
    scene wasteland
    with fade
    play music bgm_desert_wind

    ## The group is traveling in search of examples of more obvious malevolent forces. What once might have been a sprawling city can barely be discerned from the rest of the landscape, with only a few walls or building frames sticking up here or there.
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3

    lance '“It’s so obvious no one has been here in a long time.”'
    lance '“I thought we were past you wasting our time, Guide.”'

    guide '“Gods, you’re an impatient little brat.”'
    guide '“Hold your tongue for longer than five seconds and you might actually learn something.”'

    gavin '“Yeah, Lance... sheesh.”'
    lance '“Oh, I’m sorry, I didn’t realize we were monks now.”'
    morgan '“What’s a monk...?”'
    gavin '“I think it’s like half a monkey.”'
    morgan '“... What’s a monkey...?”'

    show lance happy

    lance '“Ppfft.”'
    morgan '“It’s not funny, Lance! Not everyone came from the ruins of a college town like you!”'
    lance '“Didn’t you and Gavin live in the ruins of a zoo for a few months?”'
    gavin '“That’s what the adults told us. But it was all indoors, and all the animal cages were small and had beds and toilets.”'

    show lance

    guide '“For the love of -- be quiet, all of you.”'
    guide 'Gods of patience and mercy, grant me strength while I recall why I decided never to have kids...'
    guide '“Listen up. I told you all why we came out here, now I will tell you again.”'
    guide '“If you want to have any chance of finding and defeating the Hidden Darkness, you must learn to find its vestiges in unlikely places.”'
    guide '“The corruption born from the Darkness first took root in places like this.”'
    gavin '“It... doesn’t look like there’s anything here?”'

    guide '“Precisely.”'
    guide '“All the darkness can do is warp, corrupt, and consume, until there’s nothing left to change. Then, it moves on to where it can find something new to destroy.”'
    guide '“That does not mean it doesn’t haunt what it leaves behind.”'
    guide '“Listen closely. Attune yourself to the environment. Concentrate hard enough, and you will hear the ghosts of the past that could not move on.”'
    guide '“Listen closely, and you’ll find the agony that remains.”'

    ## The HEROES all look around.

    morgan '“... Maybe we can try that bigger building over there? It looks like it was important once.”'

    lance '“Crumbled pillars, barred window frames, stone steps... either a place of government or finance.”'
    lance '“Not a bad idea.”'

    guide '“Lead on, then.”'

    ## FADE OUT character sprites
    hide gavin
    hide lance
    hide morgan
    hide guide
    with dissolve

    ## FADE IN to DESTROYED BUILDING INTERIOR. Some sort of echoey ambiance
    $ cf('audio/bgm/bgm_dangerous_path.ogg')
    scene abandoned_building
    with Fade(0.5, 0.5, 0.5)

    ## FADE IN character sprites
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3

    guide 'I can already feel the chill of tragedy and pain deep in the walls.'
    guide 'This place may be more than they’re ready to handle...'

    gavin '“Whoa, check this out! There’s half a rubber duck sitting on the desk here!”'

    lance '“You know what a rubber duck is, but not a monkey?”'
    lance '“Let me see that.”'

    gavin '“No way! I found it first.”'

    lance '“I wasn’t gonna take it from you, idiot, I just wanted to look.”'

    guide '“Lance, we don’t use that language here.”'
    guide_dark 'Hah! You sound like mother!'

    gavin '“Yeah, Lance, be nice to me.”'
    gavin '“I’m the leader after all.”'

    show lance angry
    lance '“We agreed no one was a leader!”'

    show gavin angry
    gavin '“Well it doesn’t make sense not to have one! There has to be someone who tells the others what to do!”'
    lance '“I don’t need you telling me anything!”'
    guide '“Enough of that --”'
    gavin '“Well when I don’t say anything, you just end up being a huge jerk all the time!”'
    gavin '“Being smarter than us doesn’t make you better!”'

    lance '“You know what it does make me? Better fit to be a leader.”'
    lance '“Just because the Roots of the World spoke to you first doesn’t mean you’re in charge by default!”'

    guide '“Boys --!”'
    guide_dark 'Conflict? Already? No. This is unacceptable --'
    gavin '“We probably wouldn’t have made it here if you’d been leading us! You probably would have made someone mad enough to leave us to starve when we were jumping from camp to camp!”'
    lance '“We wouldn’t have wasted time being their errand dogs, because you always have to please everyone so they won’t leave you like --”'
    guide '“Ignorant fools, I said silence!”'

    ## The boys do stop arguing, looking surprised. Meanwhile, the sound of something dropping heavily around the corner, followed by a strange groaning.
    show gavin surprised
    show lance surprised

    stop music fadeout 0.25
    play sound object_falling
    pause 0.25

    morgan '“... It’s here..!”'
    gavin '“Was it attracted by our noise? Or by..?”'
    lance '“Less questioning, more killing.”'
    guide '“Just -- focus on the sensation of its aura. Pay attention to the way you’re feeling. How the air has shifted.”'
    guide '“Consider what must have transpired here for such corruption to take root...”'
    guide '“And know that you can find it anywhere if you look hard enough.”'
    guide '“Nothing is sacred.”'
    guide '“And nothing -- no one -- is guaranteed to protect you.”'

    ## There’s a ROAR, BEGIN COMBAT
    play sound monster_roar
    "COMBAT COMBAT_CORRUPTED_WEAK"
    # call combat_corrupted_weak

    ## AFTER COMBAT, the HEROES look shaken, except for LANCE.
    show gavin uncomfortable at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan uncomfortable at grouped_left_pos3

    gavin '“I -- I’ve never seen one so close, until now... it was always the adults who fought them, or... disappeared with them.”'
    gavin '“I... I didn’t know they were...”'

    morgan '“They’re -- they were -- human...”'

    ## LANCE looks at both HEROES.
    lance '“Really? You guys didn’t know this?”'
    lance '“The monkeys were expected. How could you not know the Corrupted were once living things?”'
    lance '“It’s like Guide said; they weren’t born from nothing.”'

    morgan '“He said they were born from the Darkness! Not... this.”'

    guide '“They do originate from the Darkness, yes.”'
    guide '“But just like the Hidden Darkness begins within the heart and soul of a single person, the corruption within the Darkness also requires a host to grow and spread.”'

    gavin '“... We didn’t know...”'
    gavin '“Why wouldn’t they have told us? The adults we traveled with -- they had to have known, didn’t they?”'
    gavin '“Why didn’t they tell us..?”'

    guide_dark 'Hmm... to leave them ignorant for so long...'
    guide_dark 'Good. That leaves them more malleable to their destiny.'

    guide 'I don’t want to hear it.'
    lance '“If you’d been paying attention, you probably could have figured it out on your own, you know.”'
    lance '“I guarantee someone you once knew is one of these things now. It’s statistically improbable for them not to be.”'
    lance '“Everyone falls to these things eventually.”'
    lance '“Everyone becomes Corrupted, eventually.”'

    ## MORGAN looks horrified and disbelieving.
    show morgan uncomfortable

    gavin '“... We’re all vulnerable..?”'
    gavin '“Even us? Even though we know better?”'

    guide '“No one is immune to falling to the Darkness.”'
    guide '“That’s why you must learn to be aware of it in every corner it may lurk, building or soul.”'

    ## Everyone pauses for a moment in contemplation.
    pause 1.5

    gavin '“... Can we go home now?”'

    guide_dark 'He can’t be tired already. That was only one --'
    guide 'We can go home.'

    ## FADE OUT
    scene backdrop_black with dissolve

    ## END SCENE
    return

label day3_dinner:
    ## BLACK SCREEN
    scene backdrop_black

    guide 'The journey home was unusually quiet. The heroes had been rambunctious when they first came to me. Even Morgan was considerably subdued in comparison to when she had first arrived at my doorstep.'
    guide 'Naturally, they had much to consider. It seems it hadn’t occurred to them before that the darkness they’d been taught to fear could lurk in the hearts of those they trusted most.'
    guide 'But questioning everything is the first crucial step in directing them towards what they were Chosen to do.'
    guide 'If they remain ignorant and complacent in who they believe is friend or foe...'
    guide_dark 'They’ll never reach the potential they need to continue the cycle.'

    ## FADE IN to CABIN INTERIOR
    ## Everyone is quiet and looks greatly unnerved.
    scene fnc_cabing1_day1 with fade
    show gavin uncomfortable at linedup_center_pos1
    show lance uncomfortable at linedup_center_pos2
    show morgan uncomfortable at linedup_center_pos3

    gavin '“... Guide? How do we know we’re not corrupted?”'

    guide '“You would know.”'

    gavin '“But how?”'

    guide '“...”'
    guide '“You would hate everyone, and everything. Even those you once loved most.”'
    guide '“Everything would be pointless, a waste of time and energy to care for. At the same time, those same things would be valuable to you only in what they could offer in service to your own joy or survival.”'
    guide '“You would want everything they could offer, without providing anything in return.”'
    guide '“Put simply, hatred and hopelessness would become an addiction, because no other emotion could compare.”'

    morgan '“But that makes it sound like... the Corrupted could be saved?”'

    lance '“What?”'

    morgan '“If what makes someone corrupted is hate and hopelessness, they just... need to have hope again, right?”'
    morgan '“Couldn’t that bring them back?”'

    guide '“I assure you, if it were so simple--”'

    lance '“That’s stupid. All Corrupted are beyond saving.”'
    lance '“Didn’t you feel it in the air when we were in that building earlier? It sucked life right out of the room-- right out of us.”'
    lance '“It wasn’t a thing that could be reasoned with.”'

    morgan '“How do you know that, Mr. Know-It-All? Have you tried before?”'
    morgan '“If they were once people, wouldn’t there still be something left there that was once part of them? Who they used to be?”'

    lance '“You mean their organs? Their body? Sure, that’s all probably still there.”'
    lance '“Even if it’s nothing more than disintegrated goop.”'
    lance '“The body is still there though it’s changed. But the actual person? I assure you, that part died ages ago.”'

    morgan '“That can’t be true!”'

    guide '“Morgan, calm yourself.”'
    guide '“Lance is correct. All that remains of the person the Corrupted once were is their deepest hatred and sorrow.”'
    guide '“Of any emotion left, all they have is that, and a profound sense of betrayal.”'

    morgan '“Betrayal?”'
    morgan '“Of course they would feel betrayed! Those were once people’s friends! Families!”'
    morgan '“And they were just left behind to die!”'

    lance '“How was anyone going to save them, Morgan?”'
    lance '“It would have been a waste of resources and time even if they could be brought back from the brink.”'

    morgan '“How could you say that?!”'

    lance '“They’re monsters, Morgan! There’s nothing human left in them!”'

    gavin '“Guys-- guys, please, let Guide talk. I can tell he has something more to say about all of this.”'
    gavin '“Right?”'

    ## (The first choice of the game that leads to two different potential scene outcomes. There are still no long term consequences due to time constraints with the jam however.)

    menu day3_dinner_choice:
        'Let them discuss their thoughts and theories':
            jump day3_dinner_choice_theories
        'Tell them the history of the Corrupted':
            jump day3_dinner_choice_history

    label day3_dinner_choice_theories:
        guide_dark 'Deciding not to intervene? Oh, this could get interesting.'

        guide '“This could be a valuable learning moment for you all. Keep going.”'

        gavin '“Huh--?”'

        lance '“I’ll take your decision to be quiet as a point for my case.”'
        lance '“Think about it, Morgan; where do we decide what’s human and what isn’t?”'
        lance '“Is a thing that doesn’t think, speak, or feel like we do human?”'

        # [Unfinished, will come back to this]

        jump day3_dinner_end

    label day3_dinner_choice_history:
        guide '“I do have information for you all, yes.”'
        guide '“Settle down, all three of you. There is more yet to be told about the Hidden Darkness and the Corruption it wrought upon our world.”'

        ## The HEROES settle back down. LANCE and MORGAN are still angry with each other, but they’re not fighting anymore.
        guide '“As Morgan said last night, the Corrupted are mutated masses. They are dangerous, and they are necrotic in nature.”'
        guide '“And, as Morgan said, it would sooner kill you than run away. The promise of life is too great to turn away from.”'
        guide '“The fact that they were once human does not change what they desire now. All that matters to the Corrupted is their own survival and growth of power. The people they once were truly no longer exist.”'

        gavin '“If that’s the case, and the Corrupted started appearing early on in the first days that the Hidden Darkness awoke...”'
        gavin '“Then it would have sought out the most powerful people to feed off of, right?”'

        guide '“Yes, exactly.”'
        guide '“The Corruption did not spread like a normal disease, like a cold or flu. The disease was neither virus nor bacteria, not fungi or parasite.”'
        guide '“Because the Corruption sought the most powerful people first, our leaders and business people, research for a cure began immediately, but there was nothing to cure in the traditional sense.”'
        guide '“It is a disease of the very soul itself. It is incurable.”'
        guide '“With it being such that those who ruled at the time were selfish and cruel regardless, the Corruption was, at first, cause for celebration for the common populace. It seemed the worst of humanity would be the only ones impacted.”'
        guide '“That celebration did not last long when the leaders who did remain saw an opportunity to take advantage of their enemies’ weaknesses.”'
        guide '“They garnished the guise of their wars under all manner of excuses. Some bought into them. Most of us knew better.”'
        guide '“All the same, the more war, famine, and disease spread in a mad grab for power, so too did the Corruption further spread.”'
        guide '“Any belief that it would dissipate when the most cruel and powerful people were eradicated quickly diminished, and died.”'
        guide '“Even when people ceased to volunteer to take up the positions of the deceased, the Corruption no longer seemed to differentiate between the worst of us, and those considered only mildly nefarious.”'
        guide '“By the time the Corruption began to spread to animals, and then to the land itself, it was far too late for any substantial action to be taken.”'
        guide '“All institutions of order and aid crumbled. The few remaining civilizations left dispersed with no central power to maintain them.”'
        guide '“The actions of a select few in the beginning of the end of the world, is what led to it all spiraling so far out of hand to begin with.”'

        ## The HEROES sit in silence yet again.
        guide_dark 'Too much all at once-- you’ve broken their hearts.'

        guide 'I so wish you would go back to sleep.'

        guide_dark 'And miss all the build up? Miss all the fun?'

        lance '“... You’re saying... this all could have been stopped?”'
        lance '“That if everyone had seen what was happening for what it was, none of this would have happened?”'

        guide '“... I don’t know.”'
        guide '“I am saying that there were signs.”'
        guide '“Truthfully, if it could have been stopped, I don’t know what could have been done.”'
        guide '“The existing institutions of power had been determined for a very long time to minimize the power of the people beneath them, to the point of irrelevance.”'
        guide '“That included the power to gather.”'

        lance '“So they made themselves vulnerable by shutting out the people they were supposed to protect?”'
        lance '“... How did these institutions find out about the Hidden Darkness then, if all they were really concerned about was the Corruption right in front of them and how to use it against their enemies?”'

        guide_dark 'Now you’ve got them thinking.'
        guide_dark 'But it’s not time to tell them that yet.'

        guide '“That can be discussed later. It’s time for you all to turn in for the night.”'

        gavin '“But-- they were more technologically advanced. They must have had a way to detect the Hidden Darkness that’s better than just... {i}feeling{/i} the air for it.”'

        guide '“Haven’t you had enough of me yapping, {b}boy?{/b}”'

        guide_dark '“You’ll learn what you need to know when you need to know it.”'

        ## The HEROES look at each other nervously. They depart from the table one by one.
        guide_dark 'You are not assertive enough with them and their inquiries.'
        guide_dark 'If they know too much before they’re ready, the cycle--'

        guide 'I don’t want to hear about the damn cycle tonight.'
        guide 'You had better stay out of my dreams.'

        guide_dark '{i}Your{/i} dreams?'
        guide_dark 'Ah... cute. Keep believing this mind is still yours.'
        guide_dark 'Whatever helps you to help them.'

        # The screen throbs red
        show overlay_pain with screen_shake_light
        hide overlay_pain
        guide_dark '{i}Thus, always.{/i}'
        stop music

    label day3_dinner_end:
        # FADE OUT
        scene backdrop_black with dissolve

        # END SCENE
        return

label day3_dream:
    # BLACK SCREEN. The sound of jets, gunfire, screaming, explosions.
    scene backdrop_black with fade
    play music bgm_war_sounds fadein 2.0 volume 0.75
    play music_extra bgm_crowd_panic fadein 4.0 volume 0.5

    # Sound of RUNNING
    ## FADE IN misty background we’ve been using, tinted red. I can make another image for this if need be.
    ## Sound of a jet flying very close. A very loud explosion nearby. 

    play sound running volume 0.75
    gwen '“Lucas, keep up! We have to go!”'

    play sound jet_flyby volume 0.75
    lucas '“I -- I can’t. I can’t -- breathe --”'

    guide '“Grab one arm, I’ll grab the other.”'
    
    scene backdrop_mist_red with Fade(0.5, 0.0, 0.5)
    play sound_extra explosion_nearby volume 1.0

    guide '“Shit --!”'

    guide_dark 'Your first swear, if I recall. Tame under the circumstances.'

    guide 'You weren’t there for that.'

    guide_dark 'Is a USB unable to pull pictures from a hard drive if it was never plugged in before their creation?'
    
    play music bgm_war_sounds fadein 0.0 volume 0.5
    gwen '“Up ahead! I can see the military!”'
    gwen '“Keep going, Lucas!”'
    stop music_extra fadeout 4.0

    ## The sound of a car horn, a vehicle almost hitting the GUIDE and his friends.
    play sound car_horn volume 1.0
    play music bgm_war_sounds fadein 0.0 volume 0.25
    guide '“What the hell?!{w=1.0} Back off!{w=1.0} Argh!{w=1.0} What is wrong with these people?!”'
    guide '“It’s like they can’t even see us!”'

    gwen '“Lucas, don’t you {i}dare{/i} pass out now.”'

    scene backdrop_black with None
    guide_dark 'And so you ran, and ran, and all the other people ignored three lonely children without any parents or family, in favor of their own hides.'
    guide_dark 'And when you got to the barricade and pleaded for your lives with everyone else...'
    guide_dark 'What was it they said? That this was a “quarantine zone?” That no one was allowed in or out? Not even their own friends or families?'
    scene backdrop_mist_red with None
    ## The sound of another explosion. Angry and scared yelling crowds.
    play sound_extra explosion_nearby volume 0.75
    play music_extra bgm_crowd_panic fadein 2.0 volume 0.5
    guide '“You’re just gonna let us all die?!”'
    pause 1.0

    # Justin: it might be useful to have another screen here with a CG showing the fence and the attack of Corrupted creatures

    ## The screen shakes, a sound as the GUIDE kicks a metal fence
    play sound fence_hit
    guide '“Bastards!”' with screen_shake_mid
    gwen '“Please, our friend -- he won’t make it if you leave us in here!”'
    stop music_extra fadeout 2.0

    ## The military on the other side of the fence is suddenly assaulted by Corrupted creatures. This is symbolized by monstrous sounds, followed by yelling and gunfire.

    play sound monster_roar
    pause 1.0
    play sound_extra gunfire
    pause 0.5
    play music_extra bgm_crowd_panic fadein 2.0 volume 0.75

    guide_dark 'What fools, to think they could just lock away the problem and keep living their little status-quo on the outside.'

    guide 'I don’t want to see this again! I -- I have to wake up. I have to --'

    ## The screen transitions immediately to black. All the sound stops.
    stop music
    stop music_extra
    stop sound
    stop sound_extra
    scene backdrop_black
    with Fade(0.0, 0.0, 0.0)


    guide_dark 'You have to...?'
    guide_dark 'You have to... what? Pinch yourself? Hold your breath and count to ten?'
    guide_dark 'Waking up won’t make the past go away. Nor will it stop reminding you of the future yet to pass.'
    guide_dark 'Remember the pain. Remember the horror.'
    guide_dark 'Remember how the actions of those who were supposed to protect you only made everything worse.'
    guide_dark 'Remember how they failed you. Remember how they {i}failed{/i} you, so that you might try not to make their same mistakes...'
    guide_dark 'And then fail all the same.'

    guide 'I never intended on not making the same mistakes.'
    guide 'You make that impossible.'
    guide 'I just want to get this over with so I don’t have to worry about it anymore.'

    guide_dark 'How responsible of you! Then again, what else could I expect?'
    guide_dark 'Running from your problems is all you know.'

    guide 'That’s not true. We {i}tried{/i} to change things.'
    guide 'Me, Gwen, Lucas -- our first thought wasn’t to just lay down and die.'
    guide 'We escaped the town and left everything behind -- friends, family. Siblings.'
    guide 'We made the best of what was left, tried to help others like us -- children who had lost everything -- but soon, there wasn’t anything left to work with.'
    guide 'Even when we started hearing the radio reports about the few scientists left banding together to try to reverse the Corruption, or find someplace else to go...'
    guide 'We decided something had to change.'
    guide 'That there had to be something we could do to stop it. Save everyone.'

    guide_dark 'Until you found the Roots.'

    guide '... Until we found the Roots.'

    guide_dark 'A sacred place of pilgrimage. A sacred place with a sacred message, a message beyond that which only the Chosen could hear.'
    guide_dark 'And tell me, what did that message say?'

    guide 'That message is flawed. It doesn’t -- didn’t -- speak the truth of the world.'

    guide_dark 'Didn’t?'

    guide 'It was a warning. It warned us what the future might become.'

    guide_dark 'So it speaks truth now?'
    guide_dark 'Tell me what it said.'

    guide '...'

    ## The screen fades in to the MISTY background, tinted dull green. There’s a “throbbing” ambiance (I can’t think of a better way to describe it -- it’s just an unnerving sound.)

    scene backdrop_mist_green
    with fade
    play music bgm_drone_throb

    guide '{i}This place is a message... and part of a system of messages... pay attention to it!{/i}'
    guide '{i}Sending this message was important to us. We considered ourselves to be a powerful culture.{/i}'
    guide '{i}This place is not a place of honor... no highly esteemed deed is commemorated here... nothing valued is here.{/i}'
    guide '{i}What is here was dangerous and repulsive to us. This message is a warning about danger.{/i}'
    guide '{i}The danger is in a particular location... it increases towards a center... the center of danger is here... of a particular size and shape, and below us.{/i}'
    guide '{i}The danger is still present, in your time, as it was in ours.{/i}'
    guide '{i}The danger is to the body, and it can kill.{/i}'
    guide '{i}The form of the danger is an emanation of energy.{/i}'
    guide '{i}The danger is unleashed only if you substantially disturb this place physically.{/i}'
    guide '{i}This place is best shunned and left uninhabited.{/i}'

    guide_dark 'This place is not a place of honor. We considered ourselves to be a powerful culture. {i}Nothing is valued here{/i}.'
    guide_dark 'What a rich and timeless message!'
    guide_dark 'The folly of man and its toxic legacy, forever immortalized in every life.'
    guide_dark 'A message so universally transferable to all things, it’s a wonder it’s not yet considered scripture.'
    guide_dark 'With that reminder fresh on your mind, tell me...'
    guide_dark 'What does it mean now, after all this time, to be {i}Chosen{/i}?'

    menu day3_dream_choice:
        "It's an inevitability.":
            jump day3_dream_choice_inevitability
        "It's a curse.":
            jump day3_dream_choice_curse
        "It's a calling":
            jump day3_dream_choice_calling

    ## > It’s an inevitability.
    label day3_dream_choice_inevitability:
        guide 'It’s the inevitability of time and growth and the passing of the torch.'
        guide 'If it wasn’t me, or Gwen, Or Lucas, it would have been someone else. Someone else would have taken up the role.'
        guide 'As long as there were people who lived and breathed and were considered human, there always would have been someone Chosen.'
        guide 'Some things are just inescapable, barring annihilation.'
        jump day3_dream_choice_reconvene

    ## > It’s a curse.
    label day3_dream_choice_curse:
        guide 'One generation after the other, this life into the next, it’s a curse we have yet to break. Doing things only one certain way locks in certain outcomes.'
        guide 'All the imperfections we left behind in our rigidity are passed on to the next. I {i}loathe{/i} what those children will be bearing on their shoulders when the time comes.'
        guide 'And even if they spend their whole lives trying to patch the holes and blemishes, their own will be left behind for {i}their{/i} Chosen to deal with, ad infinitum.'
        guide 'Being Chosen means inevitable failure.'
        jump day3_dream_choice_reconvene

    ## > It’s a calling
    label day3_dream_choice_calling:
        guide 'It’s a summons to rise above the failures that made us. It’s knowing that life could be so much more.'
        guide 'And... it’s giving everything to that cause, and being stopped by the pre-existing systems and notions every step of the way.'
        guide 'And you compromise a little bit to make another step forward, and you compromise a little bit more, and a little bit more...'
        guide 'And at the end of it all, you look back and realize you’re hardly ten feet from where you started.'
        jump day3_dream_choice_reconvene

    ## > RECONVENE
    label day3_dream_choice_reconvene:
        guide 'To be Chosen is to be everything you never thought you would be.'

        ## There’s a pause. The ambiance slowly fades out. The screen shakes.

        gavin '“... Guide..!”'

        guide 'The boy..?'

        gavin '“Guide!”'

    # FADE OUT
    scene backdrop_black with dissolve

    # END SCENE
    return

label day3_night_combat:
    ## CABIN INTERIOR, night. GAVIN and LANCE are the two characters on screen. They look worried.
    scene fnc_cabing1_day1_nighttime with fade
    show gavin uncomfortable at grouped_left_pos1
    show lance uncomfortable at grouped_left_pos2

    gavin '“Guide! Get up! Morgan -- she’s gone!”'

    guide '“Gone? What do you mean, ‘gone?’”'

    lance '“It’s my fault. I -- I told her she was being a stupid baby about the whole Corrupted thing --”'

    guide '“The Corrupted?!”'

    lance '“-- so I think she went out to find one and prove it’s not dangerous!”'

    guide_dark 'What? No! She can’t do that! Does she have a death wish?'
    guide_dark 'We need the girl! {i}They{/i} need the girl!'
    guide_dark 'Without her, the cycle can’t continue!'

    guide '“Then we don’t have time to lose. Get your weapons, prepare your spells -- tell me which way she went.”'

    ## GAVIN and LUCAS run off to one side of the screen. FADE TRANSITION back into the Wasteland, night.
    hide gavin
    hide lance
    with easeoutleft

    guide 'I remember what it felt like to want to still have hope. I remember what it felt like to want to believe that everything could somehow turn around.'
    guide 'I remember seeing my first Corrupted, as I brandished my blade to protect Gwen and Lucas, and I remember seeing what was left of the poor soul it consumed -- the twisted agony, the fear.'
    guide 'I don’t blame Morgan. I think anyone who was ever Chosen felt such a way at least once.'
    guide 'But to go {i}alone{/i} to try and prove her thoughts and theories and hopes..!'
    guide 'I can only pray we aren’t too late.'

    ## The sound of a scream in the distance.
    play sound scream_woman
    gavin '“There! Around the corner!”'

    ## Fade in GAVIN and LANCE first, then Morgan second.
    show gavin uncomfortable at grouped_left_pos1
    show lance uncomfortable at grouped_left_pos2
    with fade

    show morgan uncomfortable at grouped_right_pos3
    with fade

    gavin '“Morgan!”'

    morgan '“Gavin! Lance! Help me!”'

    guide_dark 'Protect the girl! We need her power!'

    ## BEGIN BATTLE with strong variant CORRUPTED
    # call combat_corrupted_strong

    ## AFTER BATTLE, everyone catches their breath.

    guide '“Morgan? Are you injured?”'

    guide_dark 'That was too close.'

    morgan '“I... I’m okay.”'
    morgan '“I’m so sorry. I didn’t mean for this to happen. I only thought -- I wanted to...”'
    morgan '“... I didn’t think they could be lost.”'

    lance '“... Gods! What’s {i}wrong{/i} with you!”'

    gavin '“Lance, don’t --”'

    lance '“No! {i}Shut up{/i}!”'
    lance '“I’m sick of you guys ignoring me because you think I’m a know-it-all jerk!”'
    lance '“I’m not saying these things just to be mean! I know what I’m talking about!”'

    ## LANCE becomes teary and emotional.
    show lance angry

    lance '“Nothing left in the Corrupted knows anything about compassion or love!”'
    lance '“I saw what they did to my family! I {i}know{/i} what I’m talking about! Okay?!”'

    ## SURPRISED emotions on Gavin and Morgan
    show gavin surprised
    show morgan surprised

    lance '“They hated me before there wasn’t anything left of them!”'

    morgan '“Lance... why didn’t you tell us the truth? How long have your parents been gone for?”'
    morgan '“Gavin and I can hardly even remember our families. Did you think we were going to judge you?”'

    lance '“It only happened a little while before I met you guys.”'
    lance '“And you two were always talking about how much {i}fun{/i} you always had making new friends in new survivor groups.”'
    lance '“I didn’t want to be the odd one out. I’m {i}tired{/i} of being the odd one out.”'
    lance '“I didn’t know anyone outside of my family until I knew you guys. It was just me, Mom, Dad... my little brother...”'

    # LANCE is too overcome with emotion to keep talking.
    show lance sad

    lance '“I miss them. Why did it have to be them?”'
    lance '“I’m so sick of watching them {i}change{/i} when I close my eyes at night.”'
    lance '“I just want them back. I don’t want {i}this{/i}.”'

    ## GAVIN and MORGAN struggle to think of what to say.
    show gavin uncomfortable
    show morgan uncomfortable

    gavin '“We can be your family, Lance. If you’ll let us.”'
    gavin '“You know that, right?”'
    gavin '“We can’t be your mom and dad, but that doesn’t mean we can’t be... something else.”'

    morgan '“... We’d feel less weird about you if you were more honest with us.”'

    ## LANCE calms down a little.

    guide_dark 'How {i}touching{/i}.'
    guide_dark 'What a strong little boy.'

    guide 'I’m sick of {i}you{/i}.'

    ## The screen shakes and throbs red

    guide_dark '{i}Get used to me. I’m not going anywhere{/i}.'
    guide_dark '{i}It’s almost {u}my{/u} turn{/i}.'

    gavin '“Guide? You don’t look good.”'

    morgan '“I’m sure it’s my fault. I must have worried you all so much.”'

    guide '“No, I’m just... we’re glad you’re okay.”'

    guide_dark '“You are needed. You are more important than you know.”'

    morgan '“That’s... kind of you... but you still seem very unwell.”'
    morgan '“We should go home, shouldn’t we?”'

    lance '“... Home. Something like that.”'

    guide_dark '“We will discuss new rules when we return to the cabin, to ensure your safety.”'

    guide 'Get out of my throat! This isn’t your place to dictate!'

    guide_dark 'If you think you’ve been in control before the Chosen arrived, you have been {i}so{/i} sorely mistaken.'

    guide_dark '“All three of you play a role too important to risk upon such rash decisions. You have to reach your full potential before you can rush headfirst towards your destiny.”'

    gavin '“Our destiny..?”'
    gavin '“... You haven’t wanted to talk much about it before...”'

    guide_dark '“The time draws near where you will be ready to face the Hidden Darkness. To lose before you have the chance to accomplish what you were meant to would be disastrous for all life.”'

    morgan '“I guess he’s right.”'
    morgan '“I’m sorry, again, for the trouble.”'

    guide_dark '“You have learned. You will grow.”'
    guide_dark '“You will become stronger from this.”'
    guide_dark '“Now, go. I will watch our backs.”'

    ## One by one, the HEROES fade from the screen.

    ## There’s a GASP sound effect as the GUIDE regains control of himself.

    guide 'Gods! I couldn’t breathe!'

    guide_dark 'I suppose it’s been a while since I’ve had to consider such trivial functions.'

    guide_dark 'Now. {i}Walk{/i}.'

    # FADE OUT
    scene backdrop_black with dissolve

    # END SCENE
    return