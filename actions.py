""" Game class for the text-based adventure game. """
import random
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
class Actions:
    """
    Classe regroupant les actions possibles dans le jeu.

    Cette classe contient des méthodes statiques pour chaque action réalisable par le joueur,
    telles que se déplacer, regarder autour de soi, interagir avec des PNJ, et gérer son inventaire.
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Déplace le joueur dans une direction spécifiée.

        La direction doit être un point cardinal (N, E, S, O, etc.).

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si le déplacement a réussi, False sinon.
        
        # Code de la méthode
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Toutes les directions valides
        directions= {
            "N": "N", "NORD": "N",
            "S": "S", "SUD": "S",
            "E": "E", "EST": "E",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U",
            "D": "D", "DOWN": "D"}


        #Convertir la direction en majuscule

        # Move the player in the direction specified by the parameter.
        direction = list_of_words[1].upper()
        if direction in directions:
            direction = directions[direction]
    # Appeler la méthode move du joueur
            if player.move(direction, player):
                for npc in game.pnj:
                    if npc.name == "Garde":
                        npc.move()
                print(f"Vous avez avancé vers : {player.current_room.name}")
            else:
                print("Déplacement impossible.")
        else:
            print("La direction n'existe pas.")
        return True
    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quitte le jeu.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès.
        # Code de la méthode

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci gros bg {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    @staticmethod
    def Check(game, list_of_words, number_of_parameters):
        """
        Vérifie et affiche l'inventaire du joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            None
        """
        l = len(list_of_words)
    # Vérifier si le nombre de paramètres est correct
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"\nLa commande '{command_word}' prend {number_of_parameters} paramètre(s).")
            return False
    # Récupérer l'inventaire du joueur
        game.player.get_inventory()
        return

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Regarde les objets et PNJ présents dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès.
        """

        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters+1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print("\n",game.player.current_room.get_inventory())
        return True

    @staticmethod
    def Take(game, list_of_words, number_of_parameters):
        """
        Permet de prendre un objet dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'objet a été pris, False sinon.
        """
        l = len(list_of_words)

    # Vérifier si le nombre de paramètres est correct
        if l != number_of_parameters+1:
            command_word = list_of_words[0]
            print(f"La commande '{command_word}' prend {number_of_parameters} paramètre(s).")
            return False

        player = game.player
        name_item = list_of_words[1].capitalize()
        total_weight = 0

        for poids in player.inventory.values() :
            total_weight += poids.weight

        for item in player.current_room.inventory :
            if name_item == item.name :

                total_weight += item.weight
                if total_weight > player.max_weight :
                    print(
                        "\nLimite d'objet atteinte, il faut deposer un objet "
                        "avant d'en prendre un nouveau.\n"
                    )
                    return True

                player.inventory[item.name]=item
                player.current_room.inventory.remove(item)
                print(f"\nVous avez pris l'objet : '{item.name}'.\n")
                return True
        if name_item in player.inventory:
            print(f"\nL'objet '{name_item}' se trouve deja dans votre inventaire.\n")
        else :
            print(f"\nL'objet '{name_item}' n'est pas dans cet endroit.\n")
        return True

    @staticmethod
    def Drop(game, list_of_words, number_of_parameters):
        """
        Permet de déposer un objet de l'inventaire du joueur dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'objet a été déposé, False sinon.
        """
        l = len(list_of_words)
        # Vérifie si le nombre de paramètres est correct
        if l != number_of_parameters+1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        name_item = list_of_words[1].capitalize()

    # Vérifie si l'objet est dans l'inventaire du joueur
        if name_item in player.inventory:
            item = player.inventory.pop(name_item)  # Retire l'objet de l'inventaire du joueur

        # Ajoute l'objet à l'inventaire de la pièce
            if isinstance(player.current_room.inventory, set):  # Si inventory est un set
                player.current_room.inventory.add(item)
            elif isinstance(player.current_room.inventory, list):  # Si inventory est une list
                player.current_room.inventory.append(item)
            else:
                print("Erreur : type de collection non supporté pour l'inventaire de la pièce.")
                return False

            print(f"\nVous avez déposé l'objet : '{item.name}'.\n")
        else:
            print(f"\nVous ne possédez pas cet objet : '{name_item}'.\n")
        return True
    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des pièces visitées par le joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès.
        """
        player = game.player

        if not player.history_room: # Vérifie si l'ensemble des salles visitées est vide
            print("\n Aucune pièce n'a été visité.") # Message si aucune pièce n'a été visitée
            return True  # Terminer l'exécution avec succès

        # Afficher l'historique des pièces visitées
        print("\nHistorique des pièces visitées :") # Affiche un titre pour la liste des pièces

        for room in player.history_room:# Parcourt les pièces visitées
            print(f"- {room.name}") # Affiche le nom de chaque pièce visitée
        return True
    @staticmethod
    def back(game,list_of_words, number_of_parameters):
        """
        Retourne à la pièce précédente.

        Args:
            game (Game): L'objet représentant le jeu.

        Returns:
            bool: True si le joueur a réussi à revenir en arrière, False sinon.
        """
        player=game.player
        return player.back()

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler avec un PNJ dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        pnj = game.player.current_room.pnj.values()
        player = game.player
        # character correspond aux pnj présents dans la même room que le joueur
        nom_npc = list_of_words[1].capitalize()
        for npc in pnj:
            if nom_npc == npc.name:
                npc.get_msg(player)
                return True
        print(f"\n Aucun personnage portant ce nom : {nom_npc} dans cet endroit.\n")
        return False
    @staticmethod
    def exchange(game, list_of_words, number_of_parameters):
        """
        Permet d'échanger des objets avec un PNJ.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots de la commande.
            number_of_parameters (int): Nombre de paramètres attendus par la commande.

        Returns:
            bool: True si l'échange a réussi, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        nom_npc = list_of_words[1].capitalize()
        nom_item = list_of_words[2].capitalize()
        pnj = game.player.current_room.pnj.values()
        player = game.player

        for npc in pnj:
            if nom_npc == npc.name:
                if nom_item in player.inventory:
                    if npc.item_required and npc.item_required.name == nom_item:
                        print(f"\n- {npc.name} : '{nom_item}' !"
                              " Je vous remercie.")
                        # Retirer l'objet donné
                        player.inventory.pop(nom_item)
                        if npc.item_gift:
                            # Donner un objet au joueur
                            player.inventory[npc.item_gift.name] = npc.item_gift
                            print(f"Vous avez reçu l'objet: '{npc.item_gift.name}'\n")
                            npc.item_gift = None
                        return True
                    else:
                        print(f"\n{npc.name} n'a pas besoin de cet objet.\n")
                        return False
                else:
                    print(f"\nVous n'avez pas l'objet '{nom_item}' dans votre inventaire.\n")
                    return False
        print(f"\nIl n'y a personne avec le nom : {nom_npc} dans cet endroit.\n")
        return False
    