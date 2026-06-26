### Load and Save screens ############################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Default/Define
# 2. Save Screen
# 3. Save Styles
# 4. Load Screen
# 5. Load Styles
# 6. File Slots Screen
# 7. Save/Load Styles

init python:
    def format_runtime():
        total_seconds = int(renpy.get_game_runtime())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

############################################################
## DEFAULT/DEFINE ###
############################################################

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 674
define config.thumbnail_height = 425


############################################################
## SAVE SCREEN ###
############################################################

screen save():

    tag menu


    use file_slots(_("Save"))


############################################################
### LOAD SCREEN ###
############################################################

screen load():

    tag menu


    use file_slots(_("Load"))

############################################################
### FILE SLOTS SCREEN ###
############################################################

screen file_slots(title):

    default selected_slot = 0

    use game_menu(title)

    style_prefix "sl"

    fixed:
        ## The grid of file slots.
        viewport id "sl_vp":
            style_prefix "slot"
            mousewheel True draggable True pagekeys True
            scrollbars None
            has vbox

            for i in range(1*6):
                $ slot = i + 1

                button:
                    selected selected_slot == i + 1
                    action SetLocalVariable("selected_slot", i+1)

                    has vbox

                    
                    vbox:
                        yoffset 80
                        xoffset 80
                        text FileSaveName(slot) style "slot_name_text"


                        hbox:

                            ## https://www.fabriziomusacchio.com/blog/2021-08-15-strftime_Cheat_Sheet/
                            text FileTime(slot,
                                    format=_("{#file_time}%I:%M %p   %m/%d/%Y"),
                                    empty=_("empty slot")):
                                style "slot_time_text"

                            null width 150

                            if FileTime(slot):
                                text format_runtime() style "slot_time_text"

                    

                    # This means the player can hover this save
                    # slot and hit delete to delete it
                    key "save_delete" action FileDelete(slot)

        ### DISPLAY SCREENSHOT
        if FileScreenshot(selected_slot):
            
            add FileScreenshot(selected_slot) pos (1115, 253)
            add Transform("gui/button/gallery_idle_foreground.png", xsize=844, ysize=660) pos (1026, 108)

            hbox:
                pos (1098, 757)
                spacing 120
                textbutton _(title):
                    sensitive selected_slot > 0
                    selected False
                    action FileAction(selected_slot)

                textbutton _("Delete"):
                    sensitive selected_slot > 0
                    action FileDelete(selected_slot)

        vbar value YScrollValue('sl_vp'):
            xpos 940
            ypos 220
            ysize 686



        #if config.has_sync:
        #    if CurrentScreenName() == "save":
        #        textbutton _("Upload Sync"):
        #            action UploadSync()
        #    else:
        #        textbutton _("Download Sync"):
        #            action DownloadSync()

############################################################
### SAVE/LOAD STYELS ###
############################################################
style sl_button:

    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xsize=150, fit='contain', offset=(-20, -20))

style sl_button_text:
    size BTN_TEXT_SIZE2
    idle_color BTN_IDLE_COLOR
    hover_color BTN_HOVER_COLOR
    insensitive_color BTN_INSENSITIVE_COLOR


style slot_viewport:
    pos (30, 220)
    spacing 2
    xysize (912, 685)

style slot_time_text:
    size 25
    xalign 0.5

style slot_vbox:
    spacing 12

style slot_button:
    xysize (860, 355)
    padding (40, 15, 40, 15)
    background "gui/button/slot_[prefix_]background.png"
    selected_background "gui/button/slot_hover_background.png"

style slot_button_text:
    size 50
    align (0.0, 0.5)
    idle_color WHITE
    hover_color WHITE
    selected_idle_color WHITE

style slot_name_text:
    size 50
    align (0.0, 0.5)
    idle_color WHITE
    hover_color WHITE
    selected_idle_color WHITE

style page_hbox:
    xalign 0.5
    spacing 5

style page_vbox:
    xalign 0.5
    yalign 1.0
    spacing 5

style page_button:
    padding (15, 6, 15, 6)
    xalign 0.5

