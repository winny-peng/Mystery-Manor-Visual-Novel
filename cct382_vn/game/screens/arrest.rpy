# === ARREST ===
# This is the code for that allows the player to choose who to arrest.

label arrest:
    hide screen ui_gamebuttons
    call screen ui_arrest
    show screen ui_gamebuttons
    return

screen ui_arrest():
    # === VARIABLES (DEFUALT) ===
    default suspects_picked = []

    imagemap:
        # return/close map
        hotspot (895, 0, 58, 55) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/arrest.jpg"

    # === SUSPECTS ===
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
