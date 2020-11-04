# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define winny = Character("Winny")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show char winny

    # These display lines of dialogue.

    winny "Let's play some minigames!"

    menu:
        winny "Which game should we play?"

        "Fishing #1 (In Progress)":
            jump fishing_v1

        "Clicker #1 (In Progress)":
            jump clicker_v1

    # This ends the game.

    return
