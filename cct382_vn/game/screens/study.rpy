# === STUDY ===
# This is the code for the study displayables. All interatable objects are
# managed through here. The screen returns a string that lets the game know
# which object the player clicked on.

screen study():
    # === MAID ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_maid.png"
        action Return("maid")
    # === DEAD BODY ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_body.png"
        action Return("body")
    # === BLOOD ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_blood.png"
        action Return("blood")
    # === CUP ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_cup.png"
        action Return("cup")
    # === DAGGER ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_dagger.png"
        action Return("dagger")
    # === KEY ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_key.png"
        action Return("key")
    # === WILL ===
    if not playerInventory.hasItem("Mayor's Will"):
        imagebutton:
            focus_mask True
            idle "images/objects/study_will.png"
            action Return("will")
