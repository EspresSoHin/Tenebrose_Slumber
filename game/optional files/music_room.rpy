### Music Room ############################################################
##
## A basic setup for a gallery screen, using Ren'Py's built-in Gallery
## system. More information here:
## https://www.renpy.org/doc/html/rooms.html#music-room
##

image unlocked_music_thumb = Transform(RED, xysize=(370, 297))

############################################################
### PYTHON ###
############################################################

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("track1.ogg", always_unlocked=True)
    mr.add("track2.ogg")
    mr.add("track3.ogg")
    mr.add("track4.ogg")

############################################################
### MUSIC ROOM SCREEN ###
############################################################

# Step 3. Create the music room screen.
screen music_room:

    tag menu

    style_prefix "mr"

    fixed:
        grid 3 3:
            xalign 0.5
            ypos 220
            spacing 200

            textbutton _("Track 1") action mr.Play("track1.ogg")
            textbutton _("Track 2") action mr.Play("track2.ogg")
            textbutton _("Track 3") action mr.Play("track3.ogg")
            textbutton _("Track 4") action mr.Play("track4.ogg")



    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "track1.ogg")

############################################################
### MUSIC ROOM STYLES ###
############################################################
style mr_button:
    idle_background None
    hover_background Transform("gui/button/btn_blood_hover.png", xoffset=-30, yoffset=-30)

style mr_button_text:
    size BTN_TEXT_SIZE



    