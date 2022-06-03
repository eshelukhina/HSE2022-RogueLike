from typing import List, Dict, Tuple

from src.entities.cell import Cell
from src.entities.enemy.enemy import Enemy
from src.entities.hero import Hero
from src.entities.chest import Chest
from src.entities.inventory import Inventory


class GameModel:
    """
    Класс хранит все элементы карты: различные виды блоков, вражеских существ и героя
    """

    def __init__(
            self, *, hero: Hero, enemies: List[Enemy], chests: List[Chest], inventory: Inventory,
            cells_dict: Dict[Tuple[int, int], Cell], image_dict: Dict[str, str]):
        self.cells_dict = cells_dict
        self.hero = hero
        self.enemies = enemies
        self.image_dict = image_dict
        self.inventory = inventory
        self.chests = chests
