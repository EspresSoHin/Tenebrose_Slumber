### Preferences screen ############################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences


############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Preference Screen
# 2. Preference Styles

############################################################
### PYTHON ###
############################################################
init python:
    def reset_volume():
        preferences.set_mixer("voice", 0.5)
        preferences.set_mixer("sfx", 0.5)
        preferences.set_mixer("music", 0.5)
        

############################################################
### PREFERENCE SCREEN ###
############################################################
screen preferences():

    tag menu

    default curr_screen = "general"

    style_prefix "pref"


    use game_menu(_("Settings"))

    fixed:
        ## TABS 
        hbox:
            textbutton _("General"):
                selected curr_screen == "general"
                action SetScreenVariable("curr_screen", "general")

            add "gui/dia_separator.png" yalign 0.5

            textbutton _("Sound"):
                selected curr_screen == "sound"
                action SetScreenVariable("curr_screen", "sound")

            add "gui/dia_separator.png" yalign 0.5

            textbutton _("Dialogue"):
                selected curr_screen == "dialogue"
                action SetScreenVariable("curr_screen", "dialogue")


            
        showif curr_screen == "general":
            use pref_general()
        showif curr_screen == "sound":
            use pref_sound()
        showif curr_screen == "dialogue":
            use pref_dialogue()

############################################################
### PREFERENCE - GENERAL SCREEN ###
############################################################
screen pref_general():
    style_prefix "pref2"

    vbox:
        at ts_screenYEnter()

        ### DISPLAY ##

        hbox:
            label _("Display")

            hbox:
                xsize 655
                yalign 0.5
                xalign 1.0
                
                # toggle arrows
                imagebutton auto "gui/button/btn_left_arrow2_%s.png":
                    action Preference("display", "toggle")

                frame:
                    background None
                    xsize 500
                    text ("FULLSCREEN" if preferences.fullscreen else "WINDOW") align (0.5, 0.5)

                imagebutton auto "gui/button/btn_right_arrow2_%s.png":
                    action Preference("display", "toggle")


        ### SKIP ##

        hbox:
            label _("Skip: Unseen")
            hbox:
                xsize 655
                yalign 0.5
                xalign 1.0
                
                # toggle arrows
                imagebutton auto "gui/button/btn_left_arrow2_%s.png":
                    action Preference("skip", "toggle")

                frame:
                    background None
                    xsize 500
                    text ("ON" if preferences.skip_unseen else "OFF") align (0.5, 0.5)

                imagebutton auto "gui/button/btn_right_arrow2_%s.png":
                    action Preference("skip", "toggle")

        hbox:
            label _("Skip: After Choices")
            hbox:
                xsize 655
                yalign 0.5
                xalign 1.0
                
                # toggle arrows
                imagebutton auto "gui/button/btn_left_arrow2_%s.png":
                    action Preference("after choices", "toggle")

                frame:
                    background None
                    xsize 500
                    text ("ON" if preferences.skip_after_choices else "OFF") align (0.5, 0.5)

                imagebutton auto "gui/button/btn_right_arrow2_%s.png":
                    action Preference("after choices", "toggle")

        hbox:
            label _("Skip: Transition")
            hbox:
                xsize 655
                yalign 0.5
                xalign 1.0
                
                # toggle arrows
                imagebutton auto "gui/button/btn_left_arrow2_%s.png":
                    action Preference("transitions", "toggle")

                frame:
                    background None
                    xsize 500
                    text ("ON" if preferences.transitions != 2 else "OFF") align (0.5, 0.5)

                imagebutton auto "gui/button/btn_right_arrow2_%s.png":
                    action Preference("transitions", "toggle")

        ### AUTO DELAY ###
        hbox:
            label _("Auto Delay Time")
            hbox:
                xsize 655
                yalign 0.5
                xalign 1.0

                bar value Preference("auto-forward time") alt "Change auto-delay time" align (1.0, 0.5) style "bar"

    textbutton _("Revert All"):
        style_prefix "game_menu"
        pos (1200, 900)
        selected False

        action [Preference("display", "window"),
            Preference("skip", "seen"),
            Preference("after choices", "stop"),
            Preference("transitions", "all"),
            Preference("auto-forward time", 15)]

screen pref_sound():
    style_prefix "pref2"

    ### MUSIC ##
    vbox:

        hbox:
            if config.has_music:
                label _("Music")

                hbox:
                    xsize 655
                    yalign 0.5
                    xalign 1.0
                    

                    bar value Preference("music volume") alt "Change music volume" align (1.0, 0.5) style "bar"


        ### SOUND ###
        hbox:
            if config.has_sound:
                label _("Sound")

                hbox:
                    xsize 655
                    yalign 0.5
                    xalign 1.0
                    

                    bar value Preference("sound volume") alt "Sound volume" align (1.0, 0.5) style "bar"
                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound) alt "Test sound"


        ### VOICE ###
        hbox:
            if config.has_voice:
                label _("Voice Volume")
                hbox:
                    xsize 655
                    yalign 0.5
                    xalign 1.0

                    bar value Preference("voice volume") alt "Voice Volume" align (1.0, 0.5) style "bar"
                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

        ### MUTE ALL ##
        hbox:
            if config.has_music or config.has_sound or config.has_voice:
                label _("Mute All")
                hbox:
                    xsize 655
                    yalign 0.5
                    xalign 1.0

                    # toggle arrows
                    imagebutton auto "gui/button/btn_left_arrow2_%s.png":
                        action Preference("all mute", "toggle")

                    frame:
                        background None
                        xsize 500
                        text ("ON" if preferences.get_mute('main') else "OFF") align (0.5, 0.5)

                    imagebutton auto "gui/button/btn_right_arrow2_%s.png":
                        action Preference("all mute", "toggle")


    textbutton _("Revert All"):
        style_prefix "game_menu"
        pos (1200, 900)
        selected False

        action Function(reset_volume), Preference("all mute", "disable")
                

screen pref_dialogue():
    style_prefix "pref2"

    vbox:
        ### TYPEFACE ##
        default typefaces = [CRIMSON, ATKINSON, DEJAVU]
        default curr_num = typefaces.index(gui.text_font) if gui.text_font in typefaces else 0

        hbox:
            label _("Typeface")

            hbox:
                xsize 655
                yalign 0.5
                xalign 1.0

                imagebutton auto "gui/button/btn_left_arrow2_%s.png":
                        action [
                            SetScreenVariable("curr_num", (curr_num - 1) % len(typefaces)),
                            gui.SetPreference("font", typefaces[(curr_num - 1) % len(typefaces)]),
                            gui.SetPreference("name_font", typefaces[(curr_num - 1) % len(typefaces)])
                        ]

                frame:
                    background None
                    xsize 500
                    ysize 100
                    text ("{font=fonts/CrimsonText-Regular.ttf}Crimson{/font}" if curr_num == 0 else
                        "Atkinson-Hyperlegible" if curr_num == 1 else
                        "DejaVuSans") align (0.5, 0.5) font typefaces[curr_num] size (40 if curr_num == 1 else 60)

                imagebutton auto "gui/button/btn_right_arrow2_%s.png":
                    action [
                        SetScreenVariable("curr_num", (curr_num + 1) % len(typefaces)),
                        gui.SetPreference("font", typefaces[(curr_num + 1) % len(typefaces)]),
                        gui.SetPreference("name_font", typefaces[(curr_num + 1) % len(typefaces)])
                    ]


        ### TEXT SIZE ###
        hbox:
            label _("Dialogue Size")

            hbox:
                xsize 500
                yalign 0.5
                xalign 1.0

                bar value FieldValue(persistent, "dialogue_text_size", style="slider", step=5, min=25, max=45) alt "Change dialogue text size" xsize 655 align (1.0, 0.5) style "bar"


        ### TEXT LINE SPACING ###
        hbox:
            label _("Dialogue Line Spacing")

            hbox:
                xsize 500
                yalign 0.5
                xalign 1.0
                
                bar value FieldValue(persistent, "dialogue_line_spacing", style="bar", max_is_zero=False, step=0.5, min=2, max=50) alt "Change dialogue line spacing" align (1.0, 0.5)


        ### TEXT SPEED ###
        hbox:
            label _("Dialogue Speed")

            hbox:
                xsize 500
                yalign 0.5
                xalign 1.0
            
                bar value Preference("text speed") alt "Change dialogue text speed" align (1.0, 0.5) style "bar"



        ### TEXTBOX OPACITY ###
        hbox:
            label _("Dialogue Box Opacity")

            hbox:
                xsize 500
                yalign 0.5
                xalign 1.0


                bar value FieldValue(persistent, "say_window_alpha", 1.0, max_is_zero=False, offset=0, step=.2) alt "Change textbox opacity" align (1.0, 0.5) style "bar"

    textbutton _("Revert All"):
        style_prefix "game_menu"
        pos (1200, 900)
        selected False

        action [SetLocalVariable("curr_num", 0),
            gui.SetPreference("font", CRIMSON),
            gui.SetPreference("name_font", CRIMSON),
            SetVariable("persistent.dialogue_text_size", 33),
            SetVariable("persistent.dialogue_line_spacing", 2),
            Preference("text speed", 0),
            SetVariable("persistent.say_window_alpha", 1.0)]
            

############################################################
### PREFERENCE STYLES ###
############################################################
style pref_hbox:
    pos (825, 30)
    spacing 20

style pref_button:
    xysize (275, 149)
    align (0.5, 0.5)

    idle_background None
    hover_background "gui/button/btn_tab_selected.png"
    selected_background "gui/button/btn_tab_selected.png"

style pref_button_text:
    size BTN_TEXT_SIZE
    align (0.5, 0.5)



############################################################
### PREFERENCE 2 STYLES ###
############################################################
style pref2_vbox:
    yminimum 200
    ymaximum 686
    xsize 1710
    pos (100, 220)
    spacing 3

style pref2_hbox:
    xysize (1710, 100)

style pref2_label_text:
    size 50

style pref2_text:
    font CRIMSON
    size 50




