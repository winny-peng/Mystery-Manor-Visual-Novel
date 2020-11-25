# === JOURNAL ===
# This is the code for the player's journal. The journal keeps track of suspect
# information and their testimonies.

# === GLOBAL VARIABLES ===
# === SUSPECTS ===
default suspect_maid = Suspect("maid", "images/ui/journal_unknown_%s.jpg", "This is the maid")
default suspect_mayor = Suspect("mayor", "images/ui/journal_unknown_%s.jpg", "This is the dead mayor")
default suspect_brother = Suspect("brother", "images/ui/journal_unknown_%s.jpg", "This is the bro")
default suspect_wife = Suspect("wife", "images/ui/journal_unknown_%s.jpg", "This is the wifey")
default suspect_son = Suspect("son", "images/ui/journal_unknown_%s.jpg", "This is the kid")
default suspect_lover = Suspect("lover", "images/ui/journal_unknown_%s.jpg", "This is the lover")
default suspect_secretary = Suspect("secretary", "images/ui/journal_unknown_%s.jpg", "This is the secretary")
default suspect_guard = Suspect("guard", "images/ui/journal_unknown_%s.jpg", "This is the guard")

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

        def visit(self):
            """
            "Visiting" the suspect unlocks their profile picture.
            """
            self.img = "images/ui/journal_" + self.name + "_%s.jpg"

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
    # === VARIABLES ===
    default suspect_current = suspect_maid

    imagemap:
        # return/close map
        hotspot (1060, 26, 73, 66) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/journal_suspects.png"

        # === SUSPECT INFORMATION ===
        text suspect_current.name color "#000" xpos 861 ypos 111
        text suspect_current.description color "#000" xpos 700 ypos 500
        text suspect_current.img color "#000" xpos 700 ypos 300

        # === TESTIMONY INFORMATION ===
        for testimony in suspect_current.testimonies:
            if testimony.validity == True:
                text testimony.testimony color "#000" xpos 700 ypos 300

    # === SUSPECT NAVIGATION ===
    # 1
    imagebutton:
        pos (275, 32)
        auto suspect_maid.img
        action SetScreenVariable("suspect_current", suspect_maid)
    # 2
    imagebutton:
        pos (451, 34)
        auto suspect_mayor.img
        action SetScreenVariable("suspect_current", suspect_mayor)
    # 3
    imagebutton:
        pos (272, 203)
        auto suspect_brother.img
        action SetScreenVariable("suspect_current", suspect_brother)
    # 4
    imagebutton:
        pos (454, 203)
        auto suspect_wife.img
        action SetScreenVariable("suspect_current", suspect_wife)
    # 5
    imagebutton:
        pos (272, 372)
        auto suspect_son.img
        action SetScreenVariable("suspect_current", suspect_son)
    # 6
    imagebutton:
        pos (451, 369)
        auto suspect_lover.img
        action SetScreenVariable("suspect_current", suspect_lover)
    # 7
    imagebutton:
        pos (273, 535)
        auto suspect_guard.img
        action SetScreenVariable("suspect_current", suspect_guard)
    # 8
    imagebutton:
        pos (451, 534)
        auto suspect_secretary.img
        action SetScreenVariable("suspect_current", suspect_secretary)
