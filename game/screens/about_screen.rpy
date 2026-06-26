### About screen ############################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.


############################################################
## DEFAULT/DEFINE ###
############################################################

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")

############################################################
### ABOUT SCREEN ###
############################################################

screen about():

    tag menu


    style_prefix "about"
    use game_menu(_("About"))

    fixed:

        viewport id "about_vp":
            mousewheel True draggable True pagekeys True
            scrollbars None

            has vbox

            label "[config.name!t]" text_size 50
            text _("Version [config.version!t]\n")

            if gui.about:
                text "[gui.about!t]\n"
            text "This template is a modified version of EasyRenPyGui by Otoke Neko.\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

        vbar value YScrollValue("about_vp"):
            xpos 1780
            yalign 0.5
            ysize 680

############################################################
### ABOUT STYLES ###
############################################################
style about_viewport:
    pos (100, 220)
    xsize 1710
    ysize 680