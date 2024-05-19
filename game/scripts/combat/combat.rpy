default combat_log = []

default message_bar_text = ""
default tooltip_title = ""
default tooltip_description = ""
default tooltip_detail = ""
default selected_target = None
default selected_skill = None
default combat_active = True
default combat_bypass = False
default shutdown_used = False

default enemies = []
default party_members = []
default combat_entities = []
default turn_order = []
default turn = 0

default skills_sensitive = False

label reinitialize_combat_variables:
    $ combat_log = []

    $ message_bar_text = ""
    $ tooltip_title = ""
    $ tooltip_description = ""
    $ tooltip_detail = ""
    $ selected_target = None
    $ selected_skill = None
    $ combat_active = True
    $ combat_bypass = False
    return

label combat_ui_setup:
    window hide
    $ quick_menu = False
    # For some reason combat still shows the "Skipping..." modal so I'm taking a shotgun approach
    $ config.allow_skipping = False
    $ _skipping = False
    $ renpy.choice_for_skipping()
    $ _rollback = False
    return

label combat_encounter_hermit:
    call combat_ui_setup from _call_combat_ui_setup
    scene cabin_exterior with dissolve
    play music bgm_standing_stones fadein 1.0
    $ create_enemy_group(enemy_hermit, 1)
    jump combat
    return

label combat_encounter_training_dummies:
    call combat_ui_setup from _call_combat_ui_setup_1
    scene cabin_exterior with dissolve
    play music bgm_soulful_crescendo fadein 1.0
    $ create_enemy_group(enemy_training_dummy, 3)
    jump combat
    return

label combat_encounter_training_dummies_enhanced:
    call combat_ui_setup from _call_combat_ui_setup_2
    scene cabin_exterior with dissolve
    play music bgm_soulful_crescendo fadein 1.0
    $ create_enemy_group(enemy_training_dummy_enhanced, 3)
    jump combat
    return

label combat_encounter_corrupted_weak:
    call combat_ui_setup from _call_combat_ui_setup_3
    scene ruined_building_interior with dissolve
    play music bgm_find_the_master fadein 1.0
    $ create_enemy_group(enemy_corrupted_weak, 3)
    jump combat
    return

label combat_encounter_corrupted:
    call combat_ui_setup from _call_combat_ui_setup_4
    scene wasteland_night with dissolve
    play music bgm_frozen_landscape fadein 1.0
    $ create_enemy_group(enemy_corrupted, 3)
    jump combat
    return

label combat_encounter_corrupted_strong_day3_night:
    call combat_ui_setup from _call_combat_ui_setup_5
    scene wasteland_night with dissolve
    play music bgm_ghost_walk fadein 1.0
    $ create_enemy_group(enemy_corrupted_strong, 3)
    jump combat
    return

label combat_encounter_corrupted_strong_day4_combat:
    call combat_ui_setup from _call_combat_ui_setup_6
    scene cabin_exterior with dissolve
    play music bgm_ghost_walk fadein 1.0
    $ create_enemy_group(enemy_corrupted_strong, 3)
    jump combat
    return

label combat_encounter_hidden_darkness:
    call combat_ui_setup from _call_combat_ui_setup_7
    scene lab_combat with dissolve
    play music bgm_cry_of_the_soul fadein 1.0
    $ create_enemy_group(enemy_hidden_darkness, 1)
    jump combat
    return

label combat:
    call reinitialize_combat_variables from _call_reinitialize_combat_variables

    $ create_party_group()
    $ set_combat_entities()
    $ set_turn_order()

    # show screen debug_pane
    show screen message_bar
    show screen tooltip_pane
    # show screen turn_order_pane
    show screen display_enemies
    show screen display_party
    show screen skip_combat_button
    
    label combat_loop:
        $ selected_target = None
        $ selected_skill = None
        $ active_entity = set_active_entity()

        if active_entity.controllable:
            $ skills_sensitive = True
            call screen select_skill
            $ skills_sensitive = False
            call select_target from _call_select_target
        else:
            call enemy_selection from _call_enemy_selection
        
        call apply_skill from _call_apply_skill
        call end_of_combat_check from _call_end_of_combat_check

        if combat_active:
            $ turn = turn + 1
            $ set_turn_order()
            pause 0.25
            jump combat_loop
        else:
            call end_combat from _call_end_combat
        
        label break_combat_loop:
            return

label end_combat:
    $ combat_active = False
    hide screen message_bar
    hide screen tooltip_pane
    hide screen display_enemies
    hide screen display_party
    hide screen skip_combat_button
    stop music fadeout 1.0
    scene backdrop_black with dissolve
    pause 1.0
    jump break_combat_loop
    return

style combat_frame:
    padding gui.frame_borders.padding
    background Frame("images/combat/gui/combat_frame.png", gui.frame_borders, tile=False)

screen skip_combat_button():
    fixed:
        xpos 0
        ypos 0
        imagebutton:
            hover im.MatrixColor("images/combat/gui/button_skip_combat.png", im.matrix.brightness(0.5))
            hovered Function(set_tooltip, None)
            unhovered Function(unset_tooltip)
            idle "images/combat/gui/button_skip_combat.png"
            insensitive "images/combat/gui/button_skip_combat.png"
            action SetVariable("combat_bypass", True), Jump("end_of_combat_check"), SensitiveIf(not combat_bypass)

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
    style_prefix "combat"
    frame:
        xpos 1536
        ypos 440
        xsize 384
        ysize 640
        vbox:
            spacing 15
            text "[tooltip_title]" size 48
            text "[tooltip_description]" size 32
            text "[tooltip_detail]" size 16

screen turn_order_pane():
    style_prefix "combat"
    frame:
        xpos 1356
        ypos 900
        xsize 180
        ysize 180
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
    style_prefix "combat"
    frame:
        xpos 1536
        ypos 0
        xsize 384
        ysize 440
        text "[message_bar_text]" size 20

screen display_enemies():
    fixed:
        xpos 0 ypos 32
        $ spacing = enemy_spacing_patterns[len(enemies)]
        for i, e in enumerate(enemies):
            if e.is_dead:
                continue
            fixed:
                maximum (512, 512)
                if e.is_turn:
                    imagebutton:
                        xpos spacing[i][0] ypos spacing[i][1] - 25
                        idle "images/combat/gui/indicator_active_turn.png"
                
                $ eff_icon_x = 0
                for eff in e.effects:
                    imagebutton:
                        xpos spacing[i][0] + eff_icon_x
                        ypos spacing[i][1] + 480
                        # xpos (spacing[i][0]) ypos spacing[i][1] + eff_icon_y
                        hovered Function(set_tooltip, eff)
                        unhovered Function(unset_tooltip)
                        idle eff.img
                        action NullAction()
                    $ eff_icon_x += 32

                imagebutton:
                    xpos spacing[i][0] ypos spacing[i][1]
                    hover im.MatrixColor(e.img, im.matrix.brightness(0.5))
                    hovered Function(set_tooltip, e)
                    unhovered Function(unset_tooltip)
                    idle e.img
                    action [Return(e), SensitiveIf(renpy.get_screen("target_select"))]
                
                bar style "bar_hp" value AnimatedValue(e.current_hp, e.stats['hp'], delay=0.25):
                    xalign -0.125
                    xpos spacing[i][0] ypos spacing[i][1] + 448
                
                bar style "bar_mp" value AnimatedValue(e.current_mp, e.stats['mp'], delay=0.25):
                    xalign -0.125
                    xpos spacing[i][0] ypos spacing[i][1] + 460
                
screen display_party():
    fixed:
        xpos 0 ypos 640
        $ spacing = party_spacing_patterns[len(party_members)]
        for i, e in enumerate(party_members):
            if e.is_dead:
                continue
            fixed:
                maximum (512, 256)
                if e.is_turn:
                        imagebutton:
                            xpos spacing[i][0] ypos spacing[i][1] - 25
                            idle "images/combat/gui/indicator_active_turn.png"
                
                imagebutton:
                    xpos spacing[i][0] ypos spacing[i][1]
                    hover im.MatrixColor(e.img, im.matrix.brightness(0.5))
                    hovered Function(set_tooltip, e)
                    unhovered Function(unset_tooltip)
                    idle e.img
                    action [Return(e), SensitiveIf(renpy.get_screen("target_select"))]
                
                bar style "bar_hp" value AnimatedValue(e.current_hp, e.stats['hp'], delay=0.25):
                    xanchor 0.0
                    if e.name == "morgan":
                        xpos spacing[i][0] + 160
                        ypos spacing[i][1] + 256
                    else:
                        xpos spacing[i][0]
                        ypos spacing[i][1] + 256
                
                bar style "bar_mp" value AnimatedValue(e.current_mp, e.stats['mp'], delay=0.25):
                    xanchor 0.0
                    if e.name == "morgan":
                        xpos spacing[i][0] + 160
                        ypos spacing[i][1] + 268
                    else:
                        xpos spacing[i][0]
                        ypos spacing[i][1] + 268
                
                $ eff_icon_x = 0
                for eff in e.effects:
                    imagebutton:
                        xanchor 0.0
                        if e.name == "morgan":
                            xpos spacing[i][0] + 160 + eff_icon_x
                            ypos spacing[i][1] + 288
                        else:
                            xpos spacing[i][0] + eff_icon_x
                            ypos spacing[i][1] + 288
                        # xpos (spacing[i][0] - 32) ypos spacing[i][1] + eff_icon_y
                        hovered Function(set_tooltip, eff)
                        unhovered Function(unset_tooltip)
                        idle eff.img
                        action NullAction()
                    $ eff_icon_x += 32

screen select_skill():
    style_prefix "combat"
    frame:
        xalign 0.0 yalign 1.0
        hbox:
            spacing 10
            
            for s in active_entity.skills:
                imagebutton:
                    hover im.MatrixColor(s.img, im.matrix.brightness(0.5))
                    hovered Function(set_tooltip, s)
                    unhovered Function(unset_tooltip)
                    idle s.img
                    insensitive s.img
                    action [SetVariable("selected_skill", s), Return(), SensitiveIf(skills_sensitive)]

label select_target():
    while not selected_target:
        call screen target_select
        $ selected_target = _return
    return

screen target_select():
    pass

label apply_skill():
    $ apply_skill(active_entity, selected_skill, selected_target)
    return

label enemy_selection():
    $ selected_skill = select_random_skill(active_entity)
    $ selected_target = select_random_target(active_entity, selected_skill)
    return

label end_of_combat_check():
    $ living_enemies = [e for e in turn_order if e.side == "enemy" and not e.is_dead]
    $ living_party_members = [e for e in turn_order if e.side == "party" and not e.is_dead]
    
    if combat_bypass:
        $ push_message("YOU WIN!")
        $ level_up(party_gavin)
        $ level_up(party_morgan)
        $ level_up(party_lance)
        $ combat_active = False
        jump end_combat
    elif len(living_enemies) == 0:
        $ push_message("YOU WIN!")
        $ level_up(party_gavin)
        $ level_up(party_morgan)
        $ level_up(party_lance)
        $ combat_active = False
    elif len(living_party_members) == 0:
        $ push_message("YOU LOSE! (But your journey continues anyway)")
        $ combat_active = False
