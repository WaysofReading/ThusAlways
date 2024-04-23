label combat_test:
    scene battlefield
    "COMBAT MODE"
    call screen combat_main

style button_action_category:
    color "#FE3EED"
    hover_color "#D2D2D2"

style frame_combat_menu:
    xpadding 20 ypadding 20

screen combat_main():
    frame:
        style frame_combat_menu
        vbox:
            textbutton "Offense":
                text_style "button_action_category"
                action Show("sub_menu")
            textbutton "Defense"
            textbutton "Support"
            textbutton "Item"

    grid 2 3:
        xspacing 200 yspacing 200
        xycenter (0.5, 0.5)
        
        imagebutton auto "images/gui/button_%s.png" action SetVariable("var", "value")
        imagebutton auto "images/gui/button_%s.png" action SetVariable("var", "value")
        imagebutton auto "images/gui/button_%s.png" action SetVariable("var", "value")

screen sub_menu:
    frame:
        text "hello, world"