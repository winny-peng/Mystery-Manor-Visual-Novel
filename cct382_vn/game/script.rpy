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
image bg study = "images/backgrounds/study_initial.png"

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
    detective @ disgust "I don’t know who you are or why you're in MY body but the last I remember controlling my body, I was getting out of my car."
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
    "{i}Out of the corner of your eyes, you see the sentry quietly leave and someone else entering the room.{/i}"
    "Detective" "Now enough meddling and go talk to the lady on your right."
    "{i}Again, left with no other choice, you follow the detective's words{/i}"
        """
    # === TUTORIAL ===
    # The tutorial explains all the basic controls and available features the
    # player can use (e.g. click to interact, how to use inventory/map/journal)
    call tutorial from _call_tutorial

    # === GAME ===
    # The game loops from here. Until the player makes an arrest, the player
    # can explore the game however they like.
    # === STUDY ===
    while game_room == "study":
        window hide
        show screen ui_gamebuttons
        scene bg study
        call screen study
        show screen study
        # === MAID ===
        if _return == "maid":
            window show
            hide screen study
            show maid neutral
            maid @ talking "Nabe, at your service."
            show maid neutral at left
            window hide
            menu:
                "Who are you and what's your role at the manor?":
                    show maid neutral at center
                    window show
                    maid @ talking "My name’s Narberal Tamura, but you can call me Nabe."
                    maid @ annoyed "I used to live in an orphanage until Sir Henri hired me to be his maid."
                    maid @ talking "Since then, I’ve been serving Sir Henri for as long as I can remember."
                    maid @ talking "I’m in charge of all the chores, from cleaning to cooking and serving food for the household."
                    maid @ talking "In return, Sir Henri provided me with a roof over my head. I’m very grateful for his charity..."
                "What was your relationship with Sir Henri?":
                    window show
                    show maid neutral at center
                    maid @ annoyed"I was just Sir’s maid, nothing more."
                "Where were you during the time of the murder?":
                    window show
                    show maid neutral at center
                    maid @ annoyed "I don’t know exactly when Sir Henri was murdered, I didn’t hear anything!"
                    maid @ thinking "Umm...{w}after serving Sir Henri and Jeanne, I left to clean the upstairs of the manor."
                    maid @ annoyed "W-when I walked in to his s-study, Sir was...{w}he was dead."
                    maid @ annoyed "If only I checked on him earlier...Sir might still be with us."
                "Can you tell me about...":
                    menu:
                        "Henri Auguste (Mayor)":
                            window show
                            show maid neutral at center
                            maid @ talking "Sir Henri was a great man, he provided me with a home during the darkest times of my life."
                            maid @ annoyed "I could never truly repay the debt I owed."
                        "Isabelle Auguste (Mayor's wife)":
                            window show
                            show maid neutral at center
                            maid @ talking "Lady Isabelle is a kind soul...{w}Sir recently married her, I think it's only been a few months."
                            maid @ annoyed "I can’t even begin to imagine how Lady Isabelle is feeling...{w}she needs time to grieve, it’s only natural."
                        "Fabien Auguste (Mayor's son)":
                            window show
                            show maid neutral at center
                            maid @ thinking "With all due respect, Mister Fabien seems very troubled...Sir Henri wasn’t very proud of him since he never likes to study."
                            maid @ annoyed "Mister’s room is usually locked, sometimes he’s not at the manor at all...{w}and his taste in clothing is very odd."
                            maid @ thinking "Mister Fabien is a complete mystery to me."
                        "Susanne Alberg (Mayor's secretary":
                            window show
                            show maid neutral at center
                            maid @ talking "Susanne has been around since before I was here..."
                            maid @ annoyed "She always questions how much work I do around the manor even though I work very hard!"
                            maid @ thinking "I feel like she’s jealous of me..."
                "Do you know anything about this?":
                    menu:
                        "Antique Dagger":
                            window show
                            show maid neutral at center
                            maid @ thinking "Sir Henri kept that dagger displayed on the bookshelf. He's very fond of it."
                            maid @ annoyed "I can't believe someone would use it to kill Sir Henri..."
                            maid @ thinking "Sir told me it’s an antique dagger dating back to the 13th century...{w}or was it the 14th?"
                        "Carpet Blood" if playerInventory.hasItem("Blood"):
                            window show
                            show maid neutral at center
                            maid @ annoyed "Sorry, I don't know anything about that..."
                        "Mayor's Will" if playerInventory.hasItem("Mayor's Will"):
                            window show
                            show maid neutral at center
                            maid @ talking "You want me to read this?"
                            maid @ thinking "Hmm..."
                            maid @ annoyed "This doesn’t seem right...Sir Henri changed the beneficiary to Lady Isabelle a few weeks ago."
                            maid @ thinking "Why would he change the beneficiary back to Mister Fabien?"
                        "Key" if playerInventory.hasItem("Key"):
                            window show
                            show maid neutral at center
                            maid @ annoyed "Sorry, I don't know anything about that..."
                        "Suspicious Documents" if playerInventory.hasItem("Suspicious Documents"):
                            window show
                            show maid neutral at center
                            maid @ thinking "I don’t want to speak ill of Sir Henri, but he was disliked by many in town."
                            maid @ annoyed "I had no idea he kept all this hidden!"
                        "Cup" if playerInventory.hasItem("Cup"):
                            window show
                            show maid neutral at center
                            maid @ talking "This is Sir Henri’s personal cup. He uses it when he's in his study."

        # === DEAD BODY ===
        if _return == "body":
            player "So this is the dead body."
            show detective neutral
            detective @ disgust "You're kind of slow aren't you?"
            detective @ angry "OF COURSE THAT'S A DEAD BODY!"
            hide detective neutral
        # === BLOOD ===
        if _return == "blood":
            if not playerInventory.hasItem("Blood"):
                player "Is this...{w}blood?!"
                show detective neutral
                detective @ suspicious "Hmm...good catch."
                detective @ judging "But why is the blood here if the body is all the way there?"
                detective @ talking "Let's take a picture and add that to our clues."
                $ playerInventory.add(Clue("Blood", "images/objects/clue_blood.png", "Why is the mayor’s body so far away from the blood pool?", None))
            else:
                show detective neutral
                detective @ judging "Stop staring at the blood so much."
                detective @ disgust "{=txt_small}Youngsters these days...so weird..."
            hide detective neutral
        # === CUP ===
        if _return == "cup":
            show detective angry
            if not playerInventory.hasItem("Cup"):
                detective @ surprise "Don't drink from that. That's obviously used."
                player "I-I wasn't going to drink from that!"
                detective @ judging "That's what they all say."
                detective @ talking "It seems like a normal cup but let's keep a note of it anyways."
                $ playerInventory.add(Clue("Cup", "images/objects/clue_cup.png", "A regular cup. Nothing fancy about it.", None))
            else:
                detective "I TOLD YOU. DON'T DRINK FROM THAT CUP."
            hide detective neutral
        # === DAGGER ===
        # TODO PLAYER ALREADY HAS DAGGER FROM TUTORIAL
        if _return == "dagger":
            if not playerInventory.hasItem("Dagger"):
                player "Should I take it out?"
                show detective neutral
                detective @ angry "NO! ARE YOU CRAZY? YOU'RE NOT EVEN WEARING GLOVES"
                detective @ disgust "Don't you know to never touch evidence with bare hands?"
                detective @ judging "Hmmm...{w} it looks like a very old dagger."
                detective @ suspicious "I don't think it's long enough to pierce all the way through his body though..."
                player "I guess I'll add it to our clues then..."
                $ playerInventory.add(Clue("Dagger", "images/objects/clue_dagger.png", "Looks like a very old dagger; long enough to pierce all the way through his body.", None))
            else:
                show detective natural
                detective disgust "Don't even think about touching that without gloves."
            hide detective natural
        # === KEY ===
        if _return == "key":
            "A KEY! WE CAN LEAVE!"
            "THIS DOES NOT DO ANYTHING YET PLEASE BE PATIENT!"
        # === WILL ===
        if _return == "will":
            player "Cool. I can use this a scrap paper to jot down notes!"
            show detective neutral
            detective @ surprise "HOLD IT!"
            detective angry "THAT'S A WILL! YOU ALMOST DESTROYED IMPORTANT EVIDENCE!"
            detective @ judging "Hmm...{w}The ink seems fresh..."
            player "Maybe the Mayor wrote it before he was murdered?"
            detective @ disgust "Hmm...why don't you put it away before you destroy it by accident."
            $ playerInventory.add(Clue("Mayor's Will", "images/objects/clue_will.png", "The ink seems fresh… did the Mayor write it before he was murdered?", None))
        # === FRONT HALL ===
    jump ending
    return
