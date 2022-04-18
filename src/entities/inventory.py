from src.entities.armor import Armor
from src.entities.weapon import Weapon


class Inventory:
    def __init__(self):
        self.capacity = 12
        self.items = [None] * self.capacity
        self.equipped_weapon = -1
        self.equipped_armor = -1

    def add_item(self, item):
        try:
            index = self.items.index(None)
        except ValueError:
            return
        self.items[index] = item

    def discard_item(self, i):
        if self.items[i] == Weapon:
            self.equipped_weapon = -1
        elif self.items[i] == Armor:
            self.equipped_armor = -1
        self.items[i] = None

    def equip_item(self, i):
        if self.items[i] == Weapon:
            self.equipped_weapon = i
        elif self.items[i] == Armor:
            self.equipped_armor = i
