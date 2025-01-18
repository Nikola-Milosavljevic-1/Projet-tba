
import random

class pnj : 
    
   def __init__(self, name, description, msgs, room=None, item=None, gift=None):
        
      self.name = name
      self.description = description
      self.current_room = room
      self.dialogue = []
      self.msgs = []
      self.item_required = item
      self.item_gift = gift

   def __str__(self):
      """
        Retourne une représentation sous forme de chaîne de caractères du personnage.

        Returns :
            str : Une description formatée du personnage.
      """
      return  f"{self.name} : {self.description}"
   def __repr__(self):
        """
        Représentation technique (utile pour le débogage).
        """
        return (f"Item(name={self.name}, description={self.description}, "
                f"weight={self.weight}, protect={self.protect}, damage={self.damage})")
   
   def move(self):
      """
         Déplace le personnage aléatoirement dans une salle adjacente, si possible.

         Le personnage reste dans la salle actuelle ou se déplace vers une salle
         adjacente choisie aléatoirement si des sorties sont disponibles.

         Returns :
            bool : True si le personnage se déplace dans une autre salle, False sinon.
      """
      deplacement = random.choice(["bouge","reste"])
      sorties = self.current_room.exits
      if not sorties :
            return False
      deplacement = random.choice(["bouge","bouge"])
      sorties = self.current_room.exits
      if not sorties :
         return False
      if deplacement == "bouge":
         direction = random.choice(list(sorties.keys()))
         next_room = self.current_room.exits[direction]
         if type(next_room) == str :
            print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
            return False
         if self.name in self.current_room.pnj:
            del self.current_room.pnj[self.name]
         self.current_room = next_room
         next_room.pnj[self.name]=self
         print(f"{self.name} se trouve maintenant dans {self.current_room.name}\n")
         return True
      print(f"{self.name} se trouve encore dans {self.current_room.name}\n")
      return False

   def get_msg(self, player) :
      """
        Récupère un message du personnage en fonction de l'inventaire du joueur.

        Si le personnage est un "Chomeur" et qu'il nécessite un objet pour interagir,
        la réponse varie en fonction de la possession ou non de l'objet requis.
        Sinon, les messages standards du personnage sont renvoyés de manière cyclique.

        Args :
            player (Player) : Le joueur interagissant avec le personnage.

        Returns :
            str : Le message que le personnage dit.
      """
      msg = self.msgs.pop(0)
      self.msgs.append(msg)
      return msg
