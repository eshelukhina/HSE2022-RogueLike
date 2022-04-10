from typing import List, Tuple

import pygame

from entities.entity import Entity


class GameView:
    """
    Класс ответственен за вывод на экран карты и существ
    """
    BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, window_size: Tuple[int, int]):
        self.screen = pygame.display.set_mode(window_size)

    def view_load(self, entities: List[Entity]):
        """
        Выводит на экран переданные объекты
        :param entities: элементы карты
        :return: None
        """
        self.screen.fill(self.BACKGROUND_COLOR)
        for entity in entities:
            entity.draw(self.screen)
        pygame.display.update()
