from src.entities.item import Item


class Weapon(Item):
    def __init__(self, name, strength, image):
        self.name = name
        self.strength = strength
        self.image = image
