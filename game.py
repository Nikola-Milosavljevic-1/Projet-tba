# Description: Game class

# Import modules
import random
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from pnj import pnj
class Game:

    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = []
        self.pnj = []

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
        Back= Command("back", " : retourner à la pièce précédente", Actions.back, 0)
        self.commands["back"] = Back
        look= Command("look", " : Vous regardez autour de vous", Actions.look, 0)
        self.commands["look"] = look
        take= Command("take", " : prendre", Actions.Take, 1)
        self.commands["take"] = take
        drop= Command("drop", " : Enlever de votre inventaire", Actions.Drop, 1)
        self.commands["drop"] = drop
        check= Command("check", " : Regarder votre inventaire", Actions.Check, 0)
        self.commands["check"] = check
        talk = Command("talk", " <Nom du pnj> : parler avec le PNJ", Actions.talk,1)
        self.commands["talk"] = talk
        exchange = Command("exchange", " <Nom du pnj> : echanger avec le PNJ", Actions.exchange,2)
        self.commands["exchange"] = exchange

        # Créer les salles
        Pharaon = Room("Pharaon", "Pharaon, dans une pièce majestueuse ornée d'or et de pierres précieuses, où le trône du Pharaon impose son aura.")
        self.rooms.append(Pharaon)
        Scribes = Room("Scribes", "Scribes, dans une pièce avec des rouleaux de papyrus et des hiéroglyphes couvrent les murs dans une ambiance studieuse et mystérieuse")
        self.rooms.append(Scribes)
        Tombeau = Room("Tombeau", "Tombeau, la où un sarcophage imposant repose au centre d’une pièce obscure et silencieuse")
        self.rooms.append(Tombeau)
        Couloir = Room("Couloir", "couloir,  dans une intersection, au dessus la salle des Hieroglyphes, sinon au sud le temple d'Horus vous attends")
        self.rooms.append(Couloir)
        Horus = Room("Horus", "Horus, Des colonnes immenses entourent une statue imposante d’Horus qui semble vous surveiller.")
        self.rooms.append(Horus)
        Isis = Room("Isis", "Isis, Une crypte glaciale où des gravures racontent des légendes sacrées")
        self.rooms.append(Isis)
        Hieroglyphes = Room("Hiéroglyphes", "Hieroglyphes, dans la galerie de hiéroglyphes lumineux tapissent un long corridor qui murmure des secrets oubliés.")
        self.rooms.append(Hieroglyphes)
        Offrandes = Room("Offrandes", "Offrandes, dans une pièce où il y a des autels remplis d’objets rituels baignent dans une lumière mystique.")
        self.rooms.append(Offrandes)
        Pyramide = Room("Pyramide", "Pyramide, dans Une salle cachée, enfouie sous le sable, où une lumière lointaine guide votre chemin.")
        self.rooms.append(Pyramide)
        Labyrinthe = Room("Labyrinthe", "Labyrinthe, Un dédale oppressant gardé par des statues d’Anubis aux yeux rouges")
        self.rooms.append(Labyrinthe)
        Raakh = Room("Raakh", "Raakh ; dans une salle sombre, où le sol est fissuré par des éclats de lumière rouge sang. Une statue mutilée de Râ gît au sol, remplacée par un trône imposant, où Seth-Raakh vous attend, ses yeux flamboyants de malveillance.")
        self.rooms.append(Raakh)
        # creer les items
        # Create exits for rooms
        Pharaon.exits = {"N" : Scribes, "S" : None, "E": None, "O" : None}
        Scribes.exits = {"N" : Tombeau, "O" : None, "S" :Pharaon , "E": None}
        Tombeau.exits = {"S" : Scribes, "O" : Couloir, "N" : None, "E": None}
        Couloir.exits = {"S" : Horus ,"U" : Hieroglyphes, "N" : None, "E": Scribes}
        Horus.exits = {"N" : Couloir, "S" : Isis , "O" : None, "E": None}
        Isis.exits = {"N" : Horus, "S" : Hieroglyphes, "E": None, "O":None }
        Hieroglyphes.exits = {"D" : Couloir,"S" : Offrandes, "O" : "mort", "N": None}
        Offrandes.exits = {"N" : Hieroglyphes, "E" : Pyramide, "O":None, "S": None }
        Pyramide.exits = {"N" : Labyrinthe,"O" : Offrandes, "S":None, "E": None }
        Labyrinthe.exits = {"S" : Pyramide, "E" :Raakh, "N" : None, "O": None }
        Raakh.exits = {"S" : None, "E" :None, "N" : None, "O": Labyrinthe }

        epee_lourde= Item("Epee_lourde","epee faite en lame de diamant",weight=10, protect=5, damage=30)
        self.items.append(epee_lourde)
        Scribes.inventory.add(epee_lourde)
        Bouclier_robuste = Item("Bouclier_robuste", "Bouclier en acier renforcé", weight=5,protect=5, damage=0)  # Pas de dégâts, Poids : 50
        self.items.append(Bouclier_robuste)
        Pyramide.inventory.add(Bouclier_robuste)
        amulette = Item("Amulette", "Une amulette ancienne imprégnée de magie", weight=1,protect=5, damage=0)
        self.items.append(amulette)
        Couloir.inventory.add(amulette)
        potion = Item("Potion", "Une potion qui restaure 50 points de vie.", weight=2,protect=5, damage=0)
        self.items.append(potion)
        Couloir.inventory.add(potion)
        Piece_or = Item("Piece_or", "Une pièce ancienne en or massif.", weight=1,protect=5, damage=0)
        self.items.append(Piece_or)
        insigne_sacre = Item("Insigne Sacré", "Un symbole de valeur pour les gardiens d’Anubis.", weight=1,protect=5, damage=0)
        self.items.append(insigne_sacre)
        Hieroglyphes.inventory.add(insigne_sacre)
        pomme = Item("Pomme", "Une pomme bien juteuse.", weight=1,protect=5, damage=0)
        self.items.append(pomme)
        Tombeau.inventory.add(pomme)
        # Création des PNJ
        pretresse = pnj("Prêtresse", "Une prêtresse mystérieuse gardant des secrets.", 
                        ["Tout grand assasin est un bon marchand"],
                        ["Donne moi cette amulette, et je donnerai des informations "],
                        Scribes, amulette, Piece_or)
        self.pnj.append(pretresse)
        Scribes.pnj[pretresse.name]=pretresse

        garde = pnj("Garde", "Un garde rodant..", 
                        ["Qui es tu"],
                        ["Donne moi une piece d'or, et je te laisse passer"],
                        Couloir, Piece_or, None)
        self.pnj.append(garde)
        Couloir.pnj[garde.name]=garde
        
        Gardek = pnj("Gardek", "Un garde imposant qui ne laisse passer personne sans autorisation.",
            ["Qui es-tu ? Pour passer il faut me battre aux pierres feuilles ciseaux."],
            Hieroglyphes, Piece_or, None)
        self.pnj.append(Gardek)
        Hieroglyphes.pnj[Gardek.name]=Gardek

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
        print("Vous êtes un assassin envoyé dans l'une des pyramides sacrées de Gizeh pour accomplir une mission périlleuse. "
              "Votre cible : Seth-Raakh, un chef de culte maléfique qui menace de plonger le monde dans le chaos."
                "Les passages sombres et les pièges anciens des pyramides ne sont pas vos seuls ennemis : "
                "Rejoignez la salle Raakh avant qu'il n'arrive, vous avez environ le temps de 20 déplacements avant qu'il arrive"
                 "Bonne chance, assassin !")
        #
        print(self.player.current_room.get_long_description())

    def endgame(self):
        raakh_room = next((room for room in self.rooms if room.name.lower() == "raakh"), None)
        if self.player.current_room.name == raakh_room.name: 
            print("Vous êtes arrivé dans la salle de raakh ! Vous avez pu franchir toute la pyramide\n")
            return True
        if self.player.current_room.name == "mort":
            print("Vous avez perdu")
            return True
        if self.player.move_count > 25 :
            print("Vous avez pris trop de temps... Raakh est revenu\n")
            return True
        return False


    def play(self):
        self.setup()
        self.print_welcome()

        while not self.finished:
            # Obtenez la commande du joueur
            command = input("> ")
            self.process_command(command)
            if self.endgame():
                self.finished=True

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
