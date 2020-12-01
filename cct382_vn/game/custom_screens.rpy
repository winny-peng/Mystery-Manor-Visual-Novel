# === GAMEBUTTONS ===
# This is the code for gamebuttons.

screen ui_gamebuttons():
    zorder 100
    # === ARREST BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/arrest_%s.png"
        action Call("arrest")

    # === MAP BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/map_%s.png"
        action Call("map")

    # === INVENTORY BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/inventory_%s.png"
        action Call("inventory")

    # === JOURNAL BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/journal_%s.png"
        action Call("journal")
