### GUI Transitions ############################################################
##
## A list of defined transitions to make it easier to use.
## Mainly for GUI & Screens
##


############################################################
### EXIT/ENTER ###
############################################################
transform ts_screenYEnter():
    on appear:
        yoffset 50
        alpha 0.2
        linear 0.7 alpha 1.0 yoffset 0

