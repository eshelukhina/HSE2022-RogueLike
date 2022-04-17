from typing import Tuple, List, Dict, Optional

from src.entities.cell import Cell
from src.entities.cell import CellType
from src.entities.enemy import Enemy
from src.entities.coward_enemy import __get_dist__
from src.handlers.game_handler import __fight__


class AggressiveEnemy(Enemy):
    def __init__(self, health: int, max_health: int, cell_pos, image_key: int, damage: int, exp_gain: int, attack_radius: int):
        super().__init__(health, max_health, cell_pos, image_key, damage, exp_gain)
        self.attack_radius = attack_radius

    def __get_next_pos__(self,
                         pos: Tuple[int, int],
                         hero_pos: Tuple[int, int],
                         num_steps: int,
                         enemies: List[Enemy],
                         cells: Dict[Tuple[int, int], Cell],
                         first_step: Optional[Tuple[int, int]]) -> Optional[Tuple[Tuple[int, int], int]]:
        if num_steps > self.attack_radius or pos not in cells or cells[pos].cell_type == CellType.Wall:
            return None
        for enemy in enemies:
            if enemy.cell_pos[0] == pos[0] and enemy.cell_pos[1] == pos[1]:
                return None
        if pos[0] == hero_pos[0] and pos[1] == hero_pos[1]:
            return first_step, num_steps
        step_left = self.__get_next_pos__((pos[0] - 1, pos[1]), hero_pos, num_steps + 1, enemies, cells,
                                          first_step if first_step is not None else (pos[0] - 1, pos[1]))
        step_right = self.__get_next_pos__((pos[0] + 1, pos[1]), hero_pos, num_steps + 1, enemies, cells,
                                           first_step if first_step is not None else (pos[0] + 1, pos[1]))
        step_up = self.__get_next_pos__((pos[0], pos[1] - 1), hero_pos, num_steps + 1, enemies, cells,
                                        first_step if first_step is not None else (pos[0], pos[1] - 1))
        step_down = self.__get_next_pos__((pos[0], pos[1] + 1), hero_pos, num_steps + 1, enemies, cells,
                                          first_step if first_step is not None else (pos[0], pos[1] + 1))
        steps = sorted(
            list(filter(lambda s: s is not None, [step_left, step_right, step_up, step_down])),
            key=lambda s: s[1])
        if not steps:
            return None
        return steps[0]

    def move(self, hero, enemies, cells):
        close_enemies = []
        for enemy in enemies:
            if enemy.cell_pos[0] != self.cell_pos[0] and enemy.cell_pos[1] != self.cell_pos[1] and \
                    __get_dist__(self.cell_pos, enemy.cell_pos) <= self.attack_radius:
                close_enemies.append(enemy)
        next_step = \
            self.__get_next_pos__((self.cell_pos[0], self.cell_pos[1]), hero.cell_pos, 0, close_enemies, cells, None)
        if next_step is not None:
            next_pos = next_step[0]
            if next_pos[0] == hero.cell_pos[0] and next_pos[1] == hero.cell_pos[1]:
                __fight__(hero, self)
            else:
                self.cell_pos = next_pos
