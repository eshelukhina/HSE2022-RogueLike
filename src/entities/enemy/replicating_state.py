import copy
import random
from typing import List, Dict, Tuple, Optional

from pygame.math import Vector2

from src.entities.cell import Cell
from src.entities.enemy.coward_state import __try_move__
from src.entities.enemy.enemy import Enemy
from src.entities.enemy.enemy_state import EnemyState
from src.entities.hero import Hero
from src.handlers.game_handler import GameHandler


class ReplicatingState(EnemyState):
    """Класс, ответственный за тактику реплицируещегося моба"""

    def __init__(self, chance_of_cloning: float):
        self.chance_of_cloning = chance_of_cloning

    def __get_next_position__(self, enemy: Enemy, hero: Hero, enemies: List[Enemy],
                              cells: Dict[Tuple[int, int], Cell]) -> Optional[Tuple[int, int]]:
        positions = []
        for move in GameHandler.movement.values():
            next_pos = Vector2(enemy.cell_pos) + Vector2(move)
            if __try_move__(tuple(next_pos), hero, enemies, cells):
                positions.append(tuple(next_pos))
        if positions:
            return positions[random.randint(0, len(positions) - 1)]
        else:
            return None

    def move(self, enemy: Enemy, hero: Hero, enemies: List[Enemy], cells: Dict[Tuple[int, int], Cell]):
        next_pos = self.__get_next_position__(enemy, hero, enemies, cells)
        if next_pos and self.chance_of_cloning > random.random():
            enemies.append(self.clone(enemy=enemy, cell_pos=next_pos))

    def clone(self, **attr) -> Enemy:
        """
        Создание клона моба

        :param attr: дополнительные параметры для создания клона
        :return: Enemy
        """
        clone = copy.deepcopy(attr['enemy'])
        clone.__dict__.update(attr)
        return clone
