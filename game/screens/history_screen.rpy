### History screen ##############################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html


############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Default/Define
# 2. History Screen
# 3. History Styles

############################################################
### DEFAULT/DEFINE ###
############################################################

define config.history_length = 250

############################################################
### HISTORY SCREEN ###
############################################################

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False


    use game_menu(_("History"))

    style_prefix "history"

    fixed:

        viewport id "history_vp":
            mousewheel True draggable True pagekeys True
            scrollbars None yinitial 1.0

            has vbox


            for h in _history_list:

                frame:
                    has hbox
                    if h.who:
                        label h.who style 'history_name':
                            substitute False
                            ## Take the color of the who text
                            ## from the Character, if set
                            if "color" in h.who_args:
                                text_color h.who_args["color"]
                            xsize 200   # this number and the null width
                                        # number should be the same
                    else:
                        null width 200

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

            if not _history_list:
                label _("The dialogue history is empty.")

        vbar value YScrollValue("history_vp"):
            xpos 1780
            yalign 0.5
            ysize 680


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

############################################################
### HISTORY STYLES ###
############################################################

style history_viewport:
    pos (100, 220)
    xsize 1710
    ysize 680

style history_frame:
    xsize 1400
    ysize None
    background None

style history_hbox:
    spacing 20

style history_vbox:
    spacing 20

style history_name:
    xalign 1.0

style history_name_text:
    textalign 1.0
    align (1.0, 0.0)
    color '#f93c3e'

style history_text:
    textalign 0.0

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
