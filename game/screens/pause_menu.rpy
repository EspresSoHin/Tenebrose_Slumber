### Pause Menu screen ############################################################
##
## Pause menu to replace default save menu
##

############################################################
### PAUSE MENU SCREEN ###
############################################################
screen pause_menu():
    tag menu
    
    add "gui/menu_backround.png"

    style_prefix "pause_menu"

    use game_menu("Pause")

    vbox:
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Gallery") action ShowMenu("gallery_menu")
        textbutton _("Settings") action ShowMenu("preferences")
        textbutton _("Title") action MainMenu()
        textbutton _("Quit") action Quit(confirm=True)


############################################################
### PAUSE MENU STYLES ###
############################################################
style pause_menu_vbox:
    
    spacing 5
    yalign 0.5
    xpos 80

style pause_menu_button:
    xysize (267, 100)

    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xoffset=-30, yoffset=-30)

style pause_menu_button_text:
    size BTN_TEXT_SIZE2