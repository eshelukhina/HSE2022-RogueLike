from src.entities.item import Item


class Armor(Item):
    """Класс, ответственный за броню персонажа"""

    def __init__(self, name, defence, image):
        self.name = name
        self.defence = defence
        self.image = image
