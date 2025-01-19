"""This module defines the Room class, which represents a room in the game world."""
import random
class pnj:
    """
    Classe représentant un personnage non-joueur (PNJ) dans le jeu.

    Attributes:
        name (str): Nom du PNJ.
        description (str): Description du PNJ.
        current_room (Room): Salle actuelle où se trouve le PNJ.
        dialogue (list): Liste des dialogues du PNJ.
        msgs_require_item (list): Messages affichés lorsque le joueur n'a pas l'objet requis.
        msgs (list): Liste des messages standard du PNJ.
        item_required (Item): Objet requis pour interagir avec le PNJ.
        item_gift (Item): Objet donné par le PNJ.
        msg_index (int): Index pour parcourir les messages cycliquement.
        inventory (dict): Inventaire du PNJ.
    """
    def __init__(self, name, description, msgs=None, msgs_require_item=None, room=None, item=None, gift=None):
        """
        Initialise un PNJ avec son nom, sa description, ses messages et ses attributs.

        Args:
            name (str): Nom du PNJ.
            description (str): Description du PNJ.
            msgs (list, optional): Liste des messages standard. Par défaut : None.
            msgs_require_item (list, optional): Messages si un objet est requis. Par défaut : None.
            room (Room, optional): Salle où se trouve le PNJ. Par défaut : None.
            item (Item, optional): Objet requis pour interagir. Par défaut : None.
            gift (Item, optional): Objet donné par le PNJ. Par défaut : None.
        """
        self.name = name
        self.description = description
        self.current_room = room
        self.dialogue = []
        self.msgs_require_item = msgs_require_item
        self.msgs = msgs or []
        self.item_required = item
        self.item_gift = gift
        self.msg_index = 0
        self.inventory = {}

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du personnage.

        Returns:
            str: Une description formatée du personnage.
        """
        return f"{self.name} : {self.description}"

    def __repr__(self):
        """
        Représentation technique (utile pour le débogage).

        Returns:
            str: Représentation technique du PNJ.
        """
        return (f"Item(name={self.name}, description={self.description}")

    def move(self):
        """
        Déplace le PNJ Garde aléatoirement dans une salle.

        Le PNJ reste dans la salle actuelle ou se déplace vers une salle
        adjacente choisie aléatoirement parmi les sorties disponibles.

        Returns:
            bool: True si le PNJ se déplace, False sinon.
        """
        deplacement = random.choice(["bouge", "reste"])
        sorties = self.current_room.exits
        if not sorties:
            return False

        if deplacement == "bouge":
            direction = random.choice(list(sorties.keys()))
            next_room = self.current_room.exits[direction]
            if next_room is None:
                print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
                return False
            if self.name in self.current_room.pnj:
                del self.current_room.pnj[self.name]
            self.current_room = next_room
            next_room.pnj[self.name] = self
            print(f"{self.name} se trouve maintenant dans {self.current_room.name}\n")
            return True

        print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
        return False

    def get_msg(self, player):
        """
        Récupère un message du personnage en fonction de l'inventaire du joueur.

        Returns:
            str: Le message que le personnage dit.
        """
        if not self.msgs:  # Vérifie si la liste des messages est vide
            return f"{self.name} ne veut pas vous parler."

        if self.name.lower() == "prêtresse":
            if self.item_gift:
                if self.item_required.name not in player.inventory:
                    for msg in self.msgs_require_item:
                        print(f"\n- {self.name} : {msg}\n")
                else:
                    for msg in self.msgs:
                        print(f"\n- {self.name} : {msg}\n")
            msg = self.msgs[self.msg_index]
            self.msg_index = (self.msg_index + 1) % len(self.msgs)
            return msg

        if self.name.lower() == "garde":
            if self.item_gift:
                print(self.item_required.name)
                if self.item_required.name not in player.inventory:
                    for msg in self.msgs_require_item:
                        print(f"\n- {self.name} : {msg}\n")
                else:
                    for msg in self.msgs:
                        print(f"\n- {self.name} : {msg}\n")
            msg = self.msgs[self.msg_index]
            self.msg_index = (self.msg_index + 1) % len(self.msgs)
            return msg

        if self.name.lower() == "gardek":
            print("Pour passer il faut que tu me gagnes au jeu de pierre-feuille-ciseaux, sinon tu finiras en prison.")
            while True:
                result = self.play_rps()
                print(result)
                if "gagnez" in result:
                    break
                if "perdez" in result:
                    print("Game Over")
                    exit()

        self.msgs.append(self.msgs[0])
        return self.msgs.pop(0)

    def play_rps(self):
        """
        Joue à pierre-papier-ciseaux avec le joueur.

        Returns:
            str: Le résultat du jeu.
        """
        choices = ["pierre", "papier", "ciseaux"]
        npc_choice = random.choice(choices)
        player_choice = input("Choisissez pierre, papier ou ciseaux: ").lower()

        if player_choice not in choices:
            return "Choix invalide. Vous perdez automatiquement."

        if player_choice == npc_choice:
            return f"Égalité ! Vous avez tous les deux choisi {player_choice}."

        if (player_choice == "pierre" and npc_choice == "ciseaux") or \
           (player_choice == "papier" and npc_choice == "pierre") or \
           (player_choice == "ciseaux" and npc_choice == "papier"):
            return f"Vous gagnez ! Vous avez choisi {player_choice} et le garde a choisi {npc_choice}."
        return f"Vous perdez ! Vous avez choisi {player_choice} et le garde a choisi {npc_choice}. Game Over."
    