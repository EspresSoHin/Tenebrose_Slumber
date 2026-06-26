### Gallery Menu screen ############################################################
##
## Similar to the game menu screen but for the Image Gallery, Music Room, and Replay
##

############################################################
### GALLERY MENU SCREEN ###
############################################################

screen gallery_menu():
    tag menu
    default curr_screen = "images"

    style_prefix "pref"
    use game_menu("Gallery")

    fixed:
        ## TABS 
        hbox:
            textbutton _("Images"):
                selected curr_screen == "images"
                action SetScreenVariable("curr_screen", "images")

            add "gui/dia_separator.png" yalign 0.5

            textbutton _("Music"):
                selected curr_screen == "music"
                action SetScreenVariable("curr_screen", "music")

        showif curr_screen == "images":
            use gallery()
        showif curr_screen == "music":
            use music_room()

