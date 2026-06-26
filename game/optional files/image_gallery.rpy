### Gallery ############################################################
##
## A basic setup for a gallery screen, using Ren'Py's built-in Gallery
## system. More information here:
## https://www.renpy.org/doc/html/rooms.html#image-gallery
##

############################################################
### TABLE OF CONTENTS ###
############################################################
# 1. Python
# 2. Images
# 3. Gallery Screen
# 4. Gallery Styles

############################################################
### PYTHON ###
############################################################

init python:

    ## First, some constants to speed up declarations

    ## The size of gallery buttons/thumbnails
    gallery_thumb_size = (528, 297)

    ## For convenience's sake: list off all the gallery image
    ## names we're going to use in this gallery
    gallery_buttons = [
        'cg_1', 'cg_2', 'cg_3', 'cg_4', 'cg_5', 'cg_6'
    ]

    ## Set up the gallery
    g = Gallery()
    g.locked_button = "gui/button/gallery_locked_background.png"

    g.idle_border = Transform("gui/button/gallery_idle_foreground.png", xoffset=-67, yoffset=-100)
    g.hover_border = Transform("gui/button/gallery_hover_foreground.png", xoffset=-68, yoffset=-100)

    ## And declare the various gallery images
    ## This file doesn't assume the presence of any GUI files, so I'm
    ## just using basic squares, declared as images below, but you will
    ## replace these with actual images.
    ## These use the names declared in the gallery_buttons list
    g.button("cg_1")
    g.image("cg 1")

    g.button("cg_2")
    g.image("cg 2")

    g.button("cg_3")
    g.unlock_image("cg 3")

    g.button("cg_4")
    g.unlock_image("cg 4")

    g.button("cg_5")
    g.unlock_image("cg 5")

    g.button("cg_6")
    g.image("cg 6")


    ## For gallery pagination
    cgs_per_page = 4
    total_cgs = len(gallery_buttons)
    ## We do -1 so that it doesnt ROUND UP and create an extra page
    total_gal_pages = (total_cgs + cgs_per_page - 1) // cgs_per_page


############################################################
### CG IMAGES ###
############################################################
##
## You can define the unlockable images here or elswhere.
image cg 1 = "cg 1.png"
image cg 2 = Solid(GOLD)
image cg 3 = Solid(RED)
image cg 4 = Solid(WHITE)
image cg 5 = Solid(GRAY)
image cg 6 = Solid(CREAM)


## The thumbnails

image cg_1_thumb = Transform("cg 1", xysize=gallery_thumb_size)
image cg_2_thumb = Transform(GOLD, xysize=gallery_thumb_size)
image cg_3_thumb = Transform(RED, xysize=gallery_thumb_size)
image cg_4_thumb = Transform(WHITE, xysize=gallery_thumb_size)
image cg_5_thumb = Transform(GRAY, xysize=gallery_thumb_size)
image cg_6_thumb = Transform(CREAM, xysize=gallery_thumb_size)



############################################################
### GALLERY SCREENS ###
############################################################

screen gallery():
    default curr_page = 1

    tag menu



    fixed:
        style_prefix 'gal'

        ## We get the correct images for that page
        ## -1 since curr_page starts at 1
        $ start_index = int((curr_page - 1) * cgs_per_page)
        $ end_index = int(start_index + cgs_per_page)


        ## Organize the gallery images into a grid
        grid 2 2:
            for btn in gallery_buttons[start_index:end_index]:

                add g.make_button(btn, "{}_thumb".format(btn))

            ## If you're not using the loop, this will look instead like:
            # add g.make_button("button_name", "button_thumbnail.png")

        ## Page Buttons
        imagebutton auto "gui/button/btn_left_arrow_%s.png":
            yalign 0.5
            xpos 80
            action SetLocalVariable("curr_page", max(curr_page - 1, 1))

        imagebutton auto "gui/button/btn_right_arrow_%s.png":
            xanchor 1.0
            yalign 0.5
            xpos config.screen_width-80
            action SetLocalVariable("curr_page", min(curr_page + 1, total_gal_pages))


############################################################
### GALLERY STYLES ###
############################################################

style gal_grid:
    xalign 0.5
    ypos 250
    spacing 80
