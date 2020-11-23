# === JOURNAL ===
# This is the code for the player's journal. The journal keeps track of suspect
# information, clues, and testimonies the player has collected.

# === GLOBAL VARIABLES ===
# TODO ALL SUSPECTS START WITH A GENERIC PROFIL PIC UNLESS THEY HAVE MET PLAYER
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
        # img: path to suspect's profile picture

        === Representation Invariants ===
        """
        # === Private Attributes ===
        # _name: suspect's name
        # _description: suspect's description

        def __init__(self, name, img, description):
            self._name = name
            self.img = img
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

    class Clue:
        """
        The Clue class stores the information for each clue.

        === Public Attributes ===

        === Representation Invariants ===
        """
        # === Private Attributes ===
        # _title: display name for the clue (e.g. Winny's Knife)
        # _img: path to the clue's image
        # _description: description about the clue

        def __init__(self, title, img, description):
            self._title = title
            self._img = img
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
