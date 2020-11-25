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
    default guard_selected = False

    imagemap:
        # return/close map
        hotspot (895, 0, 58, 55) action Return()

        # === ARREST BUTTON (CONFIRM SELECTION) ===
        hotspot (374, 545, 235, 49) action Jump("ending")

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/arrest.jpg"

    # === SUSPECTS ===
    # 1
    imagebutton:
        pos (188, 132)
        if not maid_selected:
            auto suspect_maid.img
            action SetScreenVariable("maid_selected", True), AddToSet(suspects_selected, "maid")
        else:
            idle suspect_maid.img_arrested
            action SetScreenVariable("maid_selected", False), RemoveFromSet(suspects_selected, "maid")
    # 2
    imagebutton:
        pos (422, 144)
        if not mayor_selected:
            auto suspect_mayor.img
            action SetScreenVariable("mayor_selected", True), AddToSet(suspects_selected, "mayor")
        else:
            idle suspect_mayor.img_arrested
            action SetScreenVariable("mayor_selected", False), RemoveFromSet(suspects_selected, "mayor")
    # 3
    imagebutton:
        pos (698, 155)
        if not brother_selected:
            auto suspect_brother.img
            action SetScreenVariable("brother_selected", True), AddToSet(suspects_selected, "brother")
        else:
            idle suspect_brother.img_arrested
            action SetScreenVariable("brother_selected", False), RemoveFromSet(suspects_selected, "brother")
    # 4
    imagebutton:
        pos (870, 163)
        if not wife_selected:
            auto suspect_wife.img
            action SetScreenVariable("wife_selected", True), AddToSet(suspects_selected, "wife")
        else:
            idle suspect_wife.img_arrested
            action SetScreenVariable("wife_selected", False), RemoveFromSet(suspects_selected, "wife")
    # 5
    imagebutton:
        pos (188, 335)
        if not son_selected:
            auto suspect_son.img
            action SetScreenVariable("son_selected", True), AddToSet(suspects_selected, "son")
        else:
            idle suspect_son.img_arrested
            action SetScreenVariable("son_selected", False), RemoveFromSet(suspects_selected, "son")
    # 6
    imagebutton:
        pos (405, 335)
        if not lover_selected:
            auto suspect_lover.img
            action SetScreenVariable("lover_selected", True), AddToSet(suspects_selected, "lover")
        else:
            idle suspect_lover.img_arrested
            action SetScreenVariable("lover_selected", False), RemoveFromSet(suspects_selected, "lover")
    # 7
    imagebutton:
        pos (625, 343)
        if not secretary_selected:
            auto suspect_secretary.img
            action SetScreenVariable("secretary_selected", True), AddToSet(suspects_selected, "secretary")
        else:
            idle suspect_secretary.img_arrested
            action SetScreenVariable("secretary_selected", False), RemoveFromSet(suspects_selected, "secretary")
    # 8
    imagebutton:
        pos (830, 366)
        if not guard_selected:
            auto suspect_guard.img
            action SetScreenVariable("guard_selected", True), AddToSet(suspects_selected, "guard")
        else:
            idle suspect_guard.img_arrested
            action SetScreenVariable("guard_selected", False), RemoveFromSet(suspects_selected, "guard")
