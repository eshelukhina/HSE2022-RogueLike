from typing import Tuple
from src.config import Config
from src.entities.armor import Armor
from src.entities.weapon import Weapon


class Hero:
    """
    Класс персонажа, которым управляет игрок
    """

    def __init__(self, *, health: int, max_health: int, exp: int, level: int,
                 cell_pos: Tuple[int, int], image_name: str, damage: int):
        self.health = health
        self.max_health = max_health
        self.exp = exp
        self.level = level
        self.cell_pos = cell_pos
        self.image_name = image_name
        self.damage = damage
        self.damage_taken_modifier = 0
        self.weapon = None
        self.armor = None

    def move(self, new_cell_pos: Tuple[int, int]) -> None:
        """
        Меняет расположение героя на карте

        :param new_cell_pos: новая позиция на карте
        :return: None
        """
        self.cell_pos = new_cell_pos

    def add_exp(self, exp: int) -> None:
        """
        Метод для добавления опыта

        :param exp: добавляемый опыт
        :return: None
        """
        self.exp += exp
        lvl_up = self.exp // Config.EXPERIENCE_TO_NEXT_LEVEL
        self.damage *= (1 + lvl_up * 0.1)
        self.level += lvl_up

    def equip_weapon(self, weapon: Weapon) -> None:
        """
        Метод для экипировки оружия

        :param weapon: оружие для экипировки
        :return: None
        """
        self.unequip_weapon()
        self.weapon = weapon
        self.damage += weapon.strength

    def unequip_weapon(self) -> None:
        """
        Метод для снятия оружия

        :return: None
        """
        if self.weapon is not None:
            self.damage -= self.weapon.strength
            self.weapon = None

    def equip_armor(self, armor: Armor) -> None:
        """
        Метод для экипировки брони

        :param armor: броня для экипировки
        :return: None
        """
        self.unequip_armor()
        self.armor = armor
        self.damage_taken_modifier = armor.defence

    def unequip_armor(self) -> None:
        """
        Метод для снятия брони

        :return: None
        """
        self.damage_taken_modifier = 0
        self.armor = None
