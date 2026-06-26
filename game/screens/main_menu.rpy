### Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


############################################################
### MAIN MENU SCREEN ###
############################################################

screen main_menu():
    style_prefix "mm"

    ## This ensures that any other menu screen is replaced.
    tag menu

    add BLACK

    vbox:
        xpos 60
        yalign 0.5
        spacing 6

        textbutton _("Start") action Start()

        textbutton _("Load") action ShowMenu("load")
        
        textbutton _("Gallery") action ShowMenu("gallery_menu")

        textbutton _("Settings") action ShowMenu("preferences")

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)

############################################################
### MAIN MENU STYLES ###
############################################################
style mm_button:
    xysize (267, 100)

    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xoffset=-30, yoffset=-30)
    
style mm_button_text:
    size BTN_TEXT_SIZE