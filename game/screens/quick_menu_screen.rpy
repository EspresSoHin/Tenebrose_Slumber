### Quick menu screen ############################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

############################################################
### QUICK MENU SCREEN ###
############################################################

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            imagebutton auto "gui/quick menu/btn_back_%s.png" action Rollback()
            imagebutton auto "gui/quick menu/btn_auto_%s.png" action Preference("auto-forward", "toggle")
            imagebutton auto "gui/quick menu/btn_skip_%s.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/quick menu/btn_log_%s.png" action ShowMenu('history')
            imagebutton auto "gui/quick menu/btn_pause_%s.png" action ShowMenu('pause_menu')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")


############################################################
### QUICK MENU STYLES ###
############################################################


style quick_hbox:
    spacing 10
    pos (1300, 25)

