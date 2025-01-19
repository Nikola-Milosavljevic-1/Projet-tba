"""This module defines the Room class, which represents a room in the game world."""
class Room:
    """This class represents a room in the game world."""
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory=set()
        self.pnj={}
        self.item_required = item
    def get_exit(self, direction):
        """
        Return the room in the given direction if it exists.
        Args:
            direction (str): The direction in which to get the room.
        Returns:
            Room: The room in the given direction if it exists, None otherwise.
        """
        return self.exits.get(direction, None)
    def get_exit_string(self):
        """
        Return a string describing the room's exits.
        Returns:
            str: A string describing the room's exits.
        """
        exit_string = "Sorties:"
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    def get_inventory(self):
        """
        Return the inventory of the room.
        Returns:
            dict: The inventory of the room.
        """
        if not self.inventory :
            return "Il n'y a rien ici.\n"
        inventory_string = "On voit :\n"
        for objet in self.inventory :
            inventory_string += "\t- " + str(objet) + "\n"
        inventory_string = inventory_string.strip(",")
        for personnage in self.pnj.values():
            inventory_string += "\t- " + str(personnage) + "\n"
        inventory_string = inventory_string.strip(",")
        return inventory_string
    def get_long_description(self):
        """
        Return a long description of this room including exits.
        Returns:
            str: A long description of this room including exits.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    