# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("ME")

# Inventory

default playerInventory = Inventory()

# === ROOM CLASSES ===
init -1 python:
    class Room:
        """
        The Room class stores the information for each room.

        === Public Attributes ===
        # img: path to the background image for the room

        === Representation Invariants ===
        """
        # === Private Attributes ===

        def __init__(self, img):
            self.img = img

        def update(self, new_img):
            """
            Update the Room's background image to <new_img>.
            """
            self.img = new_img

label start:
    # === INTRODUCTION ===
    # The game's introduction.
    jump introduction

    # === TUTORIAL ===
    # The tutorial explains all the basic controls and available features the
    # player can use (e.g. click to interact, how to use inventory/map/journal)
    jump tutorial

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
