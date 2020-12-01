# This is the introduction scene.

init:
    define guard = Character("Guard")
    image guard = "images/characters/guard_neutral.png"

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

label tutorial:
    # === VARIABLES ===
    default character_visited = False
    default object_visited = False
    default journal_visited = False
    default map_visited = False
    default inventory_visited = False

    # === SCRIPT ===
    scene bg tutorial
    "Pay attention. You are thrust into the role of a detective and you have no experience whatsoever."
    "Luckily, Detective Watson is going to quickly show you the ropes."
    "Follow his instructions by clicking on the objects and people to interact with them."
    "Good luck Detective!"
    window hide
    show text "{=txt_popup}How To Detective 101" with dissolve
    with Pause(1)
    hide text with dissolve
    with Pause(1)
    window show
    # === TUTORIAL - CHARACTER INTERACTION ===
    show detective angry
    detective "HEY! I told you to stop meddling and GO TALK TO THE LADY ON YOUR RIGHT!"
    hide detective angry
    window hide
    while not character_visited:
        call screen tutorial_interactions("tutorial_character")
        if _return:
            $ character_visited = True
    show maid neutral
    window show
    maid @ talking "Detective Watson, we're so glad you're finally here..."
    maid @ annoyed "Th-this is so horrible...{w}S-Sir Henri’s been m-murdered in cold blood..."
    maid @ thinking "Sir Henri was c-completely fine this afternoon, w-who could have done this!?"
    detective "She may seem innocent, but the number one rule for a detective is that everyone’s a suspect."
    hide maid neutral
    # === TUTORIAL - JOURNAL (SUSPECT) ===
    show detective neutral
    detective @ talking "You should keep a note of all the suspects."
    detective @ talking "I usually write everything down in my journal."
    detective @ talking "Why don't you check the journal right now? It's near the bottom to your right."
    hide detective neutral
    window hide
    while not journal_visited:
        call screen tutorial_interactions("tutorial_journal")
        if _return:
            $ journal_visited = True
    window show
    show screen ui_journal
    detective "I already wrote down all the information for the household before this body switching shenanigans happened."
    detective "I'm sure you'll find my notes very handy since I'm VERY thorough."
    detective "Anyways, I haven't met all the suspects yet so there aren't any pictures for them."
    detective "Hopefully we can find all of them later during our investigation."
    detective "For now, let's put in a picture of the maid we just met."
    $ suspect_maid.visit()
    detective "Woot! This is great! Now we can remember everyone's names AND faces."
    detective "{=txt_small}I always forget what people look like."
    hide screen ui_journal
    # === TUTORIAL - OBJECT INTERACTION ===
    show detective talking
    detective "Anyways, you can question her later. Right now, you need to figure out how the Mayor was murdered."
    hide detective talking
    window hide
    while not object_visited:
        call screen tutorial_interactions("tutorial_object")
        if _return:
            $ object_visited = True
    $ playerInventory.add(Clue("Dagger", "images/objects/clue_dagger.png", "Looks like a very old dagger, but long enough to pierce all the way through his body.", None))
    window show
    show detective neutral
    detective @ talking "Looks like a very old dagger, but long enough to pierce all the way through his body."
    detective @ talking "He was pierced right through his heart...{w}but we can’t rule out the possibility of a suicide."
    # === TUTORIAL - INVENTORY ===
    detective @ talking "Now before you investigate further, a smart detective always keeps track of his gathered clues!"
    detective @ talking "Once you pick up an item, make sure to put it into your bag so you can look at it later."
    detective @ disgust "Go on, what are you waiting for? Open your bag to see if you put it in properly."
    hide detective neutral
    window hide
    while not inventory_visited:
        call screen tutorial_interactions("tutorial_inventory")
        if _return:
            $ inventory_visited = True
    show screen ui_inventory
    detective "Ah perfect! Our first clue!"
    detective "If we ever forget what clues we've found, we can always check back here."
    hide screen ui_inventory
    # === TUTORIAL - SHOW CHARACTER OBJECTS ===
    show detective neutral
    detective @ suspicious "Hmm...{w}this dagger doesn't look too special."
    detective @ talking "Let's go ask that lady again and see if she knows anything about the dagger."
    hide detective neutral
    window hide
    $ character_visited = False
    while not character_visited:
        call screen tutorial_interactions("tutorial_character")
        if _return:
            $ character_visited = True
    show maid neutral at left
    menu:
        "Do you know anything about this?":
            menu:
                "Antique Dagger":
                    window show
                    show maid neutral at center
                    maid @ thinking "Sir Henri kept that dagger displayed on the bookshelf. He's very fond of it."
                    maid @ annoyed "I can't believe someone would use it to kill Sir Henri..."
                    maid @ thinking "Sir told me it’s an antique dagger dating back to the 13th century...{w}or was it the 14th?"
    hide maid neutral
    show detective neutral
    detective @ suspicious "So it dates back to the middle ages? It must be a knightly dagger from the looks of it..."
    # === TUTORIAL - JOURNAL(TESTIMONY)
    detective @ judging "Hmm...{w}that might come in handy later."
    detective @ talking "Let's write that down. You never know when a suspect's testimony will come in handy."
    detective @ judging "I hope you remember where you put the journal."
    hide detective neutral
    window hide
    $ journal_visited = False
    while not journal_visited:
        call screen tutorial_interactions("tutorial_journal")
        if _return:
            $ journal_visited = True
    window show
    show screen ui_journal
    detective "Let's write down her testimony so we don't forget."
    $ suspect_maid.testimonies["Sir Henri kept that dagger displayed on the bookshelf. He's very fond of it."] = True
    detective "Ah that's better."
    hide screen ui_journal
    # === TUTORIAL - MAP ===
    show detective neutral
    detective @ talking  "You can look for more clues, but when you’re ready to investigate further, the map of the manor will come in handy."
    detective @ judging "Why don't you take a quick peek? I worked really hard on it."
    hide detective neutral
    window hide
    while not map_visited:
        call screen tutorial_interactions("tutorial_map")
        if _return:
            $ map_visited = True
    window show
    show screen ui_map
    detective "Oh."
    detective "I guess I accidentally spilled a bit of coffee over it."
    detective "Well I guess you can add the rooms in youself."
    detective "I'm sure you'll enjoy filling it out. It'll be like a fun puzzle!"
    $ study_visited = True
    detective "See, that wasn't so bad! We can write in the rest later when we explore the manor."
    hide screen ui_map
    # === TUTORIAL - ARREST ===
    show detective neutral
    detective @ talking "Once you think we found the suspect, you can arrest them at anytime!"
    detective @ surprise "Although I don't suggest you arrest anyone randomly though."
    detective @ judging "Once you make an arrest, there's no turning back. So choose wisely!"
    # === SCRIPT ===
    detective @ suspicious "Welp. That's about it! Everything's pretty easy right? I'm sure you'll get the hang of it."
    detective @ talking "{=txt_small}Wow this is exciting! My very first student!"
    detective @ angry "Okay! Let's go! Time to solve the mystery!"
    return

screen tutorial_interactions(tutorial):
    # === FOCUS OBJECT ===
    # Guides the player by adding a dark overlay over the objects they're not
    # supposed to interact with.
    frame:
        background ("#00000095")

    # === TUTORIAL - CHARACTER INTERACTION ===
    if tutorial == "tutorial_character":
        imagebutton:
            focus_mask True
            idle "images/objects/study_maid.png"
            action Return(True)

    # === TUTORIAL - JOURNAL ===
    if tutorial == "tutorial_journal":
        imagebutton:
            focus_mask True
            idle "images/ui/ui_journal_button.png"
            action Return(True)

    # === TUTORIAL - OBJECT INTERACTION ===
    if tutorial == "tutorial_object":
        imagebutton:
            focus_mask True
            idle "images/objects/study_dagger.png"
            action Return(True)

    # === TUTORIAL - INVENTORY ===
    if tutorial == "tutorial_inventory":
        imagebutton:
            focus_mask True
            idle "images/ui/ui_inventory_button.png"
            action Return(True)

    # === TUTORIAL - MAP ===
    if tutorial == "tutorial_map":
        imagebutton:
            focus_mask True
            idle "images/ui/ui_map_button.png"
            action Return(True)
