# === MAP ===
# This is the code for the map of the mansion. After a player has visited a
# room, it will show up on the map.

# === ROOM VARIABLES ===
# These variables keeps track of which rooms (inside the house), the player has
# visited.

define study_visited = False
define hallway_visited = False

label map:
    hide screen ui_gamebuttons
    call screen ui_map
    show screen ui_gamebuttons
    return

screen ui_map():
    # === MAP BACKGROUND ===
    imagemap:
        # === RETURN/CLOSE BUTTON ===
        hotspot (559, 0, 26, 33) action Play("sound", "audio/sfx/ui_click_close.wav"), Return()

        # === BACKGROUND IMAGE ===
        xalign 0.5
        yalign 0.5
        ground "images/ui/map.png"

    # === ROOMS ===
    # Unvisited rooms are greyed out; visited rooms are displayed. If
    # players hover over each room, the selectedr room will be highlighted
    # and displays its name.

    # === STUDY ===
    if study_visited:
        imagebutton:
            xalign 0.5
            yalign 0.5
            auto "images/ui/map_study_%s.png"
            focus_mask True
            action NullAction()

    # === HALLWAY ===
    if hallway_visited:
        imagebutton:
            xalign 0.5
            yalign 0.5
            auto "images/ui/map_hallway_%s.png"
            focus_mask True
            action NullAction()
