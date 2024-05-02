label day0_guide_backstory:
    ## NEW SCENE: Intro Dream
    ## FADE IN to blank/black screen
    scene backdrop_black with fade
    play music bgm_solemn fadein 1.0

    guide "... I’m tired."

    ## FADE IN to misty screen, FADE IN music/ambiance; there’s no defined environment
    scene backdrop_mist with fade

    guide "I’m tired."
    guide "I sleep, I dream; but in dreams, I find no rest."
    guide "No solitude."
    guide "No quiet."
    guide "When I dream, I dream of the beginning of this world. I dream of chaos unfolding and blooming into order, death into life, hope into reality."
    guide "I dream of that foggy, half-solid air that cloyed thick in our lungs, before it rushed out from us as we took our first tentative steps into the misty and primordial unknown."
    guide "I remember how the grass sprung up. I remember how the trees shot skyward, almost too tall for their own survival. I remember the flooding streams, the exploding rocks."
    guide "The mountains erupted from the earth as if molten magma bursting from a glass beaker, the oceans were a tumultuous roar that flooded both vast deserts and our ears, and the forests called to us with the same promise as any great city."
    guide "I remember the beginning of this world."
    guide "I remember how my allies and I looked at each other, and smiled..."
    guide "Even in the wake of everything we’d left behind to get here."
    guide "..."
    guide "I remember how we thought, “This time, things will be different.”"
    guide "I dream of that promise we made, even though we knew we wouldn’t keep it."
    guide "How could we, when we knew we had brought with us the same seed of destruction that annihilated the last world?"
    guide "It still grows and festers even now, with hardly anything left to feed on."
    guide "And it will keep feeding on the scraps of existence until nothing remains."
    guide "So I dream of the beginning of this world, and its end."

    ## FADE OUT to black
    scene backdrop_black with fade
    
    guide "It’s not the only thing I dream of."
    guide "I wish it was."

    ## FADE IN to a silhouette shot of three heroes. Their ages are indiscernible.
    scene backdrop_white with fade
    show gavin at linedup_center_pos1
    show lance at linedup_center_pos2
    show morgan at linedup_center_pos3
    with dissolve

    guide "I dream of three heroes, heroes I don’t recognize. I don’t know who they are, or what they look like. All I know is that they are chosen."
    guide "For what?"
    guide "Why do I ask? I know what for."
    guide "They come to me, and they tell me, “We are Chosen. We are the heroes of destiny. We are the heroes who will save the world.”"
    guide "“We are the heroes who will banish the evil that plagues the planet, and live to tell the tale.”"
    guide "..."
    guide "They come to me, and know not who I am."
    guide "They come to me, and know not what they promise."

    ## FADE OUT to black.
    scene backdrop_black
    with fade

    guide "... I pray I never see them."
    
    ## FADE OUT music/ambiance
    call end_scene_fade_to_black

    ## END SCENE
    return