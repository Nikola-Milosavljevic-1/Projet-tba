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
        exchange = Command("exchange", " <Nom du pnj> : echanger avec le PNJ", Actions.exchange,1)
        self.commands["exchange"] = exchange

        # Créer les salles
        Pharaon = Room("Pharaon", "Pharaon, dans une pièce majestueuse ornée d'or et de pierres précieuses, où le trône du Pharaon impose son aura.")
        self.rooms.append(Pharaon)
        Scribes = Room("Scribes", "Scribes, dans une pièce avec des rouleaux de papyrus et des hiéroglyphes couvrent les murs dans une ambiance studieuse et mystérieuse")
        self.rooms.append(Scribes)
        Tombeau = Room("Tombeau", "Tombeau, la où un sarcophage imposant repose au centre d’une pièce obscure et silencieuse")
        self.rooms.append(Tombeau)
        Couloir = Room("couloir", "couloir,  dans une intersection, au dessus la salle des Hieroglyphes, sinon au sud le temple d'Horus vous attends")
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
        Couloir.exits = {"S" : Horus ,"U" : Hieroglyphes, "N" : None, "E": None}
        Horus.exits = {"N" : Couloir, "S" : Isis , "O" : None, "E": None}
        Isis.exits = {"N" : Horus, "S" : Hieroglyphes, "E": None, "O":None }
        Hieroglyphes.exits = {"D" : Couloir,"S" : Offrandes, "O" : "mort", "N": None}
        Offrandes.exits = {"N" : Hieroglyphes, "E" : Pyramide, "O":None, "S": None }
        Pyramide.exits = {"N" : Labyrinthe,"O" : Offrandes, "S":None, "E": None }
        Labyrinthe.exits = {"S" : Pyramide, "E" :Raakh, "N" : None, "O": None }
        Raakh.exits = {"S" : None, "E" :None, "N" : None, "O": Labyrinthe }

        epee_lourde= Item("epee_lourde","epee faite en lame de diamant",weight=10, protect=5, damage=30)
        self.items.append(epee_lourde)
        Scribes.inventory.add(epee_lourde)
        Potion_de_soin = Item("Potion_de_soin", "Rend 50 points de vie", weight=1,protect=5, damage=0)  # Pas de dégâts, Poids : 5
        self.items.append(Potion_de_soin)
        Hieroglyphes.inventory.add(Potion_de_soin)
        Bouclier_robuste = Item("Bouclier_robuste", "Bouclier en acier renforcé", weight=5,protect=5, damage=0)  # Pas de dégâts, Poids : 50
        self.items.append(Bouclier_robuste)
        Pyramide.inventory.add(Bouclier_robuste)
        amulette = Item("Amulette d’Isis", "Une amulette ancienne imprégnée de magie.", weight=1,protect=5, damage=0)
        self.items.append(amulette)
        Isis.inventory.add(amulette)
        potion = Item("Potion de Soin", "Une potion qui restaure 50 points de vie.", weight=2,protect=5, damage=0)
        self.items.append(potion)
        Couloir.inventory.add(potion)
        piece_or = Item("Pièce d’Or", "Une pièce ancienne en or massif.", weight=1,protect=5, damage=0)
        self.items.append(piece_or)
        Offrandes.inventory.add(piece_or)
        epee_desert = Item("Épée du Désert", "Une arme légère mais tranchante.", weight=5,protect=5, damage=30)
        self.items.append(epee_desert)
        Offrandes.inventory.add(epee_desert)
        insigne_sacre = Item("Insigne Sacré", "Un symbole de valeur pour les gardiens d’Anubis.", weight=1,protect=5, damage=0)
        self.items.append(insigne_sacre)
        Hieroglyphes.inventory.add(insigne_sacre)
        carte_labyrinthe = Item("Carte du Labyrinthe", "Un guide pour traverser le labyrinthe.", weight=1,protect=5, damage=0)
        self.items.append(carte_labyrinthe)
        Tombeau.inventory.add(carte_labyrinthe)
        indice = Item("Indice", "Un conseil précieux pour résoudre l’énigme à venir.", weight=1,protect=5, damage=0)
        self.items.append(indice)
        Horus.inventory.add(indice)
        pomme = Item("Pomme", "Une pomme bien juteuse.", weight=1,protect=5, damage=0)
        self.items.append(pomme)
        Tombeau.inventory.add(pomme)
        

        # Création des PNJ
        pretresse = pnj("Prêtresse", "Une prêtresse mystérieuse gardant des secrets.", Scribes, amulette, pomme)
        self.pnj.append(pretresse)
        Scribes.pnj[pretresse.name]=pretresse
        marchand = pnj("Marchand", "Un marchand proposant des objets utiles.", Isis, epee_desert)
        self.pnj.append(marchand)
        Isis.pnj[marchand.name]=marchand
        esclave = pnj("Esclave", "Un ancien esclave reconnaissant pour sa liberté.",Offrandes)
        self.pnj.append(esclave)
        Offrandes.pnj[esclave.name]=Offrandes
        garde = pnj("Garde", "Un garde protecteur des trésors d’Anubis.",Scribes)
        self.pnj.append(garde)
        Couloir.pnj[garde.name]=garde
    
    
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
                "des gardiens, des énigmes, et des mystères ancestraux se dressent sur votre chemin. "
                "Trouvez des artefacts, déjouez les dangers et achevez votre cible avant que ses plans funestes ne se réalisent."
                 "Bonne chance, assassin !")
        #
        print(self.player.current_room.get_long_description())

    def endgame(self):
        if self.player.current_room.name == "raakh":
            print("Vous êtes arrivé dans la salle de raakh ! Vous avez pu franchir toute la pyramide\n")
            self.finished = True
            return True
        if self.player.current_room.name == "mort":
            print("Vous avez perdu")
            return True
        if self.player.move_count > 10 :
            self.finished = True
            print("Vous avez pris trop de temps... Raakh est revenu\n")
            return True


    def play(self):
        self.setup()
        self.print_welcome()

        while not self.finished:
            # Obtenez la commande du joueur
            command = input("> ")
            self.process_command(command)

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
