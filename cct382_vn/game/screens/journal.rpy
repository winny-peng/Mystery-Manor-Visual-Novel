# === JOURNAL ===
# This is the code for the player's journal. The journal keeps track of suspect
# information and their testimonies.

# === GLOBAL VARIABLES ===
default suspect_maid = Suspect("Narberal Tamura", "images/ui/pp_unknown_%s.jpg", "Stealing stuff from the mayor, has feelings for the mayor’s brother, friends with the wife.")
default suspect_mayor = Suspect("Henri Auguste", "images/ui/pp_Henri Auguste_%s.jpg", "Hated by all, dead.")
default suspect_brother = Suspect("Jean Auguste", "images/ui/pp_unknown_%s.jpg", "Wants to be mayor, aware of maid’s feelings, uses them as a means to an end.")
default suspect_wife = Suspect("Isabelle Auguste", "images/ui/pp_unknown_%s.jpg", "Second wife; in a relationship with her secret lover, trying to get along with the son, friends with the maid.")
default suspect_son = Suspect("Fabien Auguste", "images/ui/pp_unknown_%s.jpg", "Delinquent, druggie, failure in life. doesn’t get along with the mayor, doesn’t like the wife.")
default suspect_lover = Suspect("Alec", "images/ui/pp_unknown_%s.jpg", "In a relationship with the mayor's wife.")
default suspect_secretary = Suspect("Susanne Alberg", "images/ui/pp_unknown_%s.jpg", "Discovers the mayor’s body. Also the Mayor's secretary.")
default suspect_detective = Suspect("Happy Watson", "images/ui/pp_Happy Watson_%s.jpg", "Intelligent and logical. The World's Best Detective. This is me.")

# === SUSPECT CLASS ===
init -1 python:
    class Suspect:
        """
        The Suspect class stores the information for each suspect.

        === Public Attributes ===
        # testimonies: a list of testimonies given by the Suspect
        # img: path to suspect's profile picture
        # img_arrested: path to suspect's arrested profile picture
        # name: suspect's name
        # description: suspect's description
        """

        def __init__(self, name, img, description):
            self.name = name
            self.img = img
            self.img_arrested = img %("selected_idle")
            self.description = description
            self.testimonies = {}

        # === RECORD INITAL MEETING ===
        def visit(self):
            """
            "Visiting" the suspect updates their profile picture.
            """
            self.img = "images/ui/pp_" + self.name + "_%s.jpg"
            self.img_arrested = "images/ui/pp_" + self.name + "_selected_idle.jpg"

label journal:
    hide screen ui_gamebuttons
    call screen ui_journal
    show screen ui_gamebuttons
    return

screen ui_journal():
    # === VARIABLES ===
    default suspect_current = suspect_maid
    
    # === JOURNAL ===
    imagemap:
        # === RETURN/CLOSE BUTTON ===
        hotspot (1055, 45, 39, 40) action Play("sound", "audio/sfx/ui_click_close.wav"), Return()

        # === BACKGROUND IMAGE ===
        xalign 0.5
        yalign 0.5
        ground "images/ui/journal.png"

    # === SUSPECT NAME ===
    text suspect_current.name color "#000" pos(840, 100) xalign 0.5

    # === SUSPECT DESCRIPTION ===
    vbox:
        area (715, 190, 275, 210)
        box_wrap True
        text suspect_current.description color "#000"

    # === TESTIMONIES ===
    vbox:
        text "Testimonies:" color "#000" pos(715, 365) xalign
    vbox:
        area (715, 400, 270, 275)
        box_wrap True
        for testimony in suspect_current.testimonies:
            if suspect_current.testimonies[testimony] == True:
                text testimony color "#000"

    # === SUSPECT NAVIGATION ===
    # HAPPY WATSON
    imagebutton:
        pos (280, 50)
        auto suspect_detective.img
        action SetScreenVariable("suspect_current", suspect_detective)
    # Henri Auguste
    imagebutton:
        pos (455, 50)
        auto suspect_mayor.img
        action SetScreenVariable("suspect_current", suspect_mayor)
    # Narberal Tamura
    imagebutton:
        pos (280, 210)
        auto suspect_maid.img
        action SetScreenVariable("suspect_current", suspect_maid)
    # Jean Auguste
    imagebutton:
        pos (280, 530)
        auto suspect_brother.img
        action SetScreenVariable("suspect_current", suspect_brother)
    # Isabelle Auguste
    imagebutton:
        pos (455, 210)
        auto suspect_wife.img
        action SetScreenVariable("suspect_current", suspect_wife)
    # Fabien Auguste
    imagebutton:
        pos (280, 370)
        auto suspect_son.img
        action SetScreenVariable("suspect_current", suspect_son)
    # Alec
    imagebutton:
        pos (455, 370)
        auto suspect_lover.img
        action SetScreenVariable("suspect_current", suspect_lover)
    # Susanne Alberg
    imagebutton:
        pos (450, 530)
        auto suspect_secretary.img
        action SetScreenVariable("suspect_current", suspect_secretary)
