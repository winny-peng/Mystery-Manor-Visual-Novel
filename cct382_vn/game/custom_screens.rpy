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
        # TODO uncomment these and fill them out
        # TODO MAKE THIS LOOK BETTER
        # return/close button
        hotspot (452, 0, 37, 30) action Return()

        # position screen in center
        xalign 0.5
        yalign 0.5
        ground "images/ui/ui_map_1.jpg"

        # need a button to display other floor (new screen?)
