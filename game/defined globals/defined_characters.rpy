### Defined Characters ############################################################
##
## Defining all the character codes.

############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Python
# 2. Characters
# 3. Misc

############################################################
### PYTHON ###
############################################################
init python:
    _mc = "Y/N"

############################################################
### MAIN CHARACTERS ###
############################################################
define MC = Character("[_mc]", ctc="ctc", ctc_position="fixed")
define narrator = Character(None, ctc="ctc", ctc_position="fixed")

############################################################
### MISC ###
############################################################
# Create a new centered character so that it doesn't use old say_screen
define centered = Character(None, kind=centered, screen='centered_say')
