### Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

############################################################
### GAME MENU SCREEN ###
############################################################
screen game_menu(title):
    add "gui/menu_background.png"

    style_prefix "game_menu"

    label _(title) 

    ## RETURN ###
    textbutton _("Return"):
        pos (1618, 900)
        action Return()

    



style game_menu_label:
    pos (92, 45)

style game_menu_label_text:
    text_align 0.0

style game_menu_button:
    xysize (267, 155)

    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xoffset=-30)

style game_menu_button_text:
    size 50



screen game_menu_old(title):

    style_prefix "game_menu"


    vbox:
        xpos 60 yalign 0.5
        spacing 6

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and
            ## unnecessary on Android and Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

    textbutton _("Return"):
        style "return_button"
        action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


############################################################
### GAME MENU STYLES ###
############################################################

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width-420
    ysize config.screen_height-200
    align (0.5, 0.5)

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"
