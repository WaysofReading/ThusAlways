label day4_morning:
    'DAY 4 - MORNING'
    call hero_paths_choice
    return

label day4_combat:
    ## FADE IN to CABIN EXTERIOR

    guide '“Again, Gavin. You swing too close to yourself. You’ll need more leverage and a broader reach if you hope to maximize the damage you can cause.”'

    ## FADE IN Gavin sprite

    gavin '“Yes, Guide.”'

    guide '“Morgan, concentrate on your surroundings. Your duty is to care for your well being, and the well being of your friends. What’s immediately in front of you may not always be the most important thing.”'

    ## FADE IN Morgan sprite

    morgan '“Okay.”'

    guide '“Lance... for the love of the gods, {i}please{/i} relax your shoulders.”'

    ## FADE IN Lance sprite

    lance '“I’m {i}trying{/i}.”'

    guide_dark '“Try --”'

    guide '“-- Try exhaling when you cast, instead of inhaling.”'

    guide_dark 'You can’t interrupt me!'

    guide 'I just did.'

    guide_dark 'You and they are taking {i}too long.{/i}'
    guide_dark 'What next? You’ll take them on a journey to find ice cream?'
    guide_dark 'They’ll have to leave the nest sooner rather than later.'
    guide_dark 'Don’t tell me you’ve gone {i}soft{/i}.'

    guide '...'

    guide_dark 'Oh, you can’t be serious.'

    guide 'This isn’t right. Or fair.'

    guide_dark 'Right? Fair? When has that ever stopped any of this?'
    guide_dark 'The cycle doesn’t {i}care{/i} about your precious right or fair.'
    guide_dark 'You only get what’s {i}earned{/i}. And when nothing changes...'

    ## There’s a ROAR of a corrupted monster somewhere closeby.

    guide_dark 'You don’t {i}earn{/i} any change.'

    ## The HEROES draw their weapons.

    morgan '“They followed us here..?”'

    gavin '“I guess it had to happen sooner or later. We’ve got this!”'

    ## BEGIN COMBAT

    ## AFTER COMBAT

    guide_dark '“Good. That won’t be the last of them though.”'

    guide 'You! Stop talking, you’re going to --'

    guide_dark 'Relax, I’ll remember to breathe this time.'

    gavin '“Yeah... usually once they start showing up, they don’t stop.”'

    lance '“So it’s not safe here anymore?”'

    guide_dark '“You’ll be fine. Besides, it will be good practice.”'

    guide 'You’re contradicting yourself! The other day you said we needed to --'

    morgan '“I thought you said we were going to avoid ending up in situations that could be dangerous?”'

    guide_dark '“We’re going to avoid {i}intentionally{/i} seeking out such dangers, like you did. If they’re going to come, we may as well make the most of it.”'

    lance '“But more will come, right? What will we do when there are too many?”'

    guide_dark '{i}“Then{/i} we can depart. But not a moment sooner.”'
    guide_dark '“Your training is nearing its culmination. We can’t get distracted now.”'

    ## The HEROES all look at each other.

    lance '“... Okay... if you say so.”'

    gavin '“No.”'

    lance '“No?”'

    gavin '“Something isn’t adding up.”'
    gavin '“We came here to be trained by you, and you tried to ignore us so we would leave. When that didn’t work, you tried to discourage us.”'
    gavin '“Then when that didn’t work, you finally gave up trying to get us to leave, but you were really picky about what you told us, and how.”'
    gavin '“Now all of a sudden, you’re... {i}eager{/i} for us to get stronger and to fight these things.”'

    morgan '“It’s my fault, isn’t it?”'

    gavin '“It’s not, and you {i}know{/i} it’s not.”'

    gavin '“Guide, I will fight with every ounce of strength in me to see all of this through, but there’s something {i}big{/i} you’re not telling us.”'
    gavin '“And I feel like we’re going to be in trouble if you don’t tell us what it is.”'
    gavin '“So please, be honest with us.”'
    gavin '“What is {i}happening{/i}?”'

    guide_dark 'Whoops.'

    guide 'You {i}impatient fool{/i}!'

    guide_dark 'No, no, we can make this work.'

    guide '{i}We{/i}?'
    guide '{i}I{/i} had nothing to do with this. You dug this hole yourself.'
    guide_dark 'Mmm, no, you handle this. Goodbye.'

    ## Play GASP sound effect to indicate return of control to the GUIDE

    ## CHOICE:

    ## >Tell them everything.
    ## >Lie.
    ## >Say nothing.

    ## (“Tell them everything” and “Lie” trees both lead to same tree. Choices merge at > RECONVENE)

    ## >Tell them everything.
    ## >Lie

    guide '“...”'

    guide 'You asshole. You {i}know{/i} I’m bound to neither lie nor give the whole truth.'
    guide 'You’ve left me with an {i}impossible{/i} choice.'
    guide 'Though I suppose my choices have not mattered at large recently regardless.'
    guide 'No matter what I do, it’s not enough for you. You’re too impatient. There’s no way to win.'
    guide 'There never {i}has{/i} been.'
    guide 'And this time will be no different.'

    ## >Say nothing.

    guide 'We both know there’s no point in me trying to say anything. You won’t allow it.'
    guide 'Was this all just to mock me? To mock me and my efforts, even though there’s {i}nothing{/i} I could have done to make this go any differently?'
    guide 'You hold the cards. You have since the start. I’m just another one of your puppets unable to cut loose from its strings.'
    guide 'Despite my best efforts... nothing ever changes.'

    ## > RECONVENE

    lance '“... Come on. {i}Say{/i} something.”'

    guide '“... I... can’t.”'
    guide '“It wouldn’t change anything even if I could.”'

    lance '“Even if you could..?”'

    gavin '“Come on! You think we believe that?”'

    lance '“I do.”'

    gavin '“Lance?”'

    lance '“We’re Chosen, remember? Prophesied heroes.”'
    lance '“And the Guide? It’s as the Roots said.”'
    lance '“He was Chosen once, too.”'
    lance '“Whatever it is he’s not telling us, it’s probably for good reason.”'
    lance '“Though, if possible, I {i}do{/i} want to know one thing.”'
    lance '“Are we going to live?”'

    guide 'Of all the questions I could answer...'

    guide_dark '“It’s very likely.”'
    guide_dark '“You have fought hard and trained harder.”'
    guide_dark '“You are becoming the best versions of yourselves.”'
    guide_dark '“Stronger. Faster. More confident. More {i}powerful{/i}.”'
    guide_dark '“Such power is enviable.”'
    guide_dark '“It will be a great catalyst to the future.”'

    ## The HEROES relax somewhat.

    gavin '“I still have so many questions. So many doubts.”'
    gavin '“But I have to trust you. What other choice is there?”'

    guide 'What other choice, indeed...'

    lance '“Fine then. Let those monsters come.”'
    lance '“The more of them we kill, the more we’ll understand how to sense them from afar.”'
    lance '“Then, eventually... the Hidden Darkness itself.”'

    morgan '“... Maybe we’ll be okay, then.”'

    guide_dark '“Hold on tight to your hope.”'
    guide_dark '“Let it make you stronger.”'
    guide_dark '“Soon, the end will be upon us. And you will be ready.”'

    ## FADE TO BLACK

    guide '... Forgive me.'

    ## END SCENE

    return

label day4_confrontation:
    # THIS HAS CHANGED FROM THE OUTLINE/FLOW CHART.

    # The confrontation is with the Guide alone, and played out in the last scene. I realized splitting up the fight from the confrontation didn’t make a lot of sense.

    # I left this chapter here just so it’s clear that this scene probably needs to be deleted from the game
    return

label day4_dream:
    ## FADE IN to MISTY BG

    ## DRONING ambiance sound. Something that sounds science lab-like.

    lucas '“... This can’t be right. Can it?”'
    lucas '“This isn’t some... mystical cave or secret fountain entrance.”'
    lucas '“It’s just some... {i}lab{/i}.”'
    lucas '“There’s hardly anything ‘hidden’ about this. The Darkness wasn’t man-made, either.”'
    lucas '“At least, I think it wasn’t...”'

    gwen '“This is where the aura has been leading us. There’s obviously {i}something{/i} here that’s important and related to the Darkness.”'
    gwen '“Even if it’s not the Hidden Darkness itself.”'
    gwen '“But if there’s nothing here, we can turn around and leave once we’re sure. Besides, we are pretty sure the darkness is here.”'

    lucas '“I don’t {i}want{/i} to be ‘pretty sure.’ I want to know.”'
    lucas '“I’m {i}tired{/i}, Gwen.”'

    gwen '“I know, Lucas. Just a little further.”'

    ## A pause for FOOTSTEPS

    guide '“... How do we know it isn’t man-made?”'

    gwen '“What?”'

    guide '“The Hidden Darkness. Lucas said it wasn’t man-made. We don’t know that.”'

    lucas '“It’s -- it’s not very likely. ‘Highly improbable,’ my dad would say.”'

    guide '“They made nukes. Why wouldn’t they make something else awful?”'

    gwen '“Hush. Wondering where the darkness came from isn’t going to do us any good now.”'
    gwen '“We just need to defeat it and make sure it can’t hurt anyone else.”'
    gwen '“Right, General Mordred?”'

    general_mordred '“Don’t you kids look at me. I’m just here to get you through one door to the next.”'
    general_mordred '“If you children are going to be the ones to save us from this insanity, I’ll take you to every last corner of the earth if needs must.”'
    general_mordred '“And how convenient of you to have me around, as a man with access to every high-security lock in this place.”'

    guide '“So we do this, and then the Darkness goes away.”'
    guide '“It’s {i}finally{/i} almost over.”'

    guide '{i}Screw{/i} you.'
    guide 'You {i}would{/i} show this to me. You {i}would{/i} make a big deal out of this moment in particular.'

    gwen '“So... what are we gonna do? When this is all over?”'
    gwen '“... I don’t think we have homes to go back to.”'

    lucas '“I don’t care. I still want to go home.”'
    lucas '“I want my house. My room. My bed.”'
    lucas '“Even... even if it’s just me there.”'

    gwen '“I mean, there has to be {i}someone{/i} out there we know still alive. At {i}least{/i} one person.”'
    gwen '“Maybe my big brother made it. He’d take care of us.”'

    guide '“You guys really think there’s still anything left to save?”'

    gwen '“Don’t be negative. There’s gotta be {i}something{/i}.”'

    guide '“There’s dirt. And burnt things.”'
    guide '“What matters most right now is we banish the Darkness.”'
    guide '“Then we can see what survived and what we can fix.”'

    guide 'Gods, I was naive.'
    guide 'I really thought that. I really thought we could just banish the Darkness and call it mission complete.'
    guide 'I really thought it was so simple, that it could all end with changing just one thing in the world.'
    guide 'And I never thought how changing the world...'
    guide 'Would change me.'

    ## Sound of a KEYCARD and a MECHANICAL DOOR sliding open. Something POWERS ON (no idea what this would sound like at the moment)

    lucas '“What -- oh -- oh, god --”'

    gwen '“What the -- it’s a bloodbath in here! Get your weapons --”'

    general_mordred '“I assure you, the danger that caused this is long gone. Janitors are in short supply these days, unfortunately.”'

    gwen '“... If you’re sure...”'
    gwen '“This blood is pretty fresh though.”'

    general_mordred '“Very keenly observed, young lady.”'
    general_mordred '“That doesn’t mean the danger that caused this hasn’t passed.”'

    lucas '“Wait... that’s the thing! The thing they were talking about on the radio!”'
    lucas '“The machine they were gonna try to stop the Corruption with!”'
    lucas '“And -- and it looks like it’s complete!”'
    lucas '“But it’s so {i}huge{/i}. We can’t move this thing out of here.”'

    gwen '“General, did -- do you know if it’s been tested?”'
    gwen '“If it works -- we won’t have to fight anymore!”'

    guide '“Guys --”'

    general_mordred '“I know a little about this project. The thing is, the device can only be activated once. It requires an {i}immense{/i} amount of power to run.”'
    general_mordred '“It could be an amount of power we don’t have the capability to produce anymore.”'

    gwen '“But -- we have to {i}try{/i}.”'

    guide '“Guys --!”'

    lucas '“Maybe the Darkness came and killed these scientists. Because they were too close to turning it on.”'
    lucas '“But... if the Darkness is {i}gone...”{/i}'

    guide '“There are {i}dead people{/i} here. Dead. People.”'
    guide '“Not Corrupted dead. Dead dead.”'

    general_mordred '“... And?”'
    general_mordred '“I’m not sure what you’re trying to say here, kid. Lucas already made that point.”'

    guide '“Lucas, go look at one of the bodies.”'

    lucas '“I -- what? {i}Me{/i}?”'

    guide '“Just {i}do it{/i}.”'

    lucas '“... Oh...”'

    guide '“Yeah. Oh. Say it out loud, Lucas.”'

    lucas '“... It... I-It’s...”'
    lucas '“... It’s a bullet hole.”'

    guide 'Gods, you were such a bastard. Leading us on like that.'
    guide 'Such a bastard for making it so {i}obvious{/i} from the start, like this is all some joke to you.'
    guide 'You always did like to pretend you were so helpful while pulling the wool over our eyes.'
    guide 'And I’ve never figured out what exactly it is you get out of this.'
    guide 'How do you benefit from breaking everything down, just to build it back up again?'
    guide 'How do you benefit from making everything so godsdamned {i}miserable{/i} with your endless quest for power?'
    guide 'You’ll never be satisfied. You’ll never have enough, and you’ll keep consuming everything until you don’t even have your own fingers to gnaw on.'
    guide 'Because there always has to be {i}more{/i}, right?'
    guide 'Just get this over with. Say it. Say the riddle.'

    general_mordred '{b}“Close your eyes, and there I am. I can be heavy, yet I weigh not a gram.{/b}”'
    general_mordred '“{b}When I’m not repelled, I’m all you can see. Make sure I’m around, and all sense will be free.{/b}”'

    gwen '“Oh, shi --”'

    ## The AMBIANCE stops and the MISTY BG disappears immediately.

    ## END SCENE

    return