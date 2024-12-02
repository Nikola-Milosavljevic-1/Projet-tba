# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        # Définir les commandes
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history", ":Afficher toutes les pièces que vous avez fait", Actions.history, 1)
        self.commands["history"] = history

        # Créer les salles
    
        Pharaon = Room("Pharaon", "dans une pièce majestueuse ornée d'or et de pierres précieuses, où le trône du Pharaon impose son aura.")
        self.rooms.append(Pharaon)
        Scribes = Room("Scribes", "dans une pièce avec des rouleaux de papyrus et des hiéroglyphes couvrent les murs dans une ambiance studieuse et mystérieuse")
        self.rooms.append(Scribes)
        Tombeau = Room("Tombeau", "la où un sarcophage imposant repose au centre d’une pièce obscure et silencieuse")
        self.rooms.append(Tombeau)
        Couloir = Room("couloir", " dans une intersection, au dessus la salle des Hieroglyphes, sinon au sud le temple d'Horus vous attends")
        self.rooms.append(Couloir)
        Horus = Room("Horus", "Des colonnes immenses entourent une statue imposante d’Horus qui semble vous surveiller.")
        self.rooms.append(Horus)
        Isis = Room("Isis", "Une crypte glaciale où des gravures racontent des légendes sacrées")
        self.rooms.append(Isis)
        Hieroglyphes = Room("Hiéroglyphes", "dans la galerie de hiéroglyphes lumineux tapissent un long corridor qui murmure des secrets oubliés.")
        self.rooms.append(Hieroglyphes)
        Offrandes = Room("Offrandes", "dans une pièce où il y a des autels remplis d’objets rituels baignent dans une lumière mystique.")
        self.rooms.append(Offrandes)
        Pyramide = Room("Pyramide", "dans Une salle cachée, enfouie sous le sable, où une lumière lointaine guide votre chemin.")
        self.rooms.append(Pyramide)
        Labyrinthe = Room("Labyrinthe", "Un dédale oppressant gardé par des statues d’Anubis aux yeux rouges")
        self.rooms.append(Labyrinthe)
        Raakh = Room("Raakh", "dans une salle sombre, où le sol est fissuré par des éclats de lumière rouge sang. Une statue mutilée de Râ gît au sol, remplacée par un trône imposant, où Seth-Raakh vous attend, ses yeux flamboyants de malveillance.")
        self.rooms.append(Raakh)

        # Create exits for rooms

        Pharaon.exits = {"N" : Scribes, "S" : None, "E": None, "O" : None}
        Scribes.exits = {"N" : Tombeau, "O" : None, "S" :Pharaon , "E": None}
        Tombeau.exits = {"S" : Scribes, "O" : Couloir, "N" : None, "E": None}
        Couloir.exits = {"S" : Horus ,"U" : Hieroglyphes, "N" : None, "E": None}
        Horus.exits = {"N" : Couloir, "S" : Isis , "O" : None, "E": None}
        Isis.exits = {"N" : Horus, "S" : None, "E": None, "O":None }
        Hieroglyphes.exits = {"D" : Couloir,"S" : Offrandes, "O" : "mort", "N": None}
        Offrandes.exits = {"N" : Hieroglyphes, "E" : Pyramide, "O":None, "S": None }
        Pyramide.exits = {"N" : Labyrinthe,"O" : Offrandes, "S":None, "E": None }
        Labyrinthe.exits = {"S" : Pyramide, "E" :Raakh, "N" : None, "O": None }
        Raakh.exits = {"S" : None, "E" :None, "N" : None, "O": Labyrinthe }


        # Configurer les sorties

        # Configurer le joueur
        self.player = Player(input("\nEntrez votre nom : "))
        self.player.current_room = Pharaon

    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        #Affiche rien lorsque le joueur tape "entrer"
        if command_string=='':
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
