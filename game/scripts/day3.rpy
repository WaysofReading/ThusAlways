label day3_morning:
    "DAY 3 - MORNING - IF TIME"
    call hero_paths_choice
    return

label day3_combat:
    # FADE IN to WASTELAND. Hollow wind or desert sound.
    scene wasteland
    with fade
    play music bgm_desert_wind

    # The group is traveling in search of examples of more obvious malevolent forces. What once might have been a sprawling city can barely be discerned from the rest of the landscape, with only a few walls or building frames sticking up here or there.
    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3
    show guide at right

    lance '“It’s so obvious no one has been here in a long time.”'
    lance '“I thought we were past you wasting our time, Guide.”'

    guide '“Gods, you’re an impatient little brat.”'
    guide '“Hold your tongue for longer than five seconds and you might actually learn something.”'

    gavin '“Yeah, Lance… sheesh.”'

    lance '“Oh, I’m sorry, I didn’t realize we were monks now.”'

    morgan '“What’s a monk..?”'

    gavin '“I think it’s like half a monkey.”'

    morgan '“... What’s a monkey..?”'

    show lance happy

    lance '“Ppfft.”'

    morgan '“It’s not funny, Lance! Not everyone came from the ruins of a college town like you!”'

    lance '“Didn’t you and Gavin live in the ruins of a zoo for a few months?”'

    gavin '“That’s what the adults told us. But it was all indoors, and all the animal cages were small and had beds and toilets.”'

    show lance

    guide '“For the love of– be quiet, all of you.”'
    guide 'Gods of patience and mercy, grant me strength while I recall why I decided never to have kids…'
    guide '“Listen up. I told you all why we came out here, now I will tell you again.”'
    guide '“If you want to have any chance of finding and defeating the Hidden Darkness, you must learn to find its vestiges in unlikely places.”'
    guide '“The corruption born from the Darkness first took root in places like this.”'
    gavin '“It… doesn’t look like there’s anything here?”'

    guide '“Precisely.”'
    guide '“All the darkness can do is warp, corrupt, and consume, until there’s nothing left to change. Then, it moves on to where it can find something new to destroy.”'
    guide '“That does not mean it doesn’t haunt what it leaves behind.”'
    guide '“Listen closely. Attune yourself to the environment. Concentrate hard enough, and you will hear the ghosts of the past that could not move on.”'
    guide '“Listen closely, and you’ll find the agony that remains.”'

    # The HEROES all look around.

    morgan '“... Maybe we can try that bigger building over there? It looks like it was important once.”'

    lance '“Crumbled pillars, barred window frames, stone steps… either a place of government or finance.”'
    lance '“Not a bad idea.”'

    guide '“Lead on, then.”'

    # FADE OUT character sprites

    hide gavin
    hide lance
    hide morgan
    hide guide
    with dissolve

    # FADE IN to DESTROYED BUILDING INTERIOR. Some sort of echoey ambiance

    scene abandoned_building
    with fade

    # play music bgm_echoey_building

    # FADE IN Character sprites.

    show gavin at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan at grouped_left_pos3
    show guide at right

    guide 'I can already feel the chill of tragedy and pain deep in the walls.'
    guide 'This place may be more than they’re ready to handle…'

    gavin '“Whoa, check this out! There’s half a rubber duck sitting on the desk here!”'

    lance '“You know what a rubber duck is, but not a monkey?”'
    lance '“Let me see that.”'

    gavin '“No way! I found it first.”'

    lance '“I wasn’t gonna take it from you, idiot, I just wanted to look.”'

    guide '“Lance, we don’t use that language here.”'
    guide '{b}Hah! You sound like mother!{/b}'
    gavin '“Yeah, Lance, be nice to me.”'
    gavin '“I’m the leader after all.”'

    show lance angry
    lance '“We agreed no one was a leader!”'

    show gavin angry
    gavin '“Well it doesn’t make sense not to have one! There has to be someone who tells the others what to do!”'

    lance '“I don’t need you telling me anything!”'

    guide '“Enough of that–”'
    gavin '“Well when I don’t say anything, you just end up being a huge jerk all the time!”'
    gavin '“Being smarter than us doesn’t make you better!”'

    lance '“You know what it does make me? Better fit to be a leader.”'
    lance '“Just because the Roots of the World spoke to you first doesn’t mean you’re in charge by default!”'

    guide '“Boys–!”'
    guide '{b}Conflict? Already? No. This is unacceptable–{/b}'
    gavin '“We probably wouldn’t have made it here if you’d been leading us! You probably would have made someone mad enough to leave us to starve when we were jumping from camp to camp!”'

    lance '“We wouldn’t have wasted time being their errand dogs, because you always have to please everyone so they won’t leave you like–”'

    guide '{b}“Ignorant fools, I said silence!”{/b}'

    # The boys do stop arguing, looking surprised. Meanwhile, the sound of something dropping heavily around the corner, followed by a strange groaning.
    show gavin surprised
    show lance surprised

    stop music
    # play sound object_drop
    # play sound monster_groan
    morgan '“... It’s here..!”'

    gavin '“Was it attracted by our noise? Or by..?”'

    lance '“Less questioning, more killing.”'

    guide '“Just– focus on the sensation of its aura. Pay attention to the way you’re feeling. How the air has shifted.”'
    guide '“Consider what must have transpired here for such corruption to take root…”'
    guide '“And know that you can find it anywhere if you look hard enough.”'
    guide '“Nothing is sacred.”'
    guide '“And nothing– no one– is guaranteed to protect you.”'

    # There’s a ROAR, BEGIN COMBAT

    # play sound monster_roar
    # call combat_corrupted_weak

    # AFTER COMBAT, the HEROES look shaken, except for LANCE.

    show gavin uncomfortable at grouped_left_pos1
    show lance at grouped_left_pos2
    show morgan uncomfortable at grouped_left_pos3
    show guide at right

    gavin '“I– I’ve never seen one so close, until now… it was always the adults who fought them, or… disappeared with them.”'
    gavin '“I… I didn’t know they were…”'

    morgan '“They’re– they were– human…”'

    lance 'looks at both heroes.'

    lance '“Really? You guys didn’t know this?”'
    lance '“The monkeys were expected. How could you not know the Corrupted were once living things?”'
    lance '“It’s like Guide said; they weren’t born from nothing.”'

    morgan '“He said they were born from the Darkness! Not… this.”'

    guide '“They do originate from the Darkness, yes.”'
    guide '“But just like the Hidden Darkness begins within the heart and soul of a single person, the corruption within the Darkness also requires a host to grow and spread.”'

    gavin '“... We didn’t know…”'
    gavin '“Why wouldn’t they have told us? The adults we traveled with– they had to have known, didn’t they?”'
    gavin '“Why didn’t they tell us..?”'

    guide '{b}Hmm… to leave them ignorant for so long…{/b}'
    guide '{b}Good. That leaves them more malleable to their destiny.{/b}'

    guide 'I don’t want to hear it.'
    lance '“If you’d been paying attention, you probably could have figured it out on your own, you know.”'
    lance '“I guarantee someone you once knew is one of these things now. It’s statistically improbable for them not to be.”'
    lance '“Everyone falls to these things eventually.”'
    lance '“Everyone becomes Corrupted, eventually.”'

    morgan 'looks horrified and disbelieving.'

    gavin '“... We’re all vulnerable..?”'
    gavin '“Even us? Even though we know better?”'

    guide '“No one is immune to falling to the Darkness.”'
    guide '“That’s why you must learn to be aware of it in every corner it may lurk, building or soul.”'

    # Everyone pauses for a moment in contemplation.
    ""
    pause 1.5

    gavin '“... Can we go home now?”'

    guide '{b}He can’t be tired already. That was only one–{/b}'
    guide 'We can go home.'

    # FADE OUT
    scene backdrop_black with dissolve

    # END SCENE
    return

label day3_dinner:
    "DAY 3 - DINNER"
    return

label day3_dream:
    "DAY 3 - DREAM"
    return