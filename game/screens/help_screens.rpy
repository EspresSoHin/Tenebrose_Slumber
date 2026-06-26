### Help Screen ############################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.


############################################################
### HELP SCREENS ###
############################################################        

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"))
    fixed:
        ### TABS ###
        hbox:
            style_prefix "pref"

            textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
            add "gui/dia_separator.png" yalign 0.5
            textbutton _("Mouse") action SetScreenVariable("device", "mouse")

            if GamepadExists():
                add "gui/dia_separator.png" yalign 0.5
                textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")


        viewport id "help_vp":
            style_prefix "help"
            mousewheel True draggable True pagekeys True
            

            has vbox
            spacing 23

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

        vbar value YScrollValue("help_vp"):
            xpos 1780
            yalign 0.5
            ysize 680


### KEYBOARD SCREEN ###

screen keyboard_help():

    hbox:
        
        label _("Enter")
        text _("Advances dialogue and activates the interface.")
        

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


### MOUSE SCREEN ###

screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


### GAMEPAD SCREEN ###

screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()
    null height 20

############################################################
### HELP STYLES ###
############################################################
style help_viewport:
    pos (100, 220)
    xsize 1710
    ysize 680

style help_button:
    xmargin 12

style help_label:
    xsize 600
    right_padding 30

style help_label_text:
    size 50
    xalign 1.0
    textalign 1.0

style help_text:
    yalign 0.5

style help_button:

    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xsize=150, fit='contain', xoffset=20, yoffset=-20)

style help_button_text:
    size BTN_TEXT_SIZE2
