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
