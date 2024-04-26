default message_bar_text = ""
default message_bar_text_default = ""
default tooltip_text = ""
default tooltip_text_default = ""
default selected_target = None
default selected_skill = None
default combat_active = True

label combat:
    scene battlefield
    window hide
    show screen debug_pane
    $ message_bar_text = "blank"
    $ message_bar_text_default = ""
    $ set_turn_order()

    label combat_loop:
        $ selected_target = None
        $ selected_skill = None
        $ active_entity = set_active_entity()
        show screen message_bar
        show screen tooltip_pane
        show screen turn_order_pane
        show screen display_enemies
        show screen display_party
        call screen select_skill
        call select_target
        # call apply_effects
        call apply_damage
        # call update_effects
        # call check_for_end
        $ turn = turn + 1
        $ set_turn_order()
        pause 0.25
        if combat_active:
            jump combat_loop
        else:
            return
        
screen debug_pane:
    fixed:
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

screen tooltip_pane:
    frame:
        xpos 1536
        ypos 640
        xsize 384
        ysize 440
        text "[tooltip_text]"

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
            $ active_indicator = "ACTIVE" if e.is_turn else ""
            text "[active_indicator]":
                xpos spacing[i][0] ypos spacing [i][1] - 25
            text "HP: [e.current_hp]/[e.stats['hp']]":
                xpos spacing[i][0] ypos spacing[i][1] + 256
            text "MP: [e.current_mp]/[e.stats['mp']]":
                xpos spacing[i][0] ypos spacing[i][1] + 288
            imagebutton:
                xpos spacing[i][0] ypos spacing[i][1]
                hover im.MatrixColor(e.img, im.matrix.brightness(0.5))
                hovered SetVariable("tooltip_text", e.label)
                unhovered SetVariable("tooltip_text", tooltip_text_default)
                idle e.img
                action Return(e)

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
                hovered SetVariable("tooltip_text", e.label)
                unhovered SetVariable("tooltip_text", tooltip_text_default)
                idle e.img
                action Return(e)

screen select_skill():
    frame:
        xalign 0.0 yalign 1.0
        hbox:
            for s in active_entity.skills:
                imagebutton:
                    hover im.MatrixColor(s.img, im.matrix.brightness(0.5))
                    hovered SetVariable("tooltip_text", s.label)
                    unhovered SetVariable("tooltip_text", tooltip_text_default)
                    idle s.img
                    action SetVariable("selected_skill", s), Return()

label select_target():
    while not selected_target:
        call screen target_select
        $ selected_target = _return
    return

screen target_select():
    pass

label apply_damage():
    $ apply_damage(active_entity, selected_skill, selected_target)
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
