from typing import Tuple

from pygame.math import Vector2

from src.config import Config


class Camera:
    """
    Класс, отвечающий за позицию камеры
    """

    def __init__(self, hero_pos: Tuple[int, int]):
        center = Vector2(Config.WINDOW_SIZE) / 2
        self.pos = center
        self.shift = center - Vector2(hero_pos)

    def get_shift(self) -> Vector2:
        """
        Метод для получения смещения камеры

        :return: смещение камеры
        """
        return self.shift

    def change_shift(self, next_pos: Vector2) -> None:
        """
        Метод для изменения смещения камеры

        :param next_pos: новая позиция героя
        :return: None
        """
        self.shift = next_pos - self.pos
