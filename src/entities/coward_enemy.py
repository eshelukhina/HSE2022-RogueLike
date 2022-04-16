from src.entities.cell import CellType
from src.entities.enemy import Enemy


class CowardEnemy(Enemy):
    def __init__(self, health, cell_pos, image_key: int, damage: int, exp_gain: int, scare_radius: int):
        super().__init__(health, cell_pos, image_key, damage, exp_gain)
        self.scare_radius = scare_radius

    def __try_move__(self, next_pos, enemies, cells) -> bool:
        if next_pos not in cells or cells[next_pos].cell_type == CellType.Wall:
            return False
        if len(list(filter(lambda e: e.cell_pos[0] == next_pos[0] and
                                     e.cell_pos[1] == next_pos[1], enemies))) > 0:
            return False
        self.cell_pos = next_pos
        return True

    def move(self, hero, enemies, cells):
        diff_x = hero.cell_pos[0] - self.cell_pos[0]
        diff_y = hero.cell_pos[1] - self.cell_pos[1]
        dist = abs(diff_x) + abs(diff_y)
        if dist > self.scare_radius:
            return
        # todo sort priorities and try to run in that order
        run_x = 1 if diff_x < 0 else -1
        run_y = 1 if diff_y < 0 else -1
        if abs(diff_x) <= abs(diff_y):
            move_to = (self.cell_pos[0] + run_x, self.cell_pos[1])
            if self.__try_move__(move_to, enemies, cells):
                return
        move_to = (self.cell_pos[0], self.cell_pos[1] + run_y)
        self.__try_move__(move_to, enemies, cells)
