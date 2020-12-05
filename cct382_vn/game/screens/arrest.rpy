# === ARREST ===
# This is the code for that allows the player to choose who to arrest.

# === GLOBAL VARIABLES ===
default suspects_selected = []

label arrest:
    hide screen ui_gamebuttons
    call screen ui_arrest
    show screen ui_gamebuttons
    return

screen ui_arrest():
    # === VARIABLES (DEFUALT) ===
    default maid_selected = False
    default mayor_selected = False
    default brother_selected = False
    default wife_selected = False
    default son_selected = False
    default lover_selected = False
    default secretary_selected = False
    default detective_selected = False

    imagemap:
        # return/close map
        hotspot (895, 0, 58, 55) action SetVariable("suspects_selected", []), Play("sound", "audio/sfx/ui_click_close.wav"), Return()

        # === ARREST BUTTON (CONFIRM SELECTION) ===
        hotspot (374, 545, 235, 49) action Jump("ending")

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/arrest.jpg"

    # === SUSPECTS ===
    # Happy Watson
    imagebutton:
        pos (200, 175)
        if not detective_selected:
            auto suspect_detective.img
            action SetScreenVariable("detective_selected", True), AddToSet(suspects_selected, "detective")
        else:
            idle suspect_detective.img_arrested
            action SetScreenVariable("detective_selected", False), RemoveFromSet(suspects_selected, "detective")
    # Henri Auguste
    imagebutton:
        pos (450, 175)
        if not mayor_selected:
            auto suspect_mayor.img
            action SetScreenVariable("mayor_selected", True), AddToSet(suspects_selected, "mayor")
        else:
            idle suspect_mayor.img_arrested
            action SetScreenVariable("mayor_selected", False), RemoveFromSet(suspects_selected, "mayor")
    # Narberal Tamura
    imagebutton:
        pos (700, 175)
        if not maid_selected:
            auto suspect_maid.img
            action SetScreenVariable("maid_selected", True), AddToSet(suspects_selected, "maid")
        else:
            idle suspect_maid.img_arrested
            action SetScreenVariable("maid_selected", False), RemoveFromSet(suspects_selected, "maid")
    # Isabelle Auguste
    imagebutton:
        pos (950, 175)
        if not wife_selected:
            auto suspect_wife.img
            action SetScreenVariable("wife_selected", True), AddToSet(suspects_selected, "wife")
        else:
            idle suspect_wife.img_arrested
            action SetScreenVariable("wife_selected", False), RemoveFromSet(suspects_selected, "wife")
    # Fabien Auguste
    imagebutton:
        pos (200, 400)
        if not son_selected:
            auto suspect_son.img
            action SetScreenVariable("son_selected", True), AddToSet(suspects_selected, "son")
        else:
            idle suspect_son.img_arrested
            action SetScreenVariable("son_selected", False), RemoveFromSet(suspects_selected, "son")
    # Alec
    imagebutton:
        pos (450, 400)
        if not lover_selected:
            auto suspect_lover.img
            action SetScreenVariable("lover_selected", True), AddToSet(suspects_selected, "lover")
        else:
            idle suspect_lover.img_arrested
            action SetScreenVariable("lover_selected", False), RemoveFromSet(suspects_selected, "lover")
    # Jean Auguste
    imagebutton:
        pos (700, 400)
        if not brother_selected:
            auto suspect_brother.img
            action SetScreenVariable("brother_selected", True), AddToSet(suspects_selected, "brother")
        else:
            idle suspect_brother.img_arrested
            action SetScreenVariable("brother_selected", False), RemoveFromSet(suspects_selected, "brother")
    # Susanne Alberg
    imagebutton:
        pos (950, 400)
        if not secretary_selected:
            auto suspect_secretary.img
            action SetScreenVariable("secretary_selected", True), AddToSet(suspects_selected, "secretary")
        else:
            idle suspect_secretary.img_arrested
            action SetScreenVariable("secretary_selected", False), RemoveFromSet(suspects_selected, "secretary")
