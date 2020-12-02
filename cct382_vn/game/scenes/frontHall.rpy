"""
Front/Main Hall




"""


init:
    # === BACKGROUNDS ===
    image bg hall = "images/backgrounds/bg_frontHall.jpg"

    # === CHARACTERS ===
    define maid = Character("Maid")
    image maid = "images/characters/maid_neutral.png"

    define guard = Character("Guard")
    image guard = "images/characters/guard_neutral.png"

    # === ITEMS ===
    image key = "images/clues/clueKey.png"
    image poison = "images/clues/cluePoison.png"

    # === TEXT STYLING ===
    style txt_thoughts:
        color "#0099cc"
    style txt_small:
        size 8

    # === EFFECTS ===
    # Camera flash - quickly fades to white, then back to the scene.
    define flash = Fade(0.1, 0.0, 3.0, color="#fff")

label fronthall:

    # TODO REMOVE
    show screen ui_gamebuttons
    # TODO PROOFREAD + GROUP CONFIRMATION
    # Comments: not sure if "guard" is the appropriate description
    scene bg hall
    with flash

    # Testing inventory
    python:
        clueKey = Clue("Mysterious Key", "images/clues/clueKey.png", "A key I found.", True)
        cluePoison = Clue("Poison Sample", "images/clues/cluePoison.png", "A small sample of the poison on the body.", False)
        playerInventory.add(clueKey)
        playerInventory.add(cluePoison)

    # Code to initialize upon entering room
    $ main_hall_visited = False
    python:
        if (main_hall_visited == False):
            main_hall_visited = True
            "YOU HAVE UNLOCKED THE MAIN HALL"


    narrator "{i}This is a test.{/i}"
    "ME" "{=txt_thoughts}(Okay... I've finished investigating the scene of the murder. I should take a look around the rest of the manor, see if I find more clues.)"


    # Leave Front Hall Room
    return
