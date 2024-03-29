# === HALL ===
# The dialogue for the hall.

label hallway:
    while game_room == "hallway":
        show screen ui_gamebuttons
        scene bg hall
        # === FIRST VISIT TO HALL SCRIPT ===
        if not hallway_visited:
            show detective neutral
            detective @ suspicious "Hmm..."
            detective @ talking "Alright. Let's explore the rest of the house and look for more clues."
            hide detective neutral
            narrator "HELLO TESTER! THANK YOU SO MUCH FOR HELPING US TEST OUR GAME!"
            narrator "AT THIS POINT, YOU CAN NO LONGER EXPLORE FURTHER DUE TO LACK OF CONTENT."
            narrator "YOU CAN STILL GO BACK TO THE STUDY BY CLICKING ON THAT DOOR BUT OTHER THAN THAT, THERE IS NOTHING LEFT TO DO."
            narrator "IF YOU WANT, YOU CAN ARREST SOME PEOPLE TO END THE GAME."
            narrator "BUT TO BE HONEST, THERE IS NO POINT BECAUSE YOU HAVE NO INFORMATION AND HAVE ONLY MET 1 SUSPECT."
            narrator "HAVE FUN!"
            $ hallway_visited = True
        window hide
        call screen hallway()

        # === DOOR - STUDY ===
        if _return == "door_study":
            $ game_room = "study"
            hide screen hallway
            return

        # === DOOR - OTHER ROOMS ===
        else:
            narrator "Sorry! This room is under construction! Please be patient!"
    return
