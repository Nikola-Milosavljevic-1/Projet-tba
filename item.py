class Item :
    def __init__(self, name, description, damage, protect,weight):
        self.name=name
        self.strength=damage
        self.protect=protect
        self.description = description
        self.weight = weight
       
    def __str__(self):
        return f"Il y a {self.name} : , {self.description}, avec {self.protect} et {self.strength}, {self.weight}"
        pass
    def __repr__(self):
        """
        Représentation technique (utile pour le débogage).
        """
        return (f"Item(name={self.name}, description={self.description}, "
                f"weight={self.weight}, protect={self.protect}, damage={self.damage})")
    #instancier les objets

