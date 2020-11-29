# This is the introduction scene.

init:
    # === GLOBAL VARIABLES ===
    default room_study = Room("images/backgrounds/study_initial.png")

    # === BACKGROUNDS ===
    image bg mansion = "images/backgrounds/bg_mansion.jpg"
    image bg tutorial = "images/backgrounds/tutorial.png"

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
    detective "HEY! I told you to stop meddling and GO TALK TO THE LADY ON YOUR RIGHT!"
    hide screen say
    while not character_visited:
        call screen tutorial_interactions("tutorial_character")
        if _return:
            $ character_visited = True
    show maid_neutral
    maid "Detective Watson, we're so glad you're finally here..."
    maid "Th-this is so horrible...{w}S-Sir Henri’s been m-murdered in cold blood..."
    maid "Sir Henri was c-completely fine this afternoon, w-who could have done this!?"
    detective "She may seem innocent, but the number one rule for a detective is that everyone’s a suspect."
    hide maid_neutral
    # === TUTORIAL - JOURNAL (SUSPECT) ===
    # TODO ADD IMAGE INSTEAD SO JOURNAL IS NOT CLICKABLE
    detective "You should keep a note of all the suspects."
    detective "I usually write everything down in my journal."
    detective "Why don't you check the journal right now? It's near the bottom to your right."
    while not journal_visited:
        call screen tutorial_interactions("tutorial_journal")
        if _return:
            $ journal_visited = True
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
    detective "Anyways, you can question her later. Right now, you need to figure out how the Mayor was murdered."
    while not object_visited:
        call screen tutorial_interactions("tutorial_object")
        if _return:
            $ object_visited = True
    detective "He was pierced right through his heart...{w}but we can’t rule out the possibility of a suicide."
    # === TUTORIAL - INVENTORY ===
    # TODO NEED WORKING INVENTORY
    detective "Now before you investigate further, a smart detective always keeps track of his gathered clues!"
    detective "Once you pick up an item, make sure to put it into your bag so you can look at it later."
    detective "Go on, what are you waiting for? Open your bag to see if you put it in properly."
    # === TUTORIAL - SHOW CHARACTER OBJECTS ===
    # TODO NEED WORKING INVENTORY
    # === TUTORIAL - JOURNAL(SUSPECT)
    # TODO NEED WORKING INVENTORY (SHOW SUSPECT OBJECT TO OBTAIN TESTIMONY)
    # === TUTORIAL - MAP ===
    detective "You can look for more clues, but when you’re ready to investigate further, the map of the manor will come in handy."
    detective "Why don't you take a quick peek? I worked really hard on it."
    while not map_visited:
        call screen tutorial_interactions("tutorial_map")
        if _return:
            $ map_visited = True
    show screen ui_map
    detective "Oh."
    detective "I guess I accidentally spilled a bit of coffee over it."
    detective "Well I guess you can add the rooms in youself."
    detective "I'm sure you'll enjoy filling it out. It'll be like a fun puzzle!"
    $ study_visited = True
    detective "See, that wasn't so bad! We can write in the rest later when we explore the manor."
    # === TUTORIAL - ARREST ===
    detective "Once you think we found the suspect, you can arrest them at anytime!"
    detective "Although I don't suggest you arrest anyone randomly though."
    detective "Once you make an arrest, there's no turning back. So choose wisely!"
    # === SCRIPT ===
    detective "Welp. That's about it! Everything's pretty easy right? I'm sure you'll get the hang of it."
    detective "{=txt_small}Wow this is exciting! My very first student!"
    detective "Okay! Let's go! Time to solve the mystery!"

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
            idle "images/objects/study_body.png"
            action Return(True)

    # === TUTORIAL - MAP ===
    if tutorial == "tutorial_map":
        imagebutton:
            focus_mask True
            idle "images/ui/ui_map_button.png"
            action Return(True)
