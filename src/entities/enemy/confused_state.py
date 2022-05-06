import random

from pygame.math import Vector2

from src.entities.enemy.coward_state import __try_move__
from src.entities.enemy.enemy_state import EnemyState


class ConfusedState(EnemyState):
    """Класс, ответственный за тактику растерянного противника"""
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self):
        self.time = 3

    def move(self, enemy, hero, enemies, cells):
        self.time -= 1
        random.shuffle(self.movements)
        for move in self.movements:
            pos = tuple(Vector2(enemy.cell_pos) + Vector2(move))
            if __try_move__(pos, hero, enemies, cells):
                enemy.cell_pos = pos
                return
