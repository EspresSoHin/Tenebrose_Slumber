### Say screen ############################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Say Screens
# 2. Say Styles
# 3. NVL Screens
# 4. NVL Styles
# 5. Bubble Screen
# 6. Bubble Styles

############################################################
### SAY SCREENS ###
############################################################

screen say(who, what):
    style_prefix "say"

    fixed:
        window:
            id "window"
            background Transform(Image("gui/textbox.png", xalign=0.5, yalign=1.0), alpha=persistent.say_window_alpha)

            text what id "what":
                size persistent.dialogue_text_size 
                line_spacing persistent.dialogue_line_spacing
                color gui.text_color

        if who is not None:
            window:
                pos (423, 591)
                id "namebox"
                style "namebox"
                text who id "who"


    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.0 yalign 1.0

# For centered character only or other characters of NONE (Excluding narrator)
screen centered_say(who, what):
    style_prefix "say"
    window:
        id "window"

        text what id "what":
            size persistent.dialogue_text_size 
            line_spacing persistent.dialogue_line_spacing
            color gui.text_color

    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')


############################################################
### SAY STYLES ###
############################################################

# Style for the dialogue window
style window:
    xpos 221
    yalign 1.0

    xysize (1587, 471)
    padding (260, 185, 260, 94)

# Style for the dialogue
style say_dialogue:
    adjust_spacing False
    ypos 0

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xpos 20
    xysize (631, 159)
    background "gui/namebox.png"
    padding (5, 5, 5, 5)

# Style for the text with the speaker's name
style say_label:
    color OFFWHITE
    xpos 80
    yalign 1.0 yoffset -20
    size gui.name_text_size
    font gui.name_text_font


############################################################
### NVL SCREENS ###
############################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing 15

        use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


############################################################
### NVL STYLES ###
############################################################
##
## This controls the maximum number of NVL-mode entries that can be displayed at
## once.

define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 15, 0, 30)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 645 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 225
    min_width 225
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 675
    xanchor 0.0


############################################################
### BUBBLE SCREENS ###
############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what id "what":
            size persistent.dialogue_text_size 
            line_spacing persistent.dialogue_line_spacing
            color gui.text_color


############################################################
### BUBBLE STYLES ###
############################################################

style bubble_window:
    is empty
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    is empty
    xalign 0.5

style bubble_who:
    is default
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    is default
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}
