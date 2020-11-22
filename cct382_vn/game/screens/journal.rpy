# === JOURNAL ===
# This is the code for the player's journal. The journal keeps track of suspect
# information, clues, and testimonies the player has collected.

# === GLOBAL VARIABLES ===

label journal:
    hide screen ui_gamebuttons
    call screen ui_journal
    show screen ui_gamebuttons
    return

screen ui_journal():
    imagemap:
        # return/close map
        hotspot (1171, 48, 47, 45) action Return()

        # position
        xalign 0.5
        yalign 0.5

        # image
        ground "images/ui/journal.png"
