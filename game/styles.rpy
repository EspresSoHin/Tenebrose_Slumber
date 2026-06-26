### Styles ############################################################
##
## A list of all default styles including a lisst of predefined colors and GUI images.
##

############################################################
### TABLE OF CONTENTS ###
############################################################
# Python
# Initialization
# Dialogue Options
# Interface Options
# Localization
# Default Styles
# Bar Styles

############################################################
### PYTHON ###
############################################################

init python early:
    ## COLORS
    BLACK = "#000000"
    GRAY = "#7E7E7E"
    OFFWHITE = "#D8D8D8"
    WHITE = "#FFFFFF"

    CREAM = "#FFFDD0"
    GOLD = "#E4CDA6"
    RED = "#C01A14"

    BTN_IDLE_COLOR = "#FFFFFF"
    BTN_HOVER_COLOR = "#FFFFFF"
    BTN_SELECTED_COLOR = "#C01A14"
    BTN_INSENSITIVE_COLOR = "#8888887f"


    LABEL_COLOR = "#FFFF"
    HYPERLINK_COLOR = "#E4CDA6"

    ## SIZE
    LABEL_TEXT_SIZE = 100
    BTN_TEXT_SIZE = 50
    BTN_TEXT_SIZE2 = 40


    ## FONTS
    DEJAVU = "DejaVuSans.ttf"
    ATKINSON = "fonts/Atkinson-Hyperlegible-Regular-102.otf"
    CRIMSON = "fonts/CrimsonText-Regular.ttf"
    CRIMSONBOLD = "fonts/CrimsonText-Bold.ttf"

    


############################################################
### INITIALIZATION ###
############################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

    # Override default 'ESC' so it shows our custom pause menu instead.
    # By default "game_menu" calls ShowMenu() and the default argument to which
    # screen is shown is the _game_menu_screen which opens save screen
    # https://www.renpy.org/doc/html/store_variables.html#var-_game_menu_screen
    _game_menu_screen = "pause_menu"

define config.check_conflicting_properties = True


############################################################
### IMAGES ###
############################################################
image ctc:
    pos (1473, 920)
    yoffset 0
    "gui/ctc_icon.png"

    linear 0.7 yoffset 20
    linear 0.7 yoffset 0
    repeat



############################################################
### GUI CONFIGURATION VARIABLES ###
############################################################
## Some choice gui values have been left in, to make them
## easier to adjust for accessibility purposes e.g. to allow
## players to change the default text font or size by rebuilding the gui.
## You may add more back if you need to adjust them, or find-and-replace
## any instances where they are used directly with their value.


############################################################
### DIALOGUE OPTIONS ###
############################################################
# https://www.renpy.org/doc/html/gui_advanced.html#gui.preference

# Dialogue quick menu
default quick_menu = True

# Textbox Opacity
default persistent.say_window_alpha = 1.0

# The text font for dialogue and choice menus
define gui.text_font = gui.preference("font", CRIMSON)

# This is only needed if you have set text sizes instead of a slider
# default persistent.typeface = "DejaVuSans"

# Dialogue Text Size
default persistent.dialogue_text_size = 33


# Dialogue Line Spacing
default persistent.dialogue_line_spacing = 2

# Dialogue Text Color
define gui.text_color = gui.preference('color', OFFWHITE)

# The font for character names
define gui.name_text_font = gui.preference("name_font", CRIMSON)

# The size for character names
define gui.name_text_size = gui.preference("name_size", 45)


############################################################
### INTERFACE OPTIONS ###
############################################################
# The text font for buttons
define gui.interface_text_font = gui.preference("interface_font", CRIMSON)

# The default size of in-game text
# This includes the Textbuttons, input prompt, menus, etc
define gui.text_size =  gui.preference("size", 30)



############################################################
### LOCALIZATION ###
############################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


############################################################
### STYLE INITIALIZATION ###
############################################################

init offset = -1

############################################################
### DEFAULT STYLES ###
############################################################
style fixed:
    xysize (1920, 1080)

style default:
    font gui.text_font
    size gui.text_size
    language gui.language

style input:
    adjust_spacing False

style hyperlink_text:
    hover_underline True
    color HYPERLINK_COLOR

style gui_text:
    color WHITE
    size gui.text_size
    font gui.interface_text_font

style button:
    xysize (None, None)
    padding (0, 0)

style button_text:
    is gui_text
    yalign 0.5
    xalign 0.0
    ## The color used for a text button when it is neither selected nor hovered.
    idle_color BTN_IDLE_COLOR
    ## The color that is used for buttons and bars that are hovered.
    hover_color BTN_HOVER_COLOR
    ## The color used for a text button when it is selected but not focused. A
    ## button is selected if it is the current screen or preference value.
    selected_color BTN_SELECTED_COLOR
    ## The color used for a text button when it cannot be selected.
    insensitive_color BTN_INSENSITIVE_COLOR

style label_text:
    is gui_text
    size LABEL_TEXT_SIZE
    color LABEL_COLOR

############################################################
### BAR STYLES ###
############################################################
##
## https://www.renpy.org/doc/html/style_properties.html#bar-style-properties
##
## Some interesting ones include the gutter(bar scroll limits) property.
style bar:
    ysize 32
    xsize 655
    left_bar Frame("gui/bar/left.png", 6, 6, 6, 6, tile=False)
    right_bar Frame("gui/bar/right.png", 6, 6, 6, 6, tile=False)

style vbar:
    xsize 32
    top_bar Frame("gui/bar/top.png", 6, 6, 6, 6, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6, tile=False)

style scrollbar:
    ysize 45
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/scrollbar/horizontal_[prefix_]thumb.png"
    unscrollable 'hide'
    thumb_offset -5

style vscrollbar:
    xsize 45
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/scrollbar/vertical_[prefix_]thumb.png"
    unscrollable 'hide'
    thumb_offset -5

style slider:
    ysize 45
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
    thumb_offset -5

style vslider:
    xsize 45
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    thumb_offset -5


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)
