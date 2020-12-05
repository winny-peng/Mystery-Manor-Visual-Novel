# === STUDY ===
# This is the code for the study displayables. All interatable objects are
# managed through here. The screen returns a string that lets the game know
# which object the player clicked on.

screen study(state_objects, state_screen):
    layer "master"
    # === PAINTING ===
    if state_objects == "initial":
        imagebutton:
            focus_mask True
            idle "images/objects/study_painting_initial.png"
            if state_screen == "off":
                action NullAction()
            else:
                action Return("painting_initial")
    else:
        imagebutton:
            focus_mask True
            idle "images/objects/study_painting_final.png"
            if state_screen == "off":
                action NullAction()
            else:
                action Return("painting_final")
    # === SAFE ===
    if state_objects == "transition_1":
        imagebutton:
            focus_mask True
            idle "images/objects/study_safe.png"
            if state_screen == "off":
                action NullAction()
            else:
                action Return("safe")
    # === DOCUMENTS ===
    if state_objects == "final":
        if not playerInventory.hasItem("Suspicious Documents"):
            imagebutton:
                focus_mask True
                idle "images/objects/study_documents.png"
                if state_screen == "off":
                    action NullAction()
                else:
                    action Return("documents")
    # === CASH ===
        imagebutton:
            focus_mask True
            idle "images/objects/study_cash.png"
            if state_screen == "off":
                action NullAction()
            else:
                action Return("cash")
    # === MAID ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_maid.png"
        if state_screen == "off":
            action NullAction()
        else:
            action Return("maid")
    # === DEAD BODY ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_body.png"
        if state_screen == "off":
            action NullAction()
        else:
            action Return("body")
    # === BLOOD ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_blood.png"
        if state_screen == "off":
            action NullAction()
        else:
            action Return("blood")
    # === CUP ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_cup.png"
        if state_screen == "off":
            action NullAction()
        else:
            action Return("cup")
    # === DAGGER ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_dagger.png"
        if state_screen == "off":
            action NullAction()
        else:
            action Return("dagger")
    # === KEY ===
    if not playerInventory.hasItem("Key"):
        imagebutton:
            focus_mask True
            idle "images/objects/study_key.png"
            if state_screen == "off":
                action NullAction()
            else:
                action Return("key")
    # === WILL ===
    if not playerInventory.hasItem("Mayor's Will"):
        imagebutton:
            focus_mask True
            idle "images/objects/study_will.png"
            if state_screen == "off":
                action NullAction()
            else:
                action Return("will")
    # === DOOR - FRONTHALL ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_door_fronthall.png"
        if state_screen == "off":
            action NullAction()
        else:
            action Return("door_fronthall")
