# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        
        
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
      

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        if next_room == "interdit":  #Passage interdit entre la fôret et la tour en pierre
            print("\n Ce passage est interdit, choisissez un autre direction ! \n")
            return False
        if next_room == "unique":   #Passage a sens unique 
            print("\n ce passage est en sens unique, choisissez un autre chemin \n")
            return False
        # Set the current room to the next room.
       
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    