# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# === GAME STATE VARIABLES ===
default game_room = "study"

# === CHARACTERS ===
define player = Character("ME")
define maid = Character("Maid", image = "maid")
define detective = Character("Detective", image = "detective")
define sentry = Character("Sentry", image = "sentry")

# === CHARACTERS IMAGES ===
# MAID
image maid neutral = "images/characters/maid_neutral.png"
image maid annoyed = "images/characters/maid_annoyed.png"
image maid talking = "images/characters/maid_talking.png"
image maid thinking = "images/characters/maid_thinking.png"
# DETECTIVE
image detective neutral = "images/characters/detective_neutral.png"
image detective disgust = "images/characters/detective_disgust.png"
image detective judging = "images/characters/detective_judging.png"
image detective angry = "images/characters/detective_angry.png"
image detective surprise = "images/characters/detective_surprise.png"
image detective suspicious = "images/characters/detective_suspicious.png"
image detective talking = "images/characters/detective_talking.png"
# SENTRY
image sentry neutral = "images/characters/sentry_neutral.png"

# === BACKGROUNDS ===
image bg manor_gate = "images/backgrounds/manor_gate.png"
image bg manor_door = "images/backgrounds/manor_door.png"
image bg tutorial = "images/backgrounds/tutorial.png"
image bg study_initial = "images/backgrounds/study_initial.png"
image bg study_trans_1 = "images/backgrounds/study_trans_1.png"
image bg study_final = "images/backgrounds/study_final.png"
image bg hall = "images/backgrounds/hallway_initial.png"

# === TEXT STYLING ===
style txt_thoughts:
    color "#0099cc"
style txt_small:
    size 12
style txt_popup:
    size 60

# === EFFECTS ===
# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 3.0, color="#fff")

# Inventory
default playerInventory = Inventory()
default itemDescription = None

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
    python:
        """
    with flash
    scene bg manor_gate
    "{i}You see a sudden flash and it takes you awhile before your surroundings come into focus.{/i}"
    player "{=txt_thoughts}(...)"
    "{i}You see a tall, dark gate, and behind it, a grand, white manor.{/i}"
    player "{=txt_thoughts}(What the...{w}where am I?)"
    "{i}You instinctively reach for your head to steady yourself when you see something very wrong and horrifying.{/i}"
    player "{=txt_thoughts}(These are...{w}not my hands...{w}WHAT'S HAPPENING???)"
    scene bg manor_door
    "{i}The gate suddenly swings open as a sentry walks up to you.{/i}"
    show sentry neutral
    "???" "Ah! You must be Detective Watson, please follow me."
    player "{=txt_thoughts}(Huh?{p}Detective Watson?{p}Do I look like a Watson to you???)"
    "{i}The sentry ushers you in a hurry towards the manor before you can protest.{/i}"
    hide sentry neutral
    "{i}The two of you walk towards the house in silence.{/i}"
    "???" "{=txt_small}Get...my...bo...who...you..."
    player "Sorry what did you say?"
    show sentry neutral
    "{i}The sentry turns around and looks at you in confusion.{/i}"
    "???" "I didn't say anything Detective Watson."
    hide sentry neutral
    "{i}The sentry speeds up and the distance between the two of you widen.{/i}"
    player "{=txt_thoughts}Did I freak him out? I should be the one freaked out."
    "???" "{=txt_small}Man...deaf...ge...out..."
    "{i}You look at the sentry again but the voice doesn't appear to be coming from ahead.{/i}"
    "???" "{=txt_small}No...look...excu...me...HERE!"
    "{i}The voice starts getting louder...and louder, until you realize the source.{/i}"
    show detective angry with dissolve
    "???" "ARE YOU DEAF!? I'M TALKING TO YOU, GET OUT OF MY BODY!"
    show detective disgust
    "{i}There's a tiny person hovering near your right shoulder.{/i}"
    "{i}He looks a lot like your current body except...much smaller...and you can see through him.{/i}"
    player "{=txt_thoughts}(This...{w}can't be happening.{p}I must be hallucinating.{p}Is he a ghost!?)"
    show detective angry
    "???" "SO YOU CAN FINALLY HEAR ME? I’VE BEEN SCREAMING AT YOU FOR THE PAST FIVE MINUTES! AND NO I’M NOT A GHOST!!! I AM A DETECTIVE!"
    player "Wait, did you just read my mind? I never said that out loud!"
    "{i}The guard turns around to see you talking to yourself again and quickly searches for his keys.{/i}"
    show detective suspicious
    "{i}The tiny ghost detective takes a deep breath as if to calm himself.{/i}"
    show detective neutral
    detective @ talking "It seems I can hear your - I mean MY inner thoughts."
    detective @ disgust "I don’t know who you are or why you're in MY body, but the last thing I remember, when I was still in control of my body, was getting out of my car."
    detective @ talking "Anyways I got - I mean WE got more important matters to attend to and you have to do it in my place I suppose."
    detective @ talking "Follow that man into the manor.{w} Quick, he's staring."
    "{i}With no other choice, you enter the manor.{/i}"
    # TODO SCENE CHANGE
    "{i}Upon entering the manor, you feel submerged in a feeling of dread.{/i}"
    player "{=txt_thoughts}(I’m starting to...{w}feel light-headed...{w}something isn't right about this place.)"
    detective @ talking "Hmmm?{p}Ahh...{w}I haven’t felt like that in ages. You'll get used to it."
    detective @ judging "Hmm...{w}how do I explain this...{p}You see, my perception skills have always been better than the average Joe."
    player "Wh-?"
    "{i}Before you can press further, the guard escorts you through the front hall, passing by what seems to be a sitting room to the left and a dining room to the right...{/i}"
    # TODO SCENE CHANGE
    "{i}The guard turns to the left, stopping in front of a closed door.{/i}"
    sentry "We've arrived, Detective Watson."
    "{i}You can feel it. The source of that looming feeling of dread is definitely on the other side.{/i}"
    scene bg tutorial
    "{i}Your new reality hits you like a wrecking ball.{/i}"
    player "(H-hey old man...who did you say again...?)"
    show detective neutral
    detective @ angry "Isn’t it obvious by now? I’m a PRIVATE DETECTIVE for crying out loud! I EVEN TOLD YOU EARLIER!"
    detective @ surprise "And this is a VERY important case. My reputation is on the line!"
    detective @ judging "Don’t worry kid, I’ll guide you along the entire way."
    detective @ disgust "{=txt_small}I don’t want you messing things up anyway..."
    detective @ disgust "Wait, you ARE a kid right?"
    player "Well actually I-"
    detective @ angry "NOPE! You are NOT answering that! You called me an old man so that makes you a kid in my eyes."
    detective @ disgust "{=txt_small}I'm not even that old anyways."
    "{i}Out of the corner of your eye, you see the sentry quietly leave as someone else enters the room.{/i}"
    "Detective" "Now enough meddling and go talk to the lady on your right."
    "{i}Again, left with no other choice, you follow the detective's words.{/i}"
        """

    # === TUTORIAL ===
    # The tutorial explains all the basic controls and available features the
    # player can use (e.g. click to interact, how to use inventory/map/journal)
    # call tutorial from _call_tutorial

    # === GAME ===
    # The game loops from here. Until the player makes an arrest, the player
    # can explore the game however they like.

    show screen ui_gamebuttons
    while True:
        # === STUDY ===
        if game_room == "study":
            call study from _call_study
        # === FRONT HALL ===
        elif game_room == "hallway":
            call hallway from _call_hallway
    return
