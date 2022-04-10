from typing import List

from src.entities.cell import Cell
from src.entities.enemy import Enemy
from src.entities.entity import Entity
from src.entities.hero import Hero


class GameModel:
    """
    Хранит все элементы карты: различные виды блоков, вражеских существ и героя
    """

    def __init__(self, cells, hero, enemies):
        self.cells: List[Cell] = cells
        self.hero: Hero = hero
        self.enemies: List[Enemy] = enemies

    def get_all_entities(self) -> List[Entity]:
        """
        Получить все объекты
        :return: список всех элементов карты
        """
        return self.get_cells() + self.get_enemies() + ([] if self.hero is None else [self.hero])

    def get_cells(self) -> List[Cell]:
        """
        Получить элементы карты
        :return: список блоков карты
        """
        if self.cells is None:
            return []
        return self.cells

    def get_hero(self) -> Hero:
        """
        Получить главного героя
        :return: главный герой
        """
        return self.hero

    def get_enemies(self) -> List[Enemy]:
        """
        Получить всех вражеских существ
        :return: список вражеских существ
        """
        if self.enemies is None:
            return []
        return self.enemies
