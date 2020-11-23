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
        # testimonies: a list of testimonies given by the Suspect

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
            self.testimonies = []

    class Testimony:
        """
        A Testimony given by a character.

        === Public Attributes ===
        # testimony: the testimony given by a character
        # validity: whether the testimony is true or false

        === Representation Invariants ===
        """
        # === Private Attributes ===

        def __init__(self, testimony, validity):
            """
            Create a new Testimony. Each new Testimony created is True. 
            """
            self.testimony = testimony
            self.validity = True

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
