""" Game class for the text-based adventure game. """
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from pnj import pnj
class Game:
    """ Game class for the text-based adventure game. """

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
        pharaon = Room("Pharaon", "Pharaon, dans une pièce majestueuse ornée d'or et de pierres précieuses, où le trône du Pharaon impose son aura.")
        self.rooms.append(pharaon)
        scribes = Room("Scribes", "Scribes, dans une pièce avec des rouleaux de papyrus et des hiéroglyphes couvrent les murs dans une ambiance studieuse et mystérieuse")
        self.rooms.append(scribes)
        tombeau = Room("Tombeau", "Tombeau, la où un sarcophage imposant repose au centre d’une pièce obscure et silencieuse")
        self.rooms.append(tombeau)
        couloir = Room("Couloir", "couloir,  dans une intersection, au dessus la salle des Hieroglyphes, sinon au sud le temple d'Horus vous attends")
        self.rooms.append(couloir)
        horus = Room("Horus", "Horus, Des colonnes immenses entourent une statue imposante d’Horus qui semble vous surveiller.")
        self.rooms.append(horus)
        isis = Room("isis", "Isis, Une crypte glaciale où des gravures racontent des légendes sacrées")
        self.rooms.append(isis)
        hieroglyphes = Room("Hiéroglyphes", "Hieroglyphes, dans la galerie de hiéroglyphes lumineux tapissent un long corridor qui murmure des secrets oubliés.")
        self.rooms.append(hieroglyphes)
        offrandes = Room("Offrandes", "Offrandes, dans une pièce où il y a des autels remplis d’objets rituels baignent dans une lumière mystique.")
        self.rooms.append(offrandes)
        pyramide = Room("Pyramide", "Pyramide, dans Une salle cachée, enfouie sous le sable, où une lumière lointaine guide votre chemin.")
        self.rooms.append(pyramide)
        labyrinthe = Room("Labyrinthe", "Labyrinthe, Un dédale oppressant gardé par des statues d’Anubis aux yeux rouges")
        self.rooms.append(labyrinthe)
        raakh = Room("Raakh", "Raakh ; dans une salle sombre, où le sol est fissuré par des éclats de lumière rouge sang. Une statue mutilée de Râ gît au sol, remplacée par un trône imposant, où Seth-Raakh vous attend, ses yeux flamboyants de malveillance.")
        self.rooms.append(raakh)
        # Create exits for rooms
        pharaon.exits = {"N" : scribes, "S" : None, "E": None, "O" : None}
        scribes.exits = {"N" : tombeau, "O" : None, "S" :pharaon , "E": None}
        tombeau.exits = {"S" : scribes, "O" : couloir, "N" : None, "E": None}
        couloir.exits = {"S" : horus ,"U" : hieroglyphes, "N" : None, "E": scribes}
        horus.exits = {"N" : couloir, "S" : isis , "O" : None, "E": None}
        isis.exits = {"N" : horus, "S" : hieroglyphes, "E": None, "O":None }
        hieroglyphes.exits = {"D" : couloir,"S" : offrandes, "O" : None, "N": None}
        offrandes.exits = {"N" : hieroglyphes, "E" : pyramide, "O":None, "S": None }
        pyramide.exits = {"N" : labyrinthe,"O" : offrandes, "S":None, "E": None }
        labyrinthe.exits = {"S" : pyramide, "E" :raakh, "N" : None, "O": None }
        raakh.exits = {"S" : None, "E" :None, "N" : None, "O": labyrinthe }
        # creer les items
        epee_lourde= Item("Epee_lourde","epee faite en lame de diamant",{"weight": 10, "protect": 5, "damage": 30})
        self.items.append(epee_lourde)
        scribes.inventory.add(epee_lourde)
        bouclier_robuste = Item("Bouclier_robuste", "Bouclier en acier renforcé", {"weight": 5, "protect": 5, "damage": 0})  # Pas de dégâts, Poids : 50
        self.items.append(bouclier_robuste)
        pyramide.inventory.add(bouclier_robuste)
        amulette = Item("Amulette", "Une amulette ancienne imprégnée de magie", {"weight": 1, "protect": 5, "damage": 0})
        self.items.append(amulette)
        couloir.inventory.add(amulette)
        potion = Item("Potion", "Une potion qui restaure 50 points de vie.", {"weight": 2, "protect": 5, "damage": 0})
        self.items.append(potion)
        couloir.inventory.add(potion)
        piece_or = Item("Piece_or", "Une pièce ancienne en or massif.", {"weight": 1, "protect": 5, "damage": 0})
        self.items.append(piece_or)
        insigne_sacre = Item("Insigne Sacré", "Un symbole de valeur pour les gardiens d’Anubis.", {"weight": 1, "protect": 5, "damage": 0})
        self.items.append(insigne_sacre)
        hieroglyphes.inventory.add(insigne_sacre)
        pomme = Item("Pomme", "Une pomme bien juteuse.", {"weight": 1, "protect": 5, "damage": 0})
        self.items.append(pomme)
        tombeau.inventory.add(pomme)
        # Création des PNJ
        pretresse = pnj("Prêtresse", "Une prêtresse mystérieuse gardant des secrets.",
                        ["Tout grand assasin est un bon marchand"],
                        ["Donne moi cette amulette, et je donnerai des informations "],
                        scribes, amulette, piece_or)
        self.pnj.append(pretresse)
        scribes.pnj[pretresse.name]=pretresse

        garde = pnj("Garde", "Un garde imposant qui ne laisse passer personne sans autorisation.",
            ["Qui es-tu ? Passe moi une pièce d'or et je te laisse passer."],
            ["Donne moi une pièce d'or, et je te laisserai passer."],
            couloir, piece_or, None)
        self.pnj.append(garde)
        couloir.pnj[garde.name]=garde
        Gardek = pnj("Gardek", "Un garde imposant qui ne laisse passer personne sans autorisation.",
            ["Qui es-tu ? Pour passer il faut me battre aux pierres feuilles ciseaux."],
            hieroglyphes, piece_or, None)
        self.pnj.append(Gardek)
        hieroglyphes.pnj[Gardek.name]=Gardek

        self.player = Player(input("\nEntrez votre nom : "))
        self.player.current_room = pharaon
    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Process the command entered by the player.
        Args:
            command_string (str): The command entered by the player.
        """
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
        """ Print the welcome message for the player. """
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
        """Condition for end game """
        raakh_room = next((room for room in self.rooms if room.name.lower() == "raakh"), None)
        if self.player.current_room.name == raakh_room.name:
            print("Vous êtes arrivé dans la salle de raakh ! Vous avez pu franchir toute la pyramide\n")
            return True
        if self.player.move_count > 25 :
            print("Vous avez pris trop de temps... Raakh est revenu\n")
            return True
        return False
    def play(self):
        """ Play the game. """
        self.setup()
        self.print_welcome()

        while not self.finished:
            # Obtenez la commande du joueur
            command = input("> ")
            self.process_command(command)
            if self.endgame():
                self.finished=True

def main():
    """ Main function to run the game. """
    # Create a game object and play the game
    Game().play()

if __name__ == "__main__":
    main()
