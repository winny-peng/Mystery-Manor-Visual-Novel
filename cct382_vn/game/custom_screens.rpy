screen ui_gamebuttons():
    imagemap:
        yalign 1.0
        ground "images/ui/ui_gamebuttons.jpg"

        # TODO change these from scenes to screens
        # TODO decide if we should put all screens here or in different files
        # MAP BUTTON
        hotspot (959, 0, 107, 99) action Call("map")

        # BAG BUTTON
        hotspot (1066, 0, 106, 100) action Jump("inventory")

        # JOURNAL BUTTON
        hotspot (1172, 0, 107, 100) action Jump("journal")

        # ARREST BUTTON
        hotspot (35, 0, 119, 99) action Jump("arrest")

# === MAP ===
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
