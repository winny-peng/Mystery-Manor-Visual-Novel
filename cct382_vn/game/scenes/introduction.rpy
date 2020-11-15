# This is the introduction scene.

init:
    # === BACKGROUNDS ===
    image bg mansion = "images/backgrounds/bg_mansion.jpg"

    # === CHARACTERS ===
    define maid = Character("Maid")
    image maid = "images/characters/maid_neutral.png"

    # === TEXT STYLING ===
    style txt_thoughts:
        color "#0099cc"

    # === EFFECTS ===
    # Camera flash - quickly fades to white, then back to the scene.
    define flash = Fade(0.1, 0.0, 3.0, color="#fff")

label introduction:

    # TODO (REMOVE THIS PART LATER)
    show screen ui_gamebuttons
    scene bg mansion
    with flash

    show maid
    "ME" "{=txt_thoughts}(...)"
    "ME" "{=txt_thoughts}(What the...{w}where am I?)"
    "ME" "{=txt_thoughts}(These are...{w}not my hands...{w}WHAT'S HAPPENING???)"
    "Random Person" "Ah! You must be (name of detective), please follow me."
    "ME" "{=txt_thoughts}Huh?{p}(name of detective)?{p}Do I look like a (name of detective) to you???)"


    scene bg mansion

    # end introduction scene
    return
