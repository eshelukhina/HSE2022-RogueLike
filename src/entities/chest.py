from typing import Tuple


class Chest:
    def __init__(self, image_key: str, cell_pos: Tuple[int, int]):
        self.image_key = image_key
        self.cell_pos = cell_pos
