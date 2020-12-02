label ending:
    "THIS IS THE END."
    python:
        # remove all call stacks (i.e. player can no longer return)
        renpy.pop_call()
        renpy.pop_call()
        # === MAID ENDING ===
        # This ending occurs if the player decides that the maid is the killer.
        if len(suspects_selected) == 1 and suspects_selected[0] == "maid":
            narrator("YOU HAVE HAVE ARRESTED THE MAID.", interact=True)
            narrator("YOU SENT AN INNOCENT GIRL TO JAIL.", interact=True)
            narrator("DETECTIVE WATSON IS ASHAMED OF YOU.", interact=True)
        # === SUICIDE ENDING ===
        # This ending occurs if the player decides that the Mayor committed suicide.
        elif len(suspects_selected) == 1 and suspects_selected[0] == "maid":
            narrator("INTERESTING.", interact=True)
            narrator("SO YOU BELIEVE THE MAYOR COMMITTED SUICIDE?", interact=True)
            narrator("COOL COOL COOL NO DOUBT NO DOUBT.", interact=True)
        # === EVERYONE'S THE KILLER ENDING ===
        # This ending occurs if the player decides that everyone is the killer.
        elif len(suspects_selected) == 8:
            narrator("SO YOU THINK EVERYBODY IS THE KILLER?", interact=True)
            narrator("EVEN THE MAYOR WAS INVOLVED IN HIS OWN DEATH?", interact=True)
            narrator("COOL COOL COOL NO DOUBT NO DOUBT.", interact=True)
        # === GENERIC ENDING ===
        # This ending occurs if the player selects anything other than the
        # special endings.
        else:
            narrator("I DON'T THINK THIS IS CORRECT.", interact=True)
    return
