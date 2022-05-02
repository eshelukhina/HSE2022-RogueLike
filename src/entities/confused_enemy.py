import random

from src.entities.coward_enemy import __try_move__
from src.entities.enemy import Enemy


class ConfusedEnemy(Enemy):
    """Класс, ответственный за тактику растерянного противника"""
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, enemy: Enemy):
        super().__init__(enemy.health, enemy.max_health, enemy.cell_pos, enemy.image_name, enemy.damage, enemy.exp_gain)
        self.enemy = enemy
        self.time = 3

    def move(self, hero, enemies, cells):
        self.time -= 1
        random.shuffle(self.movements)
        for move in self.movements:
            pos = self.cell_pos[0] + move[0], self.cell_pos[1] + move[1]
            if __try_move__(pos, hero, enemies, cells):
                self.cell_pos = pos
                return

    def get_enemy(self):
        """
        Метод, возвращающий моба до конфузии

        :return: None
        """
        self.enemy.health = self.health
        self.enemy.max_health = self.max_health
        self.enemy.cell_pos = self.cell_pos
        self.enemy.image_name = self.image_name
        self.enemy.damage = self.damage
        self.enemy.exp_gain = self.exp_gain
        return self.enemy
