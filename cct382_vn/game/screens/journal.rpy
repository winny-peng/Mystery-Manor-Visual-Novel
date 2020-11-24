# === JOURNAL ===
# This is the code for the player's journal. The journal keeps track of suspect
# information, clues, and testimonies the player has collected.

# === GLOBAL VARIABLES ===
# === SUSPECT
# TODO ALL SUSPECTS START WITH A GENERIC PROFIL PIC UNLESS THEY HAVE MET PLAYER
define suspect_maid = Suspect("Maid", "images/characters/maid_neutral.png", "This is the maid")
define suspect_mayor = Suspect("Mayor", "images/characters/maid_neutral.png", "This is the dead mayor")
define suspect_brother = Suspect("Brother", "images/characters/maid_neutral.png", "This is the bro")
define suspect_wife = Suspect("Wife", "images/characters/maid_neutral.png", "This is the wifey")
define suspect_son = Suspect("Son", "images/characters/maid_neutral.png", "This is the kid")
define suspect_lover = Suspect("Lover", "images/characters/maid_neutral.png", "This is the lover")
define suspect_secretary = Suspect("Secretary", "images/characters/maid_neutral.png", "This is the secretary")
define suspect_guard = Suspect("Guard", "images/characters/maid_neutral.png", "This is the guard")
define suspect_current = suspect_maid

# === SUSPECT CLASS ===
init -1 python:
    class Suspect:
        """
        The Suspect class stores the information for each suspect.

        === Public Attributes ===
        # testimonies: a list of testimonies given by the Suspect
        # img: path to suspect's profile picture
        # name: suspect's name
        # description: suspect's description

        === Representation Invariants ===
        """
        # === Private Attributes ===

        def __init__(self, name, img, description):
            self.name = name
            self.img = img
            self.description = description
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
        # === VARIABLES (DEFUALT) ===
        default page = "suspect"

        text page color "#000" xpos 860 ypos 50

        # return/close map
        hotspot (1060, 26, 73, 66) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/journal_suspects.png"

        # === PAGE NAVIGATION ===
        hotspot (65, 36, 133, 47) action SetScreenVariable("page", "suspect")
        hotspot (64, 99, 134, 48) action SetScreenVariable("page", "clue")

        # === SUSPECT PAGE ===
        if page == "suspect":
            # suspect information
            default suspect_name = "Name of Suspect"
            text suspect_name color "#000" xpos 861 ypos 111

            # profile pictures
            hotspot (272, 30, 136, 146) action SetScreenVariable("suspect_name", "Maid")
            hotspot (451, 31, 133, 143) action SetScreenVariable("suspect_name", "Mayor")
            hotspot (273, 203, 134, 141) action SetScreenVariable("suspect_name","Brother")
            hotspot (451, 203, 132, 143) action SetScreenVariable("suspect_name", "Wife")
            hotspot (273, 371, 134, 144) action SetScreenVariable("suspect_name", "Son")
            hotspot (452, 372, 131, 142) action SetScreenVariable("suspect_name", "Lover")
            hotspot (274, 535, 133, 143) action SetScreenVariable("suspect_name", "Guard")
            hotspot (451, 535, 134, 143) action SetScreenVariable("suspect_name", "Secretary")
