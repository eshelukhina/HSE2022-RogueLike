from typing import Tuple
from src.config import Config

class Hero:
    """
    Класс персонажа, которым управляет игрок
    """

    def __init__(self, *, health: int, max_health: int, exp: int, level: int,
                 cell_pos: Tuple[int, int], image_key: int, damage: int):
        self.health = health
        self.max_health = max_health
        self.exp = exp
        self.level = level
        self.cell_pos = cell_pos
        self.image_key = image_key
        self.damage = damage

    def move(self, new_cell_pos: Tuple[int, int]) -> None:
        """
        Меняет расположение героя на карте
        :param new_cell_pos: новая позиция на карте
        :return: None
        """
        self.cell_pos = new_cell_pos

    def add_exp(self, exp: int):
        self.exp += exp
        lvl_up = self.exp // Config.EXPERIENCE_TO_NEXT_LEVEL
        self.damage *= (1 + lvl_up * 0.1)
        self.level += lvl_up
