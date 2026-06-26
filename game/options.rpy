### Options ############################################################
## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## TODO: Change the config.name, build.name, and config.save_directory to something unique
## Change these top three values (config.name, build.name, and
## config.save_directory) to something unique for your project!

############################################################
## BASICS ######################################################################
############################################################


## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("GUI Vampire Blood")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "GUIVampireBlood"

############################################################
## SAVE DIRECTORY ##############################################################
############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

## Note: a typical save_directory value looks like "FreshProject-1671818013"
define config.save_directory = "GUIVampireBlood-1754094805"


## The version of the game.

define config.version = "1.0"


############################################################
### SOUNDS AND MUSIC ###
############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

# define config.main_menu_music = "main-menu-theme.ogg"


############################################################
### TRANSITIONS ###
############################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None

############################################################
### WINDOW MANAGEMENT ###
############################################################
## https://www.renpy.org/doc/html/config.html#var-config.window_auto_show This
## controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "hide"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


############################################################
### PREFERENCES DEFAULTS ###
############################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15

############################################################
### ICON ###
############################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"

############################################################
### CUSTOM OPTIONS ###
############################################################
##
## Config variables that I like to have set up.

## Convenience for not crashing on grids without enough items https://
## www.renpy.org/doc/html/config.html#var-config.allow_underfull_grids In modern
## Ren'Py, this is already the default.
define config.allow_underfull_grids = True

## Default volume % for the various volume sliders https://www.renpy.org/doc/html/preferences.html#audio-channel-defaults
define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5
define config.default_voice_volume = 0.5

## Optional; this reverts the behaviour of the volume sliders back to pre-8.1,
## so muting the game shows the volume sliders all at 0
# define config.preserve_volume_when_muted = False

## The number of auto save slots Ren'Py will save to before it starts
## overwriting the first one
define config.autosave_slots = 6
## Same thing, but for quick save
define config.quicksave_slots = 6

############################################################
### BUILD CONFIGURATIONS ###
############################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('game/cache/**', None)
    ## NOTE: This excludes markdown and txt files. If you use these formats for
    ## README or instructions, you may want to remove these lines.
    build.classify('**.txt', None)
    build.classify('**.md', None)

    ## To archive files, classify them as 'archive'.

    build.classify("game/**.rpy", "archive")
    build.classify("game/**.rpym", "archive")

    build.classify("game/**.webp", "archive")
    build.classify("game/**.webm", "archive")
    build.classify("game/**.mp4", "archive")
    build.classify("game/**.png", "archive")
    build.classify("game/**.jpg", "archive")
    build.classify("game/**.ttf", "archive")
    build.classify("game/**.otf", "archive")
    build.classify("game/**.mp3", "archive")
    build.classify("game/**.wav", "archive")
    build.classify("game/**.ogg", "archive")
    build.classify("game/**.opus", "archive")
    build.classify("game/**.rpyc", "archive")
    build.classify("game/**.rpymc", "archive")

## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
