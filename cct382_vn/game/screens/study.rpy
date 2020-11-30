# === STUDY ===
# This is the code for the study displayables. All interatable objects are
# managed through here.

screen study:
    # === MAID ===
    imagebutton:
        focus_mask True
        idle "images/objects/study_maid.png"
        action Return("maid")
