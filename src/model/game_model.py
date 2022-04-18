from typing import List, Dict, Tuple

from src.entities.cell import Cell
from src.entities.enemy import Enemy
from src.entities.hero import Hero


class GameModel:
    """
    Класс хранит все элементы карты: различные виды блоков, вражеских существ и героя
    """

    def __init__(self, cells_dict, hero, enemies, image_dict, inventory):
        self.cells_dict: Dict[Tuple[int, int]][Cell] = cells_dict
        self.hero: Hero = hero
        self.enemies: List[Enemy] = enemies
        self.image_dict: Dict[str, str] = image_dict
        self.inventory = inventory
