# The game starts here.
image popup_bg = Transform("gui/menu_background.png", xsize=900, fit='contain')

label start:
    $ save_name = "Prologue"

    call screen name_input

    if _mc is None or _mc == "":
        $ _mc = "Y/N"



    MC "Welcome to the GUI Vampire Blood GUI pack."
    "It includes a modified version of {a=https://feniksdev.itch.io/easy-renpy-gui}Fenik's EasyRenPyGUI template{/a}. You can also get the template for free!"

    menu:
        "This pack was created by Otoke Neko."
        "Choice 1":
            pass

        "Choice 2":
            pass

    $ ans = renpy.input("This is showcasing the default input screen.", length=12)

    "Explore around!"


    return
