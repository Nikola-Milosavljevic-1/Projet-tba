# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description, item=None, mission=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory=set()
        self.pnj={}
        self.item_required = item
        self.missiom_cleared = mission
        self.items=[]

    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
    
    def get_inventory(self):
        if not self.inventory :
            return "Il n'y a rien ici.\n"
        else :
            inventory_string = "On voit :\n"
            for objet in self.inventory :
                inventory_string += "\t- " + str(objet) + "\n"
            inventory_string = inventory_string.strip(",")
            for personnage in self.pnj.values():
                inventory_string += "\t- " + str(personnage) + "\n"
            inventory_string = inventory_string.strip(",")
            return inventory_string
   
    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
        
    
    
