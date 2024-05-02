default message_bar_text = ""
default message_bar_text_default = ""
default tooltip_title = ""
default tooltip_title_default = ""
default tooltip_description = ""
default tooltip_description_default = ""
default tooltip_detail = ""
default tooltip_detail_default = ""
default selected_target = None
default selected_skill = None
default combat_active = True

label combat_encounter_hermit:
    play music bgm_frozen_landscape fadein 1.0
    jump combat
    return

label combat_encounter_training_dummies:
    play music bgm_soulful_crescendo fadein 1.0
    jump combat
    return

label combat_encounter_training_dummies_enhanced:
    play music bgm_soulful_crescendo fadein 1.0
    jump combat
    return

label combat_encounter_corrupted_weak:
    play music bgm_find_the_master fadein 1.0
    jump combat
    return

label combat_encounter_corrupted:
    play music bgm_frozen_landscape fadein 1.0
    jump combat
    return

label combat_encounter_corrupted_strong:
    play music bgm_ghost_walk fadein 1.0
    jump combat
    return

label combat_encounter_hidden_darkness:
    play music bgm_cry_of_the_soul fadein 1.0
    jump combat
    return


label combat:
    scene battlefield
    window hide
    show screen debug_pane
    $ message_bar_text = "blank"
    $ message_bar_text_default = ""
    $ populate_groups(enemy_group_training_dummies)
    $ set_turn_order()

    label combat_loop:
        show screen message_bar
        show screen tooltip_pane
        show screen turn_order_pane
        show screen display_enemies
        show screen display_party

        $ selected_target = None
        $ selected_skill = None
        $ active_entity = set_active_entity()

        if active_entity.controllable:
            call screen select_skill
            call select_target
        else:
            call enemy_action
        
        call apply_skill
        # call update_effects
        # call check_for_end
        $ turn = turn + 1
        $ set_turn_order()
        pause 0.25
        if combat_active:
            jump combat_loop
        else:
            return
        
screen debug_pane():
    frame:
        xpos 1536
        ypos 80
        vbox:
            text "ACTIVE: [active_entity.label]"
            text "TURN: [turn]"
            if selected_skill:
                text "SKILL: [selected_skill.label]" textalign 0.0
            else:
                text "SKILL: no skill" textalign 0.0
            
            if selected_target:
                text "TARGET: [selected_target.label]" textalign 0.0
            else:
                text "TARGET: no target" textalign 0.0
            
            textbutton "Reset" action Jump("combat")

screen tooltip_pane():
    frame:
        xpos 1536
        ypos 640
        xsize 384
        ysize 440
        vbox:
            spacing 15
            text "[tooltip_title]"
            text "[tooltip_description]"
            text "[tooltip_detail]"

screen turn_order_pane():
    frame:
        xpos 0
        ypos 128
        xsize 192
        ysize 256
        $ active_idx = turn_order.index(active_entity)
        $ x, y = 0, 0
        text "Turn Order" xpos x ypos y
        $ y += 48
        for e in turn_order:
            $ i = turn_order.index(e)
            if i == active_idx:
                text ">" xpos x ypos y size 16
            text e.label xpos (x + 16) ypos y size 16
            $ y += 16

screen message_bar():
    frame:
        xysize (1920, 80)
        if message_bar_text:
            text "[message_bar_text]"
        else:
            text ""

screen display_enemies():
    fixed:
        xpos 320 ypos 128
        $ spacing = enemy_spacing_patterns[len(enemies)]
        for i, e in enumerate(enemies):
            if e.is_dead:
                continue
            
            fixed:
                maximum (192, 256)
                $ active_indicator = "ACTIVE" if e.is_turn else ""
                if e.is_turn:
                    imagebutton:
                        xpos spacing[i][0] ypos spacing[i][1] - 25
                        idle "images/combat/gui/indicator_active_turn.png"
                $ eff_icon_y = 0
                for eff in e.effects:
                    imagebutton:
                        xpos (spacing[i][0] - 32) ypos spacing[i][1] + eff_icon_y
                        hovered SetVariable("tooltip_title", eff.label)
                        unhovered SetVariable("tooltip_title", tooltip_title_default)
                        idle eff.img
                        action NullAction()
                    $ eff_icon_y += 32

                imagebutton:
                    xpos spacing[i][0] ypos spacing[i][1]
                    hover im.MatrixColor(e.img, im.matrix.brightness(0.5))
                    hovered SetVariable("tooltip_title", e.label)
                    unhovered SetVariable("tooltip_title", tooltip_title_default)
                    idle e.img
                    action Return(e)
                bar style "bar_hp" value AnimatedValue(e.current_hp, e.stats['hp'], delay=0.25):
                    xanchor 0.0
                    xpos spacing[i][0] ypos spacing[i][1] + 256
                $ hp_str = "HP: {:.0f}/{:.0f}".format(e.current_hp, e.stats['hp'])
                text hp_str:
                    xpos spacing[i][0] ypos spacing[i][1] + 248
                $ mp_str = "MP: {:.0f}/{:.0f}".format(e.current_mp, e.stats['mp'])
                bar style "bar_mp" value AnimatedValue(e.current_mp, e.stats['mp'], delay=0.25):
                    xanchor 0.0
                    xpos spacing[i][0] ypos spacing[i][1] + 288
                text mp_str:
                    xpos spacing[i][0] ypos spacing[i][1] + 280
                

screen display_party():
    fixed:
        xpos 448 ypos 582
        $ spacing = party_spacing_patterns[len(party_members)]
        for i, e in enumerate(party_members):
            if e.is_dead:
                continue
            $ active_indicator = "ACTIVE" if e.is_turn else ""
            text "[active_indicator]":
                xpos spacing[i][0] ypos spacing [i][1] - 25
            text "HP: [e.current_hp]/[e.stats['hp']]":
                xpos spacing[i][0] ypos spacing[i][1] + 300
            text "MP: [e.current_mp]/[e.stats['mp']]":
                xpos spacing[i][0] ypos spacing[i][1] + 332
            imagebutton:
                xpos spacing[i][0] ypos spacing[i][1]
                hover im.MatrixColor(e.img, im.matrix.brightness(0.5))
                hovered SetVariable("tooltip_title", e.label)
                unhovered SetVariable("tooltip_title", tooltip_title_default)
                idle e.img
                action Return(e)

screen select_skill():
    frame:
        xalign 0.0 yalign 1.0
        hbox:
            for s in active_entity.skills:
                imagebutton:
                    hover im.MatrixColor(s.img, im.matrix.brightness(0.5))
                    hovered SetVariable("tooltip_title", s.label)
                    unhovered SetVariable("tooltip_title", tooltip_title_default)
                    idle s.img
                    action SetVariable("selected_skill", s), Return()

label select_target():
    while not selected_target:
        call screen target_select
        $ selected_target = _return
    return

screen target_select():
    pass

label apply_skill():
    $ m = apply_skill(active_entity, selected_skill, selected_target)
    $ message_bar_text = m
    return

label check_if_done():
    if len([e for e in enemies if not e.is_dead]) == 0:
        $ combat_active = False
        $ message_bar_text = "You Win"
        return
    elif len([p for p in party_members if not p.is_dead]) == 0:
        $ combat_active = False
        $ message_bar_text = "You Lose"
        return
    else:
        return
