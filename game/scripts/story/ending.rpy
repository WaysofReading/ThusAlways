label ending_the_truth:
    ## NEW SCENE: The Truth
    ## Sound of FOOTSTEPS. A DRONING AMBIANCE. A KEYCARD. A MECHANICAL DOOR. All the same sounds the player heard in the dream.
    play music foley_lab_ambiance fadein 1.0
    play sound footsteps
    pause 1.0
    play sound keycard_swipe
    play sound science_door
    play sound light_switch
    play music_extra foley_electric_hum volume 0.4

    ## NO bg or characters on screen yet.
    lance "“I’ve never seen a pre-collapse structure this complete before.”"
    lance "“It’s kind of unnerving.”"
    lance "“How long has this place been here for? A decade? A century?”"
    lance "“No, not that long. There’s still power.”"
    gavin "“Lance, please, be quiet.”"
    lance "“I can’t.”"
    lance "“I’m... nervous.”"
    morgan "“Don’t be. We have our Guide with us.”"
    morgan "“He trained us. He’s been with us every step of the way.”"
    morgan "“Everything is going to turn out okay.”"

    ## FADE IN to LABORATORY. There’s some sort of portal device in the background.
    scene lab_1 with fade
    
    ## FADE IN Heroes
    ## SPRITES Gavin A, Morgan N, Lance N
    show gavin annoyed at grouped_center_pos1
    show lance at grouped_center_pos2
    show morgan at grouped_center_pos3
    lance "“What is that?”"
    lance "“I -- nevermind. Looks like this room is a dead end.”"
    lance "“So... where’s the Darkness?”"
    morgan "“Close your eyes and feel for it. If it’s not here, it has to be close.”"

    ## LANCE and MORGAN close their eyes. Gavin doesn’t.
    ## (WILL MAKE these sprite variants if there’s time)
    "show lance eyesclosed\nshow morgan eyesclosed"
    morgan "“... Gavin, I know you’re not doing it.”"
    gavin "“...”"
    gavin "“There’s no point.”"
    gavin "“We already know it’s here.”"

    ## SPRITES Morgan A
    ## MORGAN opens her eyes, annoyed.
    show morgan annoyed
    morgan "“Yeah, but we have to {i}find{/i} it. So we can {i}kill{/i} it? Remember?”"
    gavin "“You guys {i}really{/i} haven’t figured it out, have you?”"

    ## SPRITE Lance A
    ## LANCE opens his eyes.
    show lance annoyed
    lance "“Figure {i}what{/i} out?”"
    guide "“Heroes -- Chosen.”"
    guide "“I need you to tell me something.”"
    guide "“I need you to recite the scripture at the Roots of the World. If you remember it.”"
    lance "“What? Why?”"

    ## The screen begins to shake and pulsate red intermittently as dialogue progresses. I’ll let you decide if this is randomized or dialogue-progression based.
    "Justin's plan: make this part typewriter-style and pulse the screen every X characters (whatever feels right)"
    morgan "“{i}This place is not a place of honor... no highly esteemed deed is commemorated here... nothing valued is here.{/i}”"
    morgan "“{i}What is here was dangerous and repulsive to us. This message is a warning about danger.{/i}”"

    ## SPRITE Lance N
    show lance neutral
    lance "“{i}... The danger is in a particular location... it increases towards a center... the center of danger is here... of a particular size and shape, and below us.{/i}”"
    lance "“{i}The danger is still present, in your time, as it was in ours.{/i}”"
    gavin "“{i}The danger is to the body, and it can kill.{/i}”"
    gavin "“{i}The form of the danger is an emanation of energy.{/i}”"
    guide "“{i}The danger is unleashed only if you substantially disturb this place physically.{/i}”"
    lance "“... So, what? How is that related to us, to here and now?”"
    guide "“It’s one of the few things that has hopped over continuously from world to world.”"
    guide "“As if something is meant to be learned from it... but humans never learn.”"
    guide "“... Admittedly, it’s a coincidence. At least, it was, in the first iteration of the world.”"
    morgan "“... Huh? {i}Worlds{/i}? More than one?”"
    morgan "“That’s not a thing.”"
    guide "“Allow me to break it down -- briefly, for I don’t have long.”"
    guide "“{i}No highly esteemed deed is commemorated here. Nothing valued is here.{/i}”"
    guide "“That is as it says -- but the danger increases towards a center of a particular location. That center is {i}here{/i}.”"
    guide "“It is still present, now, as it was once long ago.”"
    guide "“It is energy. It kills, and can only be unleashed with the proper catalyst.”"
    morgan "“... That {i}does{/i} sound a lot like the Corruption.”"
    morgan "“But what are you saying when you say it’s...”"

    ## SPRITE Morgan UNC
    ## MORGAN’s face becomes afraid
    show morgan uncomfortable
    morgan "“... still here...”"

    ## SPRITE Lance ANG
    ## LANCE is the last person who doesn’t get it.
    show lance angry
    lance "“{i}What{/i} am I missing? Spit it out!”"
    guide "“It’s not -- so simple.”"
    guide "“Everyone has to understand before the truth can be spoken plainly.”"
    guide "“It’s simply the nature of it.”"
    guide_dark "“But I can help things along.”"
    guide_dark "“Close your eyes, and there I am.”"
    guide_dark "“I can be heavy, yet I weigh not a gram.”"
    guide_dark "“When I'm not repelled, I'm all you can see.”"
    guide_dark "“Make sure I'm around, and all sense will be free.”"
    guide_dark "“{i}What am I?{/i}”"
    lance "“...”"

    ## SPRITE Lance SP
    ## LANCE suddenly gets it.
    show lance surprised
    lance "“{i}No.{/i}”"

    ## A BRIGHT FLASH of light indicates the beginning of THE HIDDEN DARKNESS beginning to take over the GUIDE’s body.
    "show screen light_flash"
    guide "Oh, Gods. This is it."
    guide "Breathe. Breathe through it. I didn’t know it would hurt this much."

    ## SPRITE Lance ANG
    show lance angry
    lance "“All this time?!”"
    lance "“Gavin, how long did you know?!”"
    gavin "“Since last night.”"

    ## SPRITE Morgan ANG
    show morgan angry
    morgan "“Last {i}night?!{/i}”"
    morgan "“Why didn’t you say something?!”"

    ## SPRITE Gavin ANG
    show gavin angry
    gavin "“It’s a curse! Don’t you feel it?”"
    gavin "“Or, it {i}was{/i} a curse. It’s broken now that we all know the truth.”"
    gavin "“But I’m not sure if I understand why it happened {i}now{/i} and {i}here{/i}.”"

    ## BRIGHT FLASH
    ## SPRITES Gavin A, Morgan A, Lance A
    "show screen light_flash"
    show gavin annoyed
    show lance annoyed
    show morgan annoyed
    guide "“For the same reason I pushed you all so hard in the last few days.”"

    ## NAME change “Guide (?)” --> “The Hidden Darkness”
    $ guide_dark_name = "The Hidden Darkness"
    guide_dark "“Power. An accumulation of power”"
    guide_dark "“It was always man’s greatest vice -- the endless quest to satiate their need, to gain the world at the cost of their own souls and bodies, and the generations to come.”"
    guide "“A need that never required fulfilling.”"
    guide "“The Darkness exists in a cycle that is as intertwined with the Chosen as roots are with the earth. As love is with hate. As parents with children.”"
    guide "“One cannot exist without the other.”"
    guide_dark "“For now.”"

    ## SPRITE Lance ANG
    show lance angry
    lance "“For {i}now?{/i} What does that --”"
    lance "“Why are we even {i}talking{/i} to you? Get out of the Guide’s body, {i}right now{/i}, or I’ll blast your head right off --”"

    ## SPRITE Gavin ANG
    show gavin angry
    gavin "“Lance, hold it!”"
    gavin "“There’s still a lot we don’t know, and he’s willing to tell us.”"

    ## BRIGHT FLASH
    "show screen light_flash"
    
    ## SPRITES Gavin A, Lance A
    show gavin annoyed
    show lance annoyed
    guide_dark "“I always did think your patience was a weakness. But it serves you well now.”"
    gavin "“I don’t want to hear it from {i}you{/i}.”"
    guide "“The Darkness would be more blunt and to the point... but fine.”"
    guide "“The inability to speak of the Hidden Darkness hiding within me is but a fraction of the curse -- now broken, yes.”"
    guide "“But the curse is so much more than an unspeakable evil.”"
    guide "“The Hidden Darkness is everything I told you it was -- it resides in one person, and grows from their heart to corrupt and eat the power of the world.”"
    guide "“And even if the host is aware of their circumstances, the curse grants immortality, and it prevents the host from taking their own life.”"
    guide "“Only a Chosen hero can kill the host and fight the Hidden Darkness.”"
    guide "“It fuels itself off of hate, scorn, judgment, disappointment, superiority -- all of it. And in turn, it fuels a cycle of selfishness and failure, the same one that has led to the collapse of society.”"
    guide "“Country against country, police against civilians, employer against employee.”"
    guide "“Parent against child.”"
    guide "“Why interact with the lesser beings, except to form them in your image, or the image of society? Why open your heart and mind to the art and work of the next generation?”"
    guide "“Why embrace change, when change means uprooting the old systems that no longer serve the greater good?”"
    guide "“Instead, change is seen as a rebellion against order -- something to be stamped out. Something to be {i}punished{/i}.”"
    guide "“These corrupted thoughts always inevitably lead to the destruction of the world.”"
    guide "“Kings will always succumb to greed and steal everything, even the very air from their subject’s lungs.”"
    guide "“Priests invariably come to shun their followers and distort the vision of their benevolent gods into something hateful.” "
    guide "“Teachers find they have nothing more to teach, and yet cling to the old ways, for those are all they know -- and, in their eyes, all that {i}needs{/i} to be known.”"
    guide "“The institutions passed down to the next generation will always be tainted, because they have been tainted from the beginning.”"
    guide "“Thus always to tyrants.”"

    ## SPRITE Morgan ANG
    show morgan angry
    morgan "“So you tricked us? You trained us just to steal our power too?”"
    guide "“It’s more complicated than that --”"

    ## BRIGHT FLASH, and a scream of pain.
    "show screen light_flash"
    "sound man_scream"

    ## SPRITES Morgan UNC, Lance UNC
    show morgan uncomfortable
    show lance uncomfortable
    guide "“I’m running out of time -- pay attention!”"
    guide "“When I said that the Hidden Darkness is as involved in the cycle as the rest of you, I {i}meant{/i} it.”"
    guide "“It {i}knows{/i} that once the energy of life in the world runs dry, it dies too. Even though it can never stop itself from overconsuming and destroying worlds, it seeks survival just like any creature.”"
    guide "“And so, it allows for one technology to advance unimpeded: multiversal travel. The creation of new worlds.”"
    guide "“Because with new worlds comes new life. New ages of humanity. New power to siphon.”"
    guide "“So, the Darkness survives -- as does humanity.”"

    ## BRIGHT FLASH
    "show screen light_flash"
    guide_dark "“Or...”"
    guide_dark "“Or {i}this{/i} is the cycle where you imbeciles {i}finally{/i} fall, and with your power, I will claim the new world all for myself.”"
    guide_dark "“And so will be born a universe with {i}nothing but{/i} power, an indescribable, incomprehensible hell of chaos, impossible to tell where a soul ends and a star begins.”"
    guide_dark "“Everything will become one, never distinct, never connected -- and I will be its ruler. {i}Forever{/i}.”"

    ## BRIGHT FLASH
    "show screen light_flash"
    guide "“For now, killing the host of The Hidden Darkness is the {i}only{/i} way to anything resembling a victory. Imperfection is survival.”"
    guide "“Our battle -- light against dark -- should be powerful enough to activate the portal in this room, and give humanity their next chance.”"

    ## SPRITE Lance SP
    show lance surprised
    lance "“So it was always going to end like this?”"
    lance "“But -- but the curse should die if you die, too, right?”"

    ## BRIGHT FLASH and another scream of pain.
    "show screen light_flash"
    "sound man_scream"

    ## SPRITE Gavin SD
    show gavin sad
    guide "“I -- I can’t keep it contained any longer.”"
    guide "“I can’t tell you any more.”"
    guide "“One of you -- {i}all{/i} of you --”"
    guide "“{i}Kill{/i} me. Don’t let the Hidden Darkness claim the new world first!”"
    morgan "“There has to be another way!”"
    guide "“Morgan. Lance. Gavin. {i}Kill me --{/i}”"

    ## BRIGHT FLASH fading into black screen
    "show screen light_flash"
    scene backdrop_black
    guide_dark "“Or become {i}kindling{/i} to my endless fire.”"
    
    ## BATTLE with The Hidden Darkness
    "call combat_hidden_darkness"

    ## END SCENE
    call end_scene_fade_to_black
    return

label ending_last_scene:
    ## NEW SCENE: Ending
    ## ART showing the Hidden Darkness jumping hosts to Gavin.
    "Syd: need 'ART showing the Hidden Darkness jumping hosts to Gavin.'"

    ## OPEN PORTAL SFX, Music
    play music bgm_delicate fadein 1.0
    play music_extra foley_portal fadein 1.0
    guide_dark "“So, the cycle continues, this time.”"
    guide_dark "“You will be an intriguing one to see break under the weight of reality, the immutability of man.”"
    guide_dark "“Enjoy your new world...”"
    gavin "(?) It won’t last. Thus, always."

    ## SPRITES Gavin UNC, Morgan UNC, Lance SP
    "Syd: do you want to return to the lab scene or keep the art onscreen for this?"
    show gavin uncomfortable at grouped_center_pos1
    show lance surprised at grouped_center_pos2
    show morgan uncomfortable at grouped_center_pos3
    with dissolve
    morgan "“Gavin!”"

    ## SPRITE Gavin SD
    show gavin sad
    gavin "“I -- I’m fine.”"

    ## SPRITE Morgan ANG
    show morgan angry
    morgan "“No, you’re not! You -- the Darkness --!”"
    gavin "“We were never gonna kill it.”"

    ## SPRITES Morgan ANG, Lance UNC
    show morgan angry
    show lance uncomfortable
    morgan "“That’s {i}not{/i} what I meant.”"
    lance "“That {i}thing{/i} is inside you. You know what that means, right?”"

    ## SPRITE Gavin ANG
    show gavin angry
    gavin "“Of course I do!”"

    ## SPRITE Gavin A
    show gavin annoyed
    gavin "“... I’m sorry... I didn’t mean to snap.”"

    ## SPRITE Gavin SD
    show gavin sad
    gavin "“I sort of figured something like this might happen.”"
    gavin "“If the Guide was Chosen, and he lived with the Darkness inside him for... who {i}knows{/i} how long...”"
    gavin "“Well. He and the Darkness called this a ‘cycle,’ didn’t they?”"

    ## SPRITES Morgan SD, Lance N
    show morgan sad
    show lance neutral

    ## The HEROES fall silent. The portal is still open. The GUIDE lies dead.
    pause 1.5

    ## SPRITE Lance SD
    show lance sad
    lance "“... Could we just not go?”"

    ## SPRITE Morgan SP
    show morgan surprised
    morgan "“What?”"
    lance "“We could stay here. We could destroy this thing. Let this whole mess end.”"
    lance "“The Guide tried for that outcome. He tried to turn us away.”"
    lance "“He tried to warn us, sort of.”"

    ## SPRITE Morgan N
    show morgan neutral
    morgan "“You heard what it said. There won’t be any more life left if we do. It will {i}all{/i} end.”"
    morgan "“And there has to be {i}some{/i} chance the cycle will end in our favor someday.”"

    ## SPRITE Morgan SD
    ## MORGAN gets teary
    show morgan sad
    morgan "“... Right..?”"
    lance "“Is the suffering worth it?”"
    gavin "“It {i}has{/i} to be. Otherwise, we wouldn’t have been here for... at {i}least{/i} three cycles, right?”"
    gavin "“... I don’t think we have a choice {i}not{/i} to go through.”"
    lance "“... I don’t... I don’t want {i}any{/i} part of this.”"
    lance "“But you’re right. We {i}don’t{/i} have a choice.”"

    ## SPRITE Lance A
    show lance annoyed
    lance "“I just... I just wish they’d listened. The people who came before.”"
    lance "“The ones who saw the warning signs and did nothing.”"
    lance "“Because where does that leave us? What does that leave us with?”"

    ## The HEROES stand side by side in front of the portal.
    show gavin at grouped_center_pos1
    show lance at grouped_center_pos2
    show morgan at grouped_center_pos3
    morgan "“He never {i}did{/i} tell us what it was going to look like.”"

    ## SPRITE Gavin A
    show gavin annoyed
    gavin "“Then we’ll have to remember everything we see.”"
    gavin "“And then, we’ll make the best of it while we can. And maybe next time...”"

    ## FADE OUT SPRITES
    hide gavin
    hide lance
    hide morgan
    with dissolve

    ## Art of the heroes walking into the portal. Gavin first, Lance second, Morgan last. Morgan stops and sees a button on the machine that says “Global Alert System.” She hits the button with her fist, then walks through.
    "Syd: need 'Art of the heroes walking into the portal. Gavin first, Lance second, Morgan last. Morgan stops and sees a button on the machine that says “Global Alert System.” She hits the button with her fist, then walks through.'"
    gavin "Maybe next time, things will be different."

    ## FADE OUT music/sxf
    call end_scene_fade_to_black

    ## END
    return

label ending_credits:
    play music bgm_i_am_not_alone fadein 1.0
    "scene end_credits_creator_credits"
    "scene end_credits_assets_used"
    "scene end_credits_sources_consulted"
    return

# label ending_choices:
#     'ENDING - CHOICE TREE'
#     if gavin_score >= 2 and lance_score >= 2 and morgan_score >= 2:
#         call ending_good from _call_ending_good
#     elif gavin_score <= -2 and lance_score <= -2 and morgan_score <= -2:
#         call ending_bad from _call_ending_bad
#     else:
#         call ending_neutral from _call_ending_neutral

#     label ending_good:
#         'ENDING - GOOD'
#         return

#     label ending_neutral:
#         'ENDING - NEUTRAL'
#         return

#     label ending_bad:
#         'ENDING - BAD'
#         return

