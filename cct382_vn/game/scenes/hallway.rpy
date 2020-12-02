# === HALL ===
# The dialogue for the hall.

label hallway:
    scene bg hall
    while game_room == "hallway":
        show screen ui_gamebuttons
        scene bg hall
        # === FIRST VISIT TO HALL ===
        if not hallway_visited:
            show detective neutral
            detective @ suspicious "Hmm..."
            detective @ talking "Ok let's explore the rest of the house and look for more clues."
            hide detective neutral
            $ hallway_visited = True
        window hide
        show screen ui_gamebuttons
        call screen hallway()

        # === DOOR - STUDY ===
        if _return == "door_study":
            $ game_room = "study"
            hide screen hallway
            return
    return
