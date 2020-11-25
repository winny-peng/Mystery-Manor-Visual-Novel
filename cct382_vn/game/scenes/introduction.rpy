# This is the introduction scene.

init:
    # === BACKGROUNDS ===
    image bg mansion = "images/backgrounds/bg_mansion.jpg"

    # === CHARACTERS ===
    define maid = Character("Maid")
    image maid = "images/characters/maid_neutral.png"

    define guard = Character("Guard")
    image guard = "images/characters/guard_neutral.png"

    # === TEXT STYLING ===
    style txt_thoughts:
        color "#0099cc"
    style txt_small:
        size 8

    # === EFFECTS ===
    # Camera flash - quickly fades to white, then back to the scene.
    define flash = Fade(0.1, 0.0, 3.0, color="#fff")

label introduction:

    # TODO REMOVE
    show screen ui_gamebuttons
    # TODO PROOFREAD + GROUP CONFIRMATION
    # Comments: not sure if "guard" is the appropriate description
    scene bg mansion
    with flash

    # ===== # TODO MAP TESTING CODE =====
    "YOU HAVE NOT UNLOCKED THE STUDY"
    $ study_visited = True
    "YOU HAVE UNLOCKED THE STUDY"
    # ===================================

    # ===== # TODO SUSPECT TESTING CODE =====
    "YOU HAVE NOT MET THE MAID"
    $ suspect_maid.visit()
    "YOU HAVE MET THE MAID"
    # ===================================

    narrator "{i}You see a sudden flash and it takes you awhile before your surroundings come into focus.{/i}"
    "ME" "{=txt_thoughts}(...)"
    narrator "{i}You see a tall, golden gate, and behind it, a grand, white manor.{/i}"
    "ME" "{=txt_thoughts}(What the...{w}where am I?)"
    narrator "{i}You instinctively reach for your head to steady yourself when you see something very wrong and horrifying.{/i}"
    "ME" "{=txt_thoughts}(These are...{w}not my hands...{w}WHAT'S HAPPENING???)"
    # TODO SCENE CHANGE
    narrator "{i}The gate suddenly swings open as a guard walks up to you.{/i}"
    # TODO ENTER GUARD
    "???" "Ah! You must be Detective Watson, please follow me."
    "ME" "{=txt_thoughts}Huh?{p}Detective Watson?{p}Do I look like a Watson to you???)"
    narrator "{i}The guard ushers you in a hurry towards the manor before you can protest.{/i}"
    # TODO SCENE CHANGE
    narrator "{i}The two of you walk towards the house in silence.{/i}"
    "???" "{=txt_small}Get...my...bo...who...you..."
    "ME" "Sorry what did you say?"
    narrator "{i}The guard turns around and looks at you in confusion.{/i}"
    "???" "I didn't say anything Detective Watson."
    narrator "{i}The guard speeds up and the distance between the two of you widen.{/i}"
    "ME" "Did I freak him out? I should be the one freaked out."
    "???" "{=txt_small}Man...deaf...ge...out..."
    narrator "{i}You look at the guard again but the voice doesn't appear to be coming from ahead.{/i}"
    "???" "{=txt_small}No...look...excu...me...HERE!"
    narrator "{i}The voice starts getting louder...and louder, until you realize the source.{/i}"
    "???" "ARE YOU DEAF!? I'M TALKING TO YOU, GET OUT OF MY BODY!"
    narrator "{i}There's a tiny person hovering near your right shoulder.{/i}"
    narrator "{i}He looks a lot like your current body except...much smaller...and you can see through him.{/i}"
    "ME" "{=txt_thoughts}(This...{w}can't be happening.{p}I must be hallucinating.{p}Is he a ghost!?)"
    "???" "SO YOU CAN FINALLY HEAR ME? I’VE BEEN SCREAMING AT YOU FOR THE PAST FIVE MINUTES! AND NO I’M NOT A GHOST!!!"
    "ME" "Wait, did you just read my mind? I never said that out loud!"
    narrator "{i}The guard turns around to see you talking to yourself again and quickly searches for his keys.{/i}"
    narrator "{i}The tiny ghost takes a deep breath as if to calm himself.{/i}"
    "Ghost?" "It seems I can hear your - I mean MY inner thoughts."
    "Ghost?" "I don’t know who you are or why you're in MY body but the last I remember controlling my body, I was getting out of my car."
    "Ghost?" "Spirit: Anyways I - I mean WE got more important matters to attend to and you have to do it in my place I suppose."
    "Ghost?" "Follow that man into the manor.{w} Quick, he's staring."
    narrator "{i}With no other choice, you enter the manor.{/i}"

    # end introduction scene
    return
