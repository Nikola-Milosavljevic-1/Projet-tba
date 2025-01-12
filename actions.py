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

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

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
            "D": "D", "DOWN": "D",
            }
        # Get the direction from the list of words.
        direction = list_of_words[1]

        #Convertir la direction en majuscule
        direction = direction.upper()
        if direction in directions:
            direction = directions[direction]
            # Move the player in the direction specified by the parameter.
            player.move(direction)
        else:
            print(f"Direction '{direction}' non reconnue.")
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

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
   
    def Check(game, list_of_words, number_of_parameters):
        
        l = len(list_of_words)

    # Vérifier si le nombre de paramètres est correct
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"\nLa commande '{command_word}' prend {number_of_parameters} paramètre(s).")
            return False

    # Récupérer l'inventaire du joueur
        game.player.get_inventory()
        return

           
    
    def Look(game, list_of_words, number_of_parameters):
        current_room = game.player.current_room
        print(f"\nVous êtes dans : {current_room}")

    # Affiche les objets dans la pièce
        if current_room.items:
            print("\nObjets dans la pièce :")
            for item in current_room.items:
                print(f"- {item}")
        else:
            print("\nAucun objet dans cette pièce.")

    # Affiche les PNJ dans la pièce
        if current_room.pnj:
            print("\nPersonnages présents :")
            for npc in current_room.pnj:
                print(f"- {npc}")
        else:
            print("\nIl n'y a personne ici.")
    # Vérifie si le joueur a entré trop de paramètres
        
        # Affiche la description détaillée de la salle actuelle
        
        return print(game.player.current_room.get_inventory())

    def Take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)

    # Vérifier si le nombre de paramètres est correct
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"La commande '{command_word}' prend {number_of_parameters} paramètre(s).")
            return False

        player = game.player  # Récupérer le joueur
        name_item = list_of_words[1]  # Normaliser le nom de l'objet (avec majuscule)
        total_weight = 0  # Initialiser le poids total

    # Calculer le poids total des objets dans l'inventaire
        for item in player.inventory.values():
            total_weight += item.weight

    # Parcourir les objets dans la pièce actuelle
        for item in player.current_room.inventory:
            if name_item == item.name:  # Comparer le nom de l'objet
                total_weight += item.weight

            # Vérifier si le poids total dépasse la limite
                if total_weight > player.max_weight:
                    print("\nLimite de poids atteinte ! Déposez un objet avant d'en prendre un nouveau.\n")
                    return True

            # Ajouter l'objet à l'inventaire du joueur
                player.inventory[item.name] = item
            # Retirer l'objet de la pièce
                player.current_room.inventory.remove(item)
                print(f"\nVous avez pris l'objet : '{item.name}'.\n")
                return True

    # Vérifier si l'objet est déjà dans l'inventaire
        if not name_item in player.current_room.inventory:
            #print(f"\nL'objet '{name_item}' est déjà dans votre inventaire.\n")
        #else:
            print(f"\nL'objet '{name_item}' n'est pas présent dans cette pièce.\n")

        return True 
    
    def Drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        name_item = list_of_words[1].capitalize()

        if name_item in player.inventory :
            item = player.inventory.pop(name_item)
            player.current_room.inventory.add(item)
            print(f"\nVous avez déposé l'objet : '{item.name}'.\n")
        else :
            print(f"\nVous ne possedez pas cet objet : '{name_item}'.\n")
        return True
    
    def history(game, list_of_words, number_of_parameters):
        player = game.player
        
        if not player.history_room: # Vérifie si l'ensemble des salles visitées est vide
            print("\nVous n'avez encore visité aucune pièce.") # Message si aucune pièce n'a été visitée
            return True  # Terminer l'exécution avec succès

        # Afficher l'historique des pièces visitées
        print("\nHistorique des pièces visitées :") # Affiche un titre pour la liste des pièces
        for room in player.history_room: # Parcourt les pièces visitées
            print(f"- {room.name}") # Affiche le nom de chaque pièce visitée
        return True
    
    def back(game, list_of_words, number_of_parameters):
        player = game.player
        return player.back()
    
    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un personnage dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        pnj = game.player.current_room.pnj.values()
        nom_npc = list_of_words[1].capitalize()
       
        if len(list_of_words) < 2:
            print("Spécifiez le nom du PNJ avec qui parler.")
            return False

        # Normaliser le nom entré
        nom_npc = list_of_words[1].strip().lower()
        pnj = game.player.current_room.pnj.values()  # Récupère les PNJ présents (dictionnaire)

         # Débogage : Afficher le contenu des PNJ présents
        print(f"PNJ présents : {[npc.name for npc in pnj]}")
        print(f"Nom recherché : {nom_npc}")

        found = False  # Indique si le PNJ a été trouvé
        for npc in pnj:
            if npc.name.lower() == nom_npc:  # Comparaison insensible à la casse
                print(f"\n- {npc.name} : {npc.get_msg(game.player)}\n")
                found = True
                break

        if not found:
            print(f"\nIl n'y a personne avec le nom : {list_of_words[1]} dans cet endroit.\n")

        return True
        
    @staticmethod
    def exchange(self, player, game, list_of_words, number_of_parameters):
    
        """
        Permet au joueur d'échanger un objet avec un personnage.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """

   
    # Vérifier que la commande contient le nom d'un PNJ
        if len(list_of_words) < 2:
            print("\nSpécifiez le PNJ avec qui vous voulez échanger.")
            return False

        # Récupérer le nom du PNJ depuis la commande
        nom_pnj = list_of_words[1].capitalize()
        player = game.player
        current_room = player.current_room

    # Vérifier si le PNJ est dans la salle actuelle
        for npc in current_room.npcs:
            if npc.name == nom_pnj:
                # Vérifier si le PNJ a un objet à offrir
                if npc.item_gift:
                    # Vérifier si le joueur possède l'objet requis
                    if npc.item_required and npc.item_required.name in player.inventory:
                        print(f"\n- {npc.name} : Merci pour {npc.item_required.name} ! Voici {npc.item_gift.name} en échange.")
                        # Effectuer l'échange
                        player.inventory[npc.item_gift.name] = npc.item_gift  # Ajouter l'objet donné au joueur
                        player.inventory.pop(npc.item_required.name)  # Retirer l'objet requis de l'inventaire du joueur
                        npc.item_gift = None  # L'objet a été donné, plus rien à offrir
                        return True
                    else:
                        print(f"\n- {npc.name} : Tu n'as pas {npc.item_required.name} ... Apporte-le-moi.")
                        return True
                else:
                    print(f"\n- {npc.name} : Je n'ai rien à échanger pour le moment.")
                    return True

        print(f"\nAucun PNJ nommé '{nom_pnj}' dans cette pièce.")
        return False
       