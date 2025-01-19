"""This module defines the Player class."""
class Player:
    """
    Classe représentant le joueur du jeu.
    """

    # Constructeur
    def __init__(self, name):
        """
    Classe représentant le joueur dans le jeu.

    Attributes:
        name (str): Nom du joueur.
        current_room (Room): La pièce actuelle du joueur.
        history_room (list): Liste des pièces visitées.
        history (list): Historique des pièces traversées.
        inventory (dict): Inventaire des objets du joueur.
        max_weight (int): Poids maximal que le joueur peut transporter.
        move_count (int): Nombre de déplacements effectués par le joueur.
    """
        self.name = name
        self.current_room = None
        self.history_room = []
        self.history = []
        self.inventory = {}
        self.max_weight = 20
        self.move_count = 0

    # Méthode de déplacement
    def move(self, direction, player):
        """
        Déplace le joueur dans une direction donnée.

        Args:
            direction (str): Direction dans laquelle se déplacer (N, S, E, O, etc.).
            player (Player): Instance du joueur (utile pour vérifier l'inventaire).

        Returns:
            bool: True si le déplacement a réussi, False sinon.
        """
        # Obtenir la pièce suivante à partir des sorties de la pièce actuelle.
        next_room = self.current_room.exits[direction]

        # Si la pièce suivante est None, afficher un message d'erreur et retourner False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        if not self.current_room or direction not in self.current_room.exits:
            print("\nAucune porte dans cette direction !\n")
            return False

        if next_room == "unique":
            print("\nPassage à sens unique !\n")
            return False

        # Vérification de l'objet requis pour accéder à la pièce suivante.
        objet_recquis = next_room.item_required
        if objet_recquis and objet_recquis not in player.inventory.values():
            print("\nVous avez besoin d'un passe pour accéder aux trains.\n")
            return False

        # Mettre à jour la pièce actuelle et l'historique des déplacements.
        self.history.append(self.current_room)
        self.current_room = next_room
        self.move_count += 1
        print(f"{self.current_room.get_long_description()}\n{self.get_history()}")
        print(f"Vous vous êtes déplacé {self.move_count} fois.\n")
        return True

    # Méthode pour afficher l'inventaire du joueur
    def get_inventory(self):
        """
        Affiche l'inventaire du joueur.

        Returns:
            None
        """
        if not self.get_inventory:
            print("\nVotre inventaire est vide.")
            return False

        print("Votre inventaire :")
        for item in self.inventory.values():  # Parcourt les éléments de l'inventaire
            print(f"- {item.name}, {item.description} : {item.protect} de protection {item.damage} d'attaque.")

    # Méthode pour afficher l'historique des pièces visitées
    def get_history(self):
        """
        Affiche l'historique des pièces visitées par le joueur.

        Returns:
            list or bool: Une liste des noms des pièces visitées, ou False si aucune pièce n'a été visitée.
        """
        if not self.history:  # Vérifie si l'historique est vide
            print("\nAucune pièce n'a encore été visitée.")
            return False  # Indique que le retour en arrière est impossible

        history = [room.name for room in self.history]  # Crée une liste des noms des pièces dans l'historique
        print("\nHistorique des pièces visitées :")
        for room_name in history:  # Parcourt chaque nom de pièce dans l'historique
            print(f"- {room_name}")  # Affiche chaque nom de pièce
        return history

    # Méthode pour revenir à la pièce précédente
    def back(self):
        """
        Retourne le joueur à la pièce précédente dans l'historique.

        Returns:
            bool: True si le retour a réussi, False sinon.
        """
        if not self.history:  # Vérifie si l'historique est vide
            print("\nImpossible de revenir en arrière. Vous êtes dans la salle de départ !")
            return False

        # Retirer et retourner la dernière pièce de l'historique
        previous_room = self.history.pop()
        self.move_count += 1
        self.current_room = previous_room
        print(f"\nVous êtes retourné à la salle précédente : {self.current_room.name}")
        print(self.current_room.get_long_description())

        self.get_history()  # Affiche l'historique mis à jour

        return