### Input screen ############################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input


############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Default/Define
# 2. Input Screen
# 3. Input Styles
# 4. Name Input Screen

############################################################
## DEFAULT/DEFINE ###
############################################################


############################################################
## INPUT SCREEN ##
############################################################

screen input(prompt):
    style_prefix "input"

    window:
        # This makes the background the same as the ADV dialogue box

        vbox:
            xanchor 0.0 ypos 20 spacing 10
            text prompt style "input_prompt"
            input id "input"


############################################################
## INPUT STYLES ###
############################################################

style input_prompt:
    xalign 0.0

style input:
    xalign 0.0
    xmaximum 1116

style input_button:
    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xsize=150, fit='contain', offset=(-20, -20))


############################################################
### NAME INPUT SCREEN ###
############################################################
##
## Custom name input screen different from regular input.
screen name_input():
    style_prefix "input"
    ## TODO: Change variable_here to input the variable of the character you want to change
    ## For example: VariableInputValue("_mc", returnable=False)
    
    add "popup_bg" align (0.5, 0.5)
    

    label _("Enter your name:") xalign 0.5 ypos 300 text_size 50

    vbox:
        align (0.5, 0.5)
        spacing 80

        frame:
            background GRAY
            xysize (500, 80)


            ## returnable = False; can't press ENTER to forward
            ## Remove it if you would like to have player use 'ENTER' key
            input value VariableInputValue("_mc", returnable=False):
                id "input"
                align (0.5, 0.5)
                length 12

        textbutton _("Done"):
            align (0.5, 0.5)
            action Confirm("Confirm [_mc] as name?", yes=Return(), no=Hide())


        

