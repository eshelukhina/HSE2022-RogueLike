from typing import Tuple


class Enemy:
    """Интерфейс для противников"""
    def __init__(self, health: int, max_health: int, cell_pos: Tuple[int, int],
                 image_name: str, damage: int, exp_gain: int):
        self.health = health
        self.max_health = max_health
        self.cell_pos = cell_pos
        self.image_name = image_name
        self.damage = damage
        self.exp_gain = exp_gain

    def move(self, hero, enemies, cells):
        pass
