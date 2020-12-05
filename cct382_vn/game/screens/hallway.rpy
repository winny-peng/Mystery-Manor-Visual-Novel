# === STUDY ===
# This is the code for the hallway displayables.

screen hallway():
    # === DOOR - STUDY ===
    imagebutton:
        auto "images/objects/hallway_study_%s.png"
        focus_mask True
        action Play("sound", "audio/sfx/ui_door.wav"), Return("door_study")

    # === DOOR - LIVING ROOM ===
    imagebutton:
        auto "images/objects/hallway_livingroom_%s.png"
        focus_mask True
        action Play("sound", "audio/sfx/ui_door.wav"), Return()

    # === DOOR - UPSTAIRS ===
    imagebutton:
        auto "images/objects/hallway_upstairs_%s.png"
        focus_mask True
        action Play("sound", "audio/sfx/ui_door.wav"), Return()

    # === DOOR - BACKYARD ===
    imagebutton:
        xalign 1.0
        auto "images/objects/hallway_backyard_%s.png"
        focus_mask True
        action Play("sound", "audio/sfx/ui_door.wav"), Return()

    # === DOOR - KITCHEN ===
    imagebutton:
        xalign 1.0
        auto "images/objects/hallway_kitchen_%s.png"
        focus_mask True
        action Play("sound", "audio/sfx/ui_door.wav"), Return()

    # === DOOR - DINING ROOM ===
    imagebutton:
        xalign 1.0
        auto "images/objects/hallway_diningroom_%s.png"
        focus_mask True
        action Play("sound", "audio/sfx/ui_door.wav"), Return()
