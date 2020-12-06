# Jiu Song
# CCT382 Game Project
# Clues/Inventory System

# Clue Section.

init python:

    class Clue:
        """
        Clue Class: Defines a clue object.

        Attributes
        # Name: Name of the clue
        # Image: Path to the image of the clue
        # Description: Short description of the clue

        """
        def __init__(self, name, image, description):
            self.name = name;
            self.image = image;
            self.description = description;

    class Inventory:
        """
        Inventory Class: Defines the Player Inventory.

        Attributes
        # itemList: A list of Clue objects.

        """
        def __init__(self):
            self.itemList = [];

        # Adds a given Clue object to the Player Inventory.
        def add(self, Clue):
            self.itemList.append(Clue);

        # Removes a given Clue object from the Player Inventory, if it exists.
        # Assumes that no duplicate clues exist.
        def remove(self, Clue):
            self.itemList.remove(Clue);

        # Returns True if the player possesses the given Clue
        # from their Inventory.
        def hasItem(self, clue_name):
            flag = False;
            for item in self.itemList:
                if item.name == clue_name:
                    flag = True;
            return flag;

        # === UPDATE ITEM DESCRIPTION ===
        def update(self, clue, new_description):
            """
            Updates the description of <clue> with <new_description>.
            """
            for item in self.itemList:
                if item.name == clue:
                    item.description = new_description
                    break

label inventory:
    hide screen ui_gamebuttons
    call screen ui_inventory
    show screen ui_gamebuttons
    return

screen ui_inventory():
    button:
        xalign(1.0)
        yalign(0.0)
        minimum(50, 50)
        maximum(50, 50)
        background("#ff0000")
        activate_sound("audio/sfx/ui_click_close.wav")
        action Return()

    grid 8 3:
        xalign 0.5
        yalign 0.1
        spacing 3
        for item in playerInventory.itemList:
            frame:
                minimum(120, 120)
                maximum(120, 120)
                background("#00000050")
                imagebutton idle item.image action SetVariable("itemDescription", item.description)


        for i in range(len(playerInventory.itemList), 24):
            frame:
                minimum(120, 120)
                maximum(120, 120)
                background("#FFFFFF75")


    frame:
        xalign(0.5)
        yalign(0.9)
        minimum(980, 250)
        maximum(980, 250)
        background("#00000099")
        if (itemDescription != None):
            text itemDescription
