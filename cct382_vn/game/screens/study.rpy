# === STUDY ===
# This is the code for the study displayables. All interatable objects are
# managed through here. The screen returns a string that lets the game know
# which object the player clicked on.

screen study(state):
    # === PAINTING ===
    if state == "initial":
        imagebutton:
            focus_mask True
            idle "images/objects/study_painting_initial.png"
            action Return("painting_initial")
    else:
        imagebutton:
            focus_mask True
            idle "images/objects/study_painting_final.png"
            action Return("painting_final")
    # === SAFE ===
    if state == "transition_1":
        imagebutton:
            focus_mask True
            idle "images/objects/study_safe.png"
            action Return("safe")
    # === DOCUMENTS ===
    if state == "final":
        if not playerInventory.hasItem("Suspicious Documents"):
            imagebutton:
                focus_mask True
                idle "images/objects/study_documents.png"
                action Return("documents")
    # === CASH ===
        imagebutton:
            focus_mask True
            idle "images/objects/study_cash.png"
            action Return("cash")
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
