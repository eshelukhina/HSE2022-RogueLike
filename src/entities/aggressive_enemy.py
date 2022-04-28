from typing import Tuple, List, Dict, Optional

from src.entities.cell import Cell
from src.entities.cell import CellType
from src.entities.coward_enemy import __get_dist__
from src.entities.enemy import Enemy
from src.handlers.game_handler import __fight__


class AggressiveEnemy(Enemy):
    def __init__(self, health: int, max_health: int, cell_pos, image_key: str, damage: int, exp_gain: int,
                 attack_radius: int):
        super().__init__(health, max_health, cell_pos, image_key, damage, exp_gain)
        self.attack_radius = attack_radius

    def __try_move__(self, num_steps: int, pos: Tuple[int, int], enemies: List[Enemy],
                     cells: Dict[Tuple[int, int], Cell]) -> bool:
        if num_steps > self.attack_radius or pos not in cells or cells[pos].cell_type == CellType.Wall:
            return False
        for enemy in enemies:
            if enemy.cell_pos[0] == pos[0] and enemy.cell_pos[1] == pos[1]:
                return False
        return True

    def __get_next_pos__(self,
                         pos: Tuple[int, int],
                         hero_pos: Tuple[int, int],
                         num_steps: int,
                         enemies: List[Enemy],
                         cells: Dict[Tuple[int, int], Cell],
                         first_step: Optional[Tuple[int, int]]) -> Optional[Tuple[Tuple[int, int], int]]:
        if not self.__try_move__(num_steps, pos, enemies, cells):
            return None
        if pos[0] == hero_pos[0] and pos[1] == hero_pos[1]:
            return first_step, num_steps
        potential_positions = [
            (pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)
        ]
        if first_step is None:
            results_of_steps = [
                self.__get_next_pos__(pot_pos, hero_pos, num_steps + 1, enemies, cells, pot_pos)
                for pot_pos in potential_positions
            ]
        else:
            results_of_steps = [
                self.__get_next_pos__(pot_pos, hero_pos, num_steps + 1, enemies, cells, first_step)
                for pot_pos in potential_positions
            ]
        steps = sorted(
            list(filter(lambda step: step is not None, results_of_steps)),
            key=lambda s: s[1]
        )
        return steps[0] if steps else None

    def move(self, hero, enemies, cells):
        close_enemies = []
        for enemy in enemies:
            dist = __get_dist__(self.cell_pos, enemy.cell_pos)
            if 0 < dist <= self.attack_radius:
                close_enemies.append(enemy)
        next_step = self.__get_next_pos__(
            (self.cell_pos[0], self.cell_pos[1]), hero.cell_pos, 0, close_enemies, cells, None
        )
        if next_step is not None:
            next_pos = next_step[0]
            if next_pos[0] == hero.cell_pos[0] and next_pos[1] == hero.cell_pos[1]:
                __fight__(hero, self)
            else:
                self.cell_pos = next_pos
