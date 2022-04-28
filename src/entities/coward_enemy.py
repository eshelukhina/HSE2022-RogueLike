from typing import Tuple

from src.entities.cell import CellType
from src.entities.enemy import Enemy


def __get_dist__(cell_pos: Tuple[int, int], other_cell_pos):
    return abs(cell_pos[0] - other_cell_pos[0]) + abs(cell_pos[1] - other_cell_pos[1])


def __try_move__(next_pos, hero, enemies, cells) -> bool:
    if next_pos not in cells or cells[next_pos].cell_type == CellType.Wall:
        return False
    if len(list(filter(lambda e: e.cell_pos[0] == next_pos[0] and
                                 e.cell_pos[1] == next_pos[1], enemies))) > 0:
        return False
    if hero.cell_pos[0] == next_pos[0] and hero.cell_pos[1] == next_pos[1]:
        return False
    return True


class CowardEnemy(Enemy):
    def __init__(self, health, max_health: int, cell_pos, image_key: str, damage: int, exp_gain: int,
                 scare_radius: int):
        super().__init__(health, max_health, cell_pos, image_key, damage, exp_gain)
        self.scare_radius = scare_radius

    def move(self, hero, enemies, cells):
        cur_dist = __get_dist__(self.cell_pos, hero.cell_pos)
        if cur_dist <= 1:
            return
        cur_x, cur_y = self.cell_pos
        potential_positions = [
            (cur_x + 1, cur_y), (cur_x - 1, cur_y),
            (cur_x, cur_y + 1), (cur_x, cur_y - 1)
        ]
        potential_position_with_dist = []
        for pot_pos in potential_positions:
            pot_x, pot_y = pot_pos
            dist = __get_dist__(pot_pos, hero.cell_pos)
            potential_position_with_dist.append((pot_x, pot_y, dist))

        potential_position_with_dist = filter(
            lambda e: self.scare_radius >= e[2] > cur_dist,
            potential_position_with_dist
        )
        potential_position_with_dist = sorted(
            potential_position_with_dist, key=lambda e: -e[2]
        )
        for pot_pos_with_dist in potential_position_with_dist:
            pot_pos = pot_pos_with_dist[0], pot_pos_with_dist[1]
            if __try_move__(pot_pos, hero, enemies, cells):
                self.cell_pos = pot_pos
                return
