# === GAMEBUTTONS ===
# This is the code for gamebuttons.

screen ui_gamebuttons():
    zorder 100
    # === ARREST BUTTON ===
    imagebutton:
        xalign 0.0
        yalign 1.0
        focus_mask True
        auto "images/ui/arrest_%s.png"
        hover_sound "audio/sfx/ui_click.wav"
        activate_sound "audio/sfx/ui_arrest.wav"
        action Call("arrest")

    # === MAP BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/map_%s.png"
        hover_sound "audio/sfx/ui_click.wav"
        activate_sound "audio/sfx/ui_map.wav"
        action Call("map")

    # === INVENTORY BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/inventory_%s.png"
        hover_sound "audio/sfx/ui_click.wav"
        activate_sound "audio/sfx/ui_inventory.wav"
        action Call("inventory")

    # === JOURNAL BUTTON ===
    imagebutton:
        yalign 1.0
        focus_mask True
        auto "images/ui/journal_%s.png"
        hover_sound "audio/sfx/ui_click.wav"
        activate_sound "audio/sfx/ui_journal.wav"
        action Call("journal")
