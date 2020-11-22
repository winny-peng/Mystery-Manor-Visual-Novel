# === MAP ===
# This is the code for the map of the mansion.

label map:
    hide screen ui_gamebuttons
    call screen ui_map
    show screen ui_gamebuttons
    return

screen ui_map():
    imagemap:
        # return/close map
        hotspot (452, 0, 37, 30) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/map_1.jpg"

    # === ROOMS ===
    # Unvisited rooms are greyed out; visited rooms are displayed. If
    # players hover over each room, the selectedr room will be highlighted
    # and displays its name.

    # STUDY
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "images/ui/map_study_%s.png"
        focus_mask True
        action Null()
