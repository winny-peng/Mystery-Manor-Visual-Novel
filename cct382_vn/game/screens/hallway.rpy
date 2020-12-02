# === STUDY ===
# This is the code for the hallway displayables.

screen hallway():
    # === DOOR - STUDY ===
    imagemap:
        ground "images/backgrounds/bg_frontHall.jpg"
        # focus_mask True
        hotspot (503, 172, 232, 315) action Return("door_study")
