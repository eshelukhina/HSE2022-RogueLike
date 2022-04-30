from typing import Tuple


class Chest:
    def __init__(self, image_name: str, cell_pos: Tuple[int, int]):
        self.image_name = image_name
        self.cell_pos = cell_pos
