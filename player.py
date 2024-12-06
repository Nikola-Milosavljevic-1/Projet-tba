# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history_room = []
         
        
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        self.get_history()
        next_room = self.current_room.exits.get(direction)
        # If the next room is None, print an error message and return False.
        if next_room in self.history_room:
            print("\nVous avez déjà visité cette pièce\n")
            print(next_room.get_long_description())
            return False
        self.history_room.append(self.current_room)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        if next_room == "mort":  #si dans la prochaine pièce est "mort", alors afficher qu'il est mort et qu'il a perdu
            print("\nC'ètait un piège, une porte qui menait dans le vide! Vous êtes de mort de chute\n")
            return False
  
        # Set the current room to the next room.
        self.current_room = next_room
    
        print(self.current_room.get_long_description())
        return True
    
    
    def get_history(self):
        
        if not self.history_room:   # Ici on verifie si la pile est vide
            print("\nAucune pièce n'a encore été visitée.")
            return False #indique bien que le retour en arrière a été un echec

        history = [room.name for room in self.history_room] # Crée une liste des noms des pièces dans la pile history_room
        print("\nHistorique des pièces visitées :")
        for room_name in history: #Parcourt chaque nom de pièce dans la liste history
            print(f"- {room_name}") # Affiche chaque nom de pièce avec un tiret devant
        return history

    def back(self):
         if not self.history_room:  # Vérifie si la pile est vide
            print("\nImpossible de revenir en arrière. Vous êtes dans la salle de départ !")
            return False
        
         previous_room=self.history_room.pop() #retirer et retourner le dernier élément         
         self.current_room=previous_room
         print(f"\nVous êtes retourné à la salle précédente : {self.current_room.name}")
         print(self.current_room.get_long_description())
        
         self.get_history()  # Affiche l'historique mis à jour
        
         return 
         
        
    
        # Revenir à la pièce précédente
       