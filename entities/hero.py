import pygame
from entities.entity import Entity


class Hero(Entity):
    """
    Класс персонажа, которым управляет игрок
    """
    def __init__(self, *, x: int, y: int, image):
        super().__init__(x, y, image)

    def move(self, shift_x, shift_y) -> None:

        """
        :param shift_x: дельта для сдвига по оси абсцисс
        :param shift_y: дельта для сдвига по оси ординат
        :return: None
        """
        self.rect.x += shift_x
        self.rect.y += shift_y
