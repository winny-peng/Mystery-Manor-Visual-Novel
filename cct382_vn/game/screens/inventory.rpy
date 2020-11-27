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
        # Type: The type of the clue (Is it interactable?)

        """
        def __init__(self, name, image, description, type):
            self.name = name;
            self.image = image;
            self.description = description;
            self.type = type;

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
        def hasItem(self, Clue):
            flag = False;
            for item in self.itemList:
                if item == Clue.name:
                    flag = True;
            return flag;





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
        background("#000000")
        action Return()

    grid 8 3:
        for i in playerInventory.itemList:
            frame:
                minimum(120, 120)
                maximum(120, 120)
                xalign(0.5)
        for i in range(24):
            frame:
                minimum(120, 120)
                maximum(120, 120)
                background("#FFFFFF75")
        xalign 0.5
        yalign 0.1

    frame:
        xalign(0.5)
        yalign(0.9)
        minimum(1000, 250)
        maximum(1000, 250)
        background("#00000099")
