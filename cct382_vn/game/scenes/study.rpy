# === STUDY ===
# The dialogue for the study.

# BUG ITEMS SHOW UP ON TOP OF CHARACTER SPRITES (e.g. key on top of spirit)

# === GLOBAL VARIABLES ===
default state_study = "initial"
define music_playing = False

label study:

    if (music_playing == False):
        $ renpy.music.play("audio/bgm/study_placeholder_test.wav", channel="music", loop=True)
        $ music_playing = True


    while game_room == "study":
        # display proper background depending on state of the room
        if state_study == "initial":
            scene bg study_initial
        elif state_study == "transition_1":
            scene bg study_trans_1
        else:
            scene bg study_final
        window hide
        show screen ui_gamebuttons
        call screen study(state_study)
        show screen study(state_study)
        # === MAID ===
        if _return == "maid":
            window show
            show maid neutral
            maid @ talking "Nabe, at your service."
            hide maid neutral
            show maid neutral onlayer screens at left zorder 2
            window hide
            menu:
                "Who are you and what's your role at the manor?":
                    window show
                    hide maid neutral onlayer screens at left zorder 2
                    show maid neutral at center
                    maid @ talking "My name’s Narberal Tamura, but you can call me Nabe."
                    maid @ annoyed "I used to live in an orphanage until Sir Henri hired me to be his maid."
                    maid @ talking "Since then, I’ve been serving Sir Henri for as long as I can remember."
                    maid @ talking "I’m in charge of all the chores, from cleaning to cooking and serving food for the household."
                    maid @ talking "In return, Sir Henri provided me with a roof over my head. I’m very grateful for his charity..."
                "What was your relationship with Sir Henri?":
                    window show
                    hide maid neutral onlayer screens at left zorder 2
                    show maid neutral at center
                    maid @ annoyed"I was just Sir’s maid, nothing more."
                "Where were you during the time of the murder?":
                    window show
                    hide maid neutral onlayer screens at left zorder 2
                    show maid neutral at center
                    maid @ annoyed "I don’t know exactly when Sir Henri was murdered, I didn’t hear anything!"
                    maid @ thinking "Umm...{w}after serving Sir Henri and Jeanne, I left to clean the upstairs of the manor."
                    maid @ annoyed "W-when I walked in to his s-study, Sir was...{w}he was dead."
                    maid @ annoyed "If only I checked on him earlier...Sir might still be with us."
                "Can you tell me about...":
                    menu:
                        "Henri Auguste (Mayor)":
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ talking "Sir Henri was a great man, he provided me with a home during the darkest times of my life."
                            maid @ annoyed "I could never truly repay the debt I owed."
                        "Isabelle Auguste (Mayor's wife)":
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ talking "Lady Isabelle is a kind soul...{w}Sir recently married her, I think it's only been a few months."
                            maid @ annoyed "I can’t even begin to imagine how Lady Isabelle is feeling...{w}she needs time to grieve, it’s only natural."
                        "Fabien Auguste (Mayor's son)":
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ thinking "With all due respect, Mister Fabien seems very troubled...Sir Henri wasn’t very proud of him since he never likes to study."
                            maid @ annoyed "Mister’s room is usually locked, sometimes he’s not at the manor at all...{w}and his taste in clothing is very odd."
                            maid @ thinking "Mister Fabien is a complete mystery to me."
                        "Susanne Alberg (Mayor's secretary":
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ talking "Susanne has been around since before I was here..."
                            maid @ annoyed "She always questions how much work I do around the manor even though I work very hard!"
                            maid @ thinking "I feel like she’s jealous of me..."
                "Do you know anything about this?":
                    menu:
                        "Antique Dagger":
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ thinking "Sir Henri kept that dagger displayed on the bookshelf. He's very fond of it."
                            maid @ annoyed "I can't believe someone would use it to kill Sir Henri..."
                            maid @ thinking "Sir told me it’s an antique dagger dating back to the 13th century...{w}or was it the 14th?"
                        "Carpet Blood" if playerInventory.hasItem("Blood"):
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ annoyed "Sorry, I don't know anything about that..."
                        "Mayor's Will" if playerInventory.hasItem("Mayor's Will"):
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ talking "You want me to read this?"
                            maid @ thinking "Hmm..."
                            maid @ annoyed "This doesn’t seem right...Sir Henri changed the beneficiary to Lady Isabelle a few weeks ago."
                            maid @ thinking "Why would he change the beneficiary back to Mister Fabien?"
                        "Key" if playerInventory.hasItem("Key"):
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ annoyed "Sorry, I don't know anything about that..."
                        "Suspicious Documents" if playerInventory.hasItem("Suspicious Documents"):
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ thinking "I don’t want to speak ill of Sir Henri, but he was disliked by many in town."
                            maid @ annoyed "I had no idea he kept all this hidden!"
                        "Cup" if playerInventory.hasItem("Cup"):
                            window show
                            hide maid neutral onlayer screens at left zorder 2
                            show maid neutral at center
                            maid @ talking "This is Sir Henri’s personal cup. He uses it when he's in his study."
                "Nevermind. I forgot what I was going to say.":
                    hide maid neutral onlayer screens at left zorder 2
        # === DEAD BODY ===
        elif _return == "body":
            player "So this is the dead body."
            show detective neutral
            detective @ disgust "You're kind of slow aren't you?"
            detective @ angry "OF COURSE THAT'S A DEAD BODY!"
            hide detective neutral
        # === BLOOD ===
        elif _return == "blood":
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
        elif _return == "cup":
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
        elif _return == "dagger":
            show detective neutral
            detective @ disgust "Don't even think about touching that without gloves."
            hide detective neutral
        # === KEY ===
        elif _return == "key":
            player "Oh. It's a key."
            show detective neutral
            detective @ suspicious "This looks important."
            detective @ talking "Let's take it."
            hide detective neutral
            $ playerInventory.add(Clue("Key", "images/objects/clue_key.png", "A key... could I use it to open something?", None))
        # === WILL ===
        elif _return == "will":
            player "Cool. I can use this as scrap paper to jot down notes!"
            show detective neutral
            detective @ surprise "HOLD IT!"
            detective @ angry "THAT'S A WILL! YOU ALMOST DESTROYED IMPORTANT EVIDENCE!"
            detective @ judging "Hmm...{w}The ink seems fresh..."
            player "Maybe the Mayor wrote it before he was murdered?"
            detective @ disgust "Hmm...why don't you put it away before you destroy it by accident."
            $ playerInventory.add(Clue("Mayor's Will", "images/objects/clue_will.png", "The ink seems fresh… did the Mayor write it before he was murdered?", None))
        # === PAINTING ===
        elif _return == "painting_initial":
            player "This painting looks kind cool."
            show detective neutral
            detective @ disgust "Can you not touch random pieces of evidence without gloves?"
            detective @ judging "Now look what you did."
            detective @ disgust "It's crooked. Straighten it up before anyone notices."
            hide detective neutral
            player "Hmm...this painting is a bit hard to straighten..."
            player "Woah!"
            $ state_study = "transition_1"
        elif _return == "painting_final":
            player "Do we just leave this here?"
            show detective neutral
            detective @ talking "I'm sure someone will pick it up eventually."
            hide detective neutral
            show maid neutral
            maid @ annoyed "..."
            hide maid neutral
        # === SAFE ===
        elif _return == "safe":
            show maid neutral
            maid @ annoyed "..."
            hide maid neutral
            show detective neutral
            detective @ surprise "A secret safe!"
            detective @ angry "What are you waiting for?! Open it!"
            player "Uh...{w}is this allowed?"
            detective @ disgust "We're trying to solve a MURDER here. This is just part of the job."
            hide detective neutral
            show maid neutral
            maid @ annoyed "..."
            hide maid neutral
            player "It's unlocked. I guess a quick peek is fine."
            player "Oh what's this?"
            $ state_study = "final"
        # === DOCUMENTS ===
        elif _return == "documents":
            show detective neutral
            detective @ suspicious "What a thick stack of papers."
            detective @ talking "What does it say?"
            detective @ angry "Move closer! I can't see!"
            player "..."
            detective @ surprise "Hold on...{w}this is..."
            detective @ disgust "So many incriminating documents...{w}just how many crimes did the mayor commit?"
            player "So many terrible crimes...{w}no wonder someone wanted to kill him."
            detective @ judging "Let's not jump to conclusions."
            detective @ talking "But you're right."
            detective @ talking "Let's take these for now. The documents might help us find someone with a motive to kill the Mayor."
            $ playerInventory.add(Clue("Suspicious Documents", "images/objects/clue_documents.png", "So many incriminating documents...just how many crimes did the mayor commit?", None))
            hide detective neutral
            show maid neutral
            maid @ annoyed "..."
            hide maid neutral
        # === CASH ===
        elif _return == "cash":
            show detective neutral
            detective @ angry "HEY!{w} STOP EYEING THE CASH!"
            detective @ disgust "{=txt_small}We're in public!"
            detective @ judging "Since the safe was unlocked but no one took the cash, this probably isn't some petty theft gone wrong."
            hide detective neutral
        # === DOOR - FRONTHALL ===
        elif _return == "door_fronthall":
            # player has not unlocked door
            if not playerInventory.hasItem("Key"):
                player "..."
                show detective neutral
                detective @ talking "What are you doing? Do you not know how to open doors?"
                player "This..."
                player "This door is locked..."
                detective @ surprise "WHAT?"
                detective @ angry "WHY WOULD SOMEONE LOCK THE DOOR FROM THE OUTSIDE? WHAT KIND OF DOOR IS THIS???"
                detective @ disgust "{=txt_small}This makes no sense. Who thought this was a good idea?"
                detective @ angry "WHAT ARE YOU WAITNG FOR?{w} GO FIND A KEY SO WE CAN GET OUT!"
                player "..."
                hide detective neutral
            # player first time unlocking door
            elif not hallway_visited:
                player "Ah ha!"
                player "This key fits perfectly!"
                show detective neutral
                detective @ disgust "Oh good. I'm glad we didn't have to ask Nabe to unlock the door."
                detective @ judging "That would be embarassing."
                detective @ disgust "The best detective in town comes to solve a murder and he gets locked in."
                detective @ judging "If people foundo out, my reputation would be ruined."
                player "..."
                hide detective neutral
                play sound "audio/sfx/ui_door.wav"
                $ game_room = "hallway"
                hide screen study
                return
            # player using door regularly
            else:
                play sound "audio/sfx/ui_door.wav"
                $ game_room = "hallway"
                hide screen study
                return
