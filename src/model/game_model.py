from typing import List, Dict, Tuple

from src.entities.cell import Cell
from src.entities.enemy import Enemy
from src.entities.hero import Hero


class GameModel:
    """
    Класс хранит все элементы карты: различные виды блоков, вражеских существ и героя
    """

    def __init__(self, cells, hero, enemies):
        self.cells: Dict[Tuple[int, int]][Cell] = cells
        self.hero: Hero = hero
        self.enemies: List[Enemy] = enemies
