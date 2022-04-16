from typing import Tuple


class Hero:
    """
    Класс персонажа, которым управляет игрок
    """

    def __init__(self, *, cell_pos: Tuple[int, int], image_key: int):
        self.cell_pos = cell_pos
        self.image_key = image_key

    def move(self, new_cell_pos: Tuple[int, int]) -> None:
        """
        Меняет расположение героя на карте
        :param new_cell_pos: новая позиция на карте
        :return: None
        """
        self.cell_pos = new_cell_pos
