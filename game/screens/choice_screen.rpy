### Choice screen ############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

############################################################
### CHOICE SCREEN ###
############################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

############################################################
### CHOICE STYLES ###
############################################################

style choice_vbox:
    xalign 0.5
    xoffset 80
    ypos 405
    yanchor 0.5
    spacing 10

style choice_button:
    is default # This means it doesn't use the usual button styling
    xysize (1153, 192)
    background "gui/button/choice_[prefix_]background.png"
    insensitive_background Transform("gui/button/choice_idle_background.png", matrixcolor=SaturationMatrix(0.0))
    padding (80, 20)

style choice_button_text:
    is default # This means it doesn't use the usual button text styling
    xalign 0.5 yalign 0.5
    idle_color OFFWHITE
    hover_color GOLD
    insensitive_color GRAY