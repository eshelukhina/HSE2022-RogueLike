from src.entities.item import Item


class Weapon(Item):
    """Класс, ответственный за оружие персонажа"""

    def __init__(self, name, strength, image):
        self.name = name
        self.strength = strength
        self.image = image
