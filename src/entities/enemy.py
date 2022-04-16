from typing import Tuple


class Enemy:
    def __init__(self, health: int, cell_pos: Tuple[int, int], image_key: int, damage: int, exp_gain: int):
        self.health = health
        self.cell_pos = cell_pos
        self.image_key = image_key
        self.damage = damage
        self.exp_gain = exp_gain

    def move(self, hero, enemies, cells):
        pass
