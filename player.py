# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history_room = set()
        
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        
        # If the next room is None, print an error message and return False.
        if next_room in self.history_room:
            print("\nVous avez déjà visité cette pièce\n")
            print(next_room.get_long_description())
            return False
        self.history_room.add(self.current_room)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        if next_room == "mort":
            print("\nC'ètait un piège, une porte qui menait dans le vide! Vous êtes de mort de chute\n")
            return False
  
        # Set the current room to the next room.
        self.current_room = next_room
    
        print(self.current_room.get_long_description())
        return True
    
    
    def get_history(self):
        
        if not self.history_room:
            print("\nAucune pièce n'a encore été visitée.")
            return []

        history = [room.name for room in self.history_room]
        print("\nHistorique des pièces visitées :")
        for room_name in history:
            print(f"- {room_name}")
        return history

    