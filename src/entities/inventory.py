from src.entities.armor import Armor
from src.entities.weapon import Weapon


class Inventory:
    """Класс, ответственный за хранение предметов персонажа, получаемых из сундуков на карте"""
    def __init__(self):
        self.capacity = 12
        self.items = [None] * self.capacity
        self.equipped_weapon = -1
        self.equipped_armor = -1

    def add_item(self, item) -> None:
        """Добавить предмет в инвентарь
        :param item: предмет, подобранный из сундука"""
        try:
            index = self.items.index(None)
        except ValueError:
            return
        self.items[index] = item

    def discard_item(self, i) -> None:
        """Убрать предмет из инвентаря
        :param i: индекс предмета в инвентаре, который надо убрать из инвентаря"""
        if self.items[i] == Weapon:
            self.equipped_weapon = -1
        elif self.items[i] == Armor:
            self.equipped_armor = -1
        self.items[i] = None

    def equip_item(self, i) -> None:
        """Надеть предмет на персонажа из инвентаря
        :param i: индекс предметв инвентаре, который надо надеть на персонажа"""
        if isinstance(self.items[i], Weapon):
            self.equipped_weapon = i
        elif isinstance(self.items[i], Armor):
            self.equipped_armor = i

    def unequip_item(self, i) -> None:
        """Снять предмет с персонажа
        :param i: индекс предметв инвентаре, который надо снять с персонажа"""
        if isinstance(self.items[i], Weapon):
            self.equipped_weapon = -1
        elif isinstance(self.items[i], Armor):
            self.equipped_armor = -1
