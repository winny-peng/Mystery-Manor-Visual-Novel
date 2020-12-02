# === MAP ===
# This is the code for the map of the mansion.

# === ROOM VARIABLES ===
# These variables keeps track of which rooms (inside the house), the player has
# visited.

define shed_visited = False
define study_visited = False
define kitchen_visited = False
define bathroom_visited = False
define sittingroom_visited = False
define diningroom_visited = False
define hallway_visited = False

label map:
    hide screen ui_gamebuttons
    call screen ui_map
    show screen ui_gamebuttons
    return

screen ui_map():
    imagemap:
        # return/close map
        hotspot (900, 2, 24, 31) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/map.png"

    # === ROOMS ===
    # Unvisited rooms are greyed out; visited rooms are displayed. If
    # players hover over each room, the selectedr room will be highlighted
    # and displays its name.

    # STUDY
    if study_visited:
        imagebutton:
            xalign 0.5
            yalign 0.5
            auto "images/ui/map_study_%s.png"
            focus_mask True
            action NullAction()
