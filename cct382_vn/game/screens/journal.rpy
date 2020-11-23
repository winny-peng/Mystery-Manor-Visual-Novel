# === JOURNAL ===
# This is the code for the player's journal. The journal keeps track of suspect
# information, clues, and testimonies the player has collected.

# === GLOBAL VARIABLES ===
define suspect_maid = Suspect("Maid", "images/characters/maid_neutral.png", "This is a maid")

# === SUSPECT CLASS ===
init -1 python:
    def load_Suspects():
        """
        This function loads all information into the Suspect class.
        """
        # === MAID ===
        suspect_maid = Suspect("Maid", "images/characters/maid_neutral.png", "This is a maid")

    class Suspect:
        """
        The Suspect class stores the information for each suspect.

        === Public Attributes ===

        === Representation Invariants ===
        """
        # === Private Attributes ===
        # _name: suspect's name
        # _image: path to suspect's profile picture
        # _description: suspect's description

        def __init__(self, name, image_path, description):
            self._name = name
            self._image = image_path
            self._description = description

label journal:
    hide screen ui_gamebuttons
    call screen ui_journal
    show screen ui_gamebuttons
    return

screen ui_journal():
    imagemap:
        # return/close map
        hotspot (1171, 48, 47, 45) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/journal_suspect.png"
