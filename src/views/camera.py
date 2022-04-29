from typing import Tuple

from pygame.math import Vector2


class Camera:

    def __init__(self, hero_pos: Tuple[int, int]):
        self.pos = Vector2(hero_pos)
        self.shift = Vector2(0, 0)

    def get_shift(self):
        return self.shift

    def set_shift(self, next_pos):
        self.shift = next_pos - self.pos
