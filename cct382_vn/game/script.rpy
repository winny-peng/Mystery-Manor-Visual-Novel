# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# === GAME STATE VARIABLES ===
default game_room = "study"

# === CHARACTERS ===
define player = Character("ME")
define detective = Character("Detective")
define maid = Character("Maid")

# === CHARACTERS IMAGES ===
image maid_neutral= "images/characters/maid_neutral.png"

# === CLUES ===


# === BACKGROUNDS ===
image bg mansion = "images/backgrounds/bg_mansion.jpg"
image bg tutorial = "images/backgrounds/tutorial.png"
image bg study = "images/backgrounds/study_initial.png"

# Inventory

default playerInventory = Inventory()

# === ROOM CLASSES ===
init -1 python:
    class Room:
        """
        The Room class stores the information for each room.

        === Public Attributes ===
        # state: the state of the room; this determines which background to use
        # clues: a dictionary of all clues in the room and their state

        === Representation Invariants ===
        """
        # === Private Attributes ===

        def __init__(self, state, clues):
            self.state = state
            self.clues = clues

label start:
    # === INTRODUCTION ===
    # The game's introduction.

    # TODO PROOFREAD + GROUP CONFIRMATION
    # Comments: not sure if "guard" is the appropriate description
    scene bg mansion
    with flash

    python:
        """
    # ===== # TODO INVENTORY TESTING CODE =====
    "YOU HAVE NOT PICKED UP THE CAP"
    $ cap = Clue("cap", "images/ui/pp_unknown_idle.jpg", "this is a cap", "cap")
    $ playerInventory.add(cap)
    $ test_2 = playerInventory.hasItem(cap)
    "Do I have the cap? [test_2]"
    "Clue name: [cap.name]"
    "YOU HAVE PICKED UP THE CAP"
    # ===================================

    # ===== # TODO TESTIMONY TESTING CODE =====
    "MAID'S TESTIMONY: I AM A MAID"
    $ suspect_maid.testimonies["I AM A MAID"] = True
    "SYKE"
    "MAID IS NOT THE MAID"
    "REVISED TESTIMONY: I AM A COW"
    $ suspect_maid.testimonies["I AM A MAID"] = False
    $ suspect_maid.testimonies["I AM A COW"] = True
    # ===================================

    "{i}You see a sudden flash and it takes you awhile before your surroundings come into focus.{/i}"
    player "{=txt_thoughts}(...)"
    "{i}You see a tall, golden gate, and behind it, a grand, white manor.{/i}"
    player "{=txt_thoughts}(What the...{w}where am I?)"
    "{i}You instinctively reach for your head to steady yourself when you see something very wrong and horrifying.{/i}"
    player "{=txt_thoughts}(These are...{w}not my hands...{w}WHAT'S HAPPENING???)"
    # TODO SCENE CHANGE
    "{i}The gate suddenly swings open as a guard walks up to you.{/i}"
    # TODO ENTER GUARD
    "???" "Ah! You must be Detective Watson, please follow me."
    player "{=txt_thoughts}(Huh?{p}Detective Watson?{p}Do I look like a Watson to you???)"
    "{i}The guard ushers you in a hurry towards the manor before you can protest.{/i}"
    # TODO SCENE CHANGE
    "{i}The two of you walk towards the house in silence.{/i}"
    "???" "{=txt_small}Get...my...bo...who...you..."
    player "Sorry what did you say?"
    "{i}The guard turns around and looks at you in confusion.{/i}"
    "???" "I didn't say anything Detective Watson."
    "{i}The guard speeds up and the distance between the two of you widen.{/i}"
    player "Did I freak him out? I should be the one freaked out."
    "???" "{=txt_small}Man...deaf...ge...out..."
    "{i}You look at the guard again but the voice doesn't appear to be coming from ahead.{/i}"
    "???" "{=txt_small}No...look...excu...me...HERE!"
    "{i}The voice starts getting louder...and louder, until you realize the source.{/i}"
    "???" "ARE YOU DEAF!? I'M TALKING TO YOU, GET OUT OF MY BODY!"
    "{i}There's a tiny person hovering near your right shoulder.{/i}"
    "{i}He looks a lot like your current body except...much smaller...and you can see through him.{/i}"
    player "{=txt_thoughts}(This...{w}can't be happening.{p}I must be hallucinating.{p}Is he a ghost!?)"
    "???" "SO YOU CAN FINALLY HEAR ME? I’VE BEEN SCREAMING AT YOU FOR THE PAST FIVE MINUTES! AND NO I’M NOT A GHOST!!!"
    player "Wait, did you just read my mind? I never said that out loud!"
    "{i}The guard turns around to see you talking to yourself again and quickly searches for his keys.{/i}"
    "{i}The tiny ghost takes a deep breath as if to calm himself.{/i}"
    "Ghost?" "It seems I can hear your - I mean MY inner thoughts."
    "Ghost?" "I don’t know who you are or why you're in MY body but the last I remember controlling my body, I was getting out of my car."
    "Ghost?" "Anyways I got - I mean WE got more important matters to attend to and you have to do it in my place I suppose."
    "Ghost?" "Follow that man into the manor.{w} Quick, he's staring."
    "{i}With no other choice, you enter the manor.{/i}"
    # TODO SCENE CHANGE
    "{i}Upon entering the manor, you feel submerged in a feeling of dread.{/i}"
    player "{=txt_thoughts}(I’m starting to...{w}feel light-headed...{w}something isn't right about this place.)"
    "Ghost?" "Hmmm?{p}Ahh...{w}I haven’t felt like that in ages. You'll get used to it."
    "Ghost?" "Hmm...{w}how do I explain this...{p}You see, my perception skills have always been better than the average Joe."
    player "Wh-?"
    "{i}Before you can press further, the guard escorts you through the front hall, passing by what seems to be a sitting room to the left and a dining room to the right...{/i}"
    # TODO SCENE CHANGE
    "{i}The guard turns to the left, stopping in front of a closed door.{/i}"
    "Guard" "We've arrived, Detective Watson."
    "You can feel it. The source of that looming feeling of dread is definitely on the other side."
    scene bg tutorial
    "Your new reality hits you like a wrecking ball."
    player "(H-hey old man...what exactly do you do for a living...?)"
    "Ghost?" "Isn’t it obvious by now? I’m a PRIVATE DETECTIVE for crying out loud!"
    "Detective" "And this is a VERY important case. My reputation is on the line!"
    "Detective" "Don’t worry kid, I’ll guide you along the entire way."
    "Detective" "{=txt_small}I don’t want you messing things up anyway..."
    "Detective" "Wait, you ARE a kid right?"
    player "Well actually I-"
    "Detective" "NOPE! You are NOT answering that! You called me an old man so that makes you a kid in my eyes."
    "Detective" "{=txt_small}I'm not even that old anyways."
    "{i}Out of the corner of your eyes, you see the guard quietly leave and someone else entering the room.{/i}"
    "Detective" "Now enough meddling and go talk to the lady on your right."
    "{i}Again, left with no other choice, you follow the detective's words{/i}"
        """
    # === TUTORIAL ===
    # The tutorial explains all the basic controls and available features the
    # player can use (e.g. click to interact, how to use inventory/map/journal)
    # call tutorial

    # === GAME ===
    # The game loops from here. Until the player makes an arrest, the player
    # can explore the game however they like.
    "GAME STARTS"
    while True:
        show screen ui_gamebuttons
        # window hide
        # === STUDY ===
        while game_room == "study":
            scene bg study
            call screen study
            if _return == "maid":
                "You talked to the maid"
        # === FRONT HALL ===
    jump ending
    return
