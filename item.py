"""Item class for the game."""


class Item:
    """
    Classe représentant un objet dans le jeu.

    Attributs :
        name (str) : Le nom de l'objet.
        description (str) : La description de l'objet.
        damage (int) : Les dégâts que l'objet peut infliger.
        protect (int) : La protection que l'objet peut offrir.
        weight (int) : Le poids de l'objet.
    """

    def __init__(self, name, description, attributes):
        """
        Initialise un nouvel objet.

        Args :
            name (str) : Le nom de l'objet.
            description (str) : Une description de l'objet.
            attributes (dict) : Dictionnaire contenant les attributs de l'objet :
                - damage (int) : Les dégâts infligés.
                - protect (int) : La protection offerte.
                - weight (int) : Le poids de l'objet.
        """
        self.name = name
        self.description = description
        self.damage = attributes.get("damage", 0)
        self.protect = attributes.get("protect", 0)
        self.weight = attributes.get("weight", 0)

    def __str__(self):
        """
        Retourne une chaîne de caractères décrivant l'objet.

        Returns :
            str : Une description détaillée de l'objet incluant son nom, sa description,
                  sa protection, ses dégâts, et son poids.
        """
        return (
            f"Il y a {self.name} : {self.description}, avec {self.protect} de protection, "
            f"{self.damage} de puissance, et {self.weight} de poids"
        )

    def __repr__(self):
        """
        Représentation technique (utile pour le débogage).

        Returns :
            str : Une représentation technique de l'objet avec ses attributs.
        """
        return (
            f"Item(name={self.name}, description={self.description}, "
            f"weight={self.weight}, protect={self.protect}, damage={self.damage})"
        )
