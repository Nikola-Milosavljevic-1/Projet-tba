# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history_room = []
        self.history = []
        self.inventory = {}
        self.max_weight = 20
        self.move_count=0
         
        
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        if not self.current_room or direction not in self.current_room.exits:
                print("\nAucune porte dans cette direction !\n")
                return False

        if next_room == "unique":
            print("\nPassage a sens unique !\n")
            return False
        objet_recquis = next_room.item_required
        if objet_recquis and objet_recquis not in player.inventory.values() :
            print("\nVous avez besoin d'un passe pour acceder aux trains.\n")
            return False
        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        self.move_count += 1
        print(f"{self.current_room.get_long_description()}\n{self.get_history()}")
        print(f"Vous vous etes deplace {self.move_count} fois.\n")
        return True
    
    def get_inventory(self):
        if not self.get_inventory:
            print("\n Votre inventaire est vide.")
            return False
        
        print("votre inventaire :")
        for item in self.inventory.values():  # Parcourt les éléments de l'inventaire
            print(f"- {item.name}: {item.damae} {item.protect} {item.description} ")  
    

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
       