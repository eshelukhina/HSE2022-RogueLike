from typing import Tuple

import pygame

from src.model.game_model import GameModel


class GameView:
    """
    Класс ответственный за вывод на экран карты и других обьектов
    """
    BACKGROUND_COLOR = (0, 0, 0)
    images = None

    def __init__(self, window_size: Tuple[int, int], cell_size: Tuple[int, int]):
        self.screen = pygame.display.set_mode(window_size)
        self.cell_size = cell_size

    def __get_cell_screen_pos__(self, cell_pos: Tuple[int, int], cell_size: Tuple[int, int]):
        cell_width, cell_height = cell_size
        cell_pos_x, cell_pos_y = cell_pos
        return cell_pos_x * cell_width, cell_pos_y * cell_height

    def view_load(self, game_model: GameModel):
        """
        Выводит на экран переданные объекты
        :param game_model: обьекты карты
        :return: None
        """
        if self.images is None:
            raise ValueError('images is not set')
        self.screen.fill(self.BACKGROUND_COLOR)
        # draw cells
        cells = game_model.cells
        for cell_pos in cells:
            cell = cells[cell_pos]
            screen_pos = self.__get_cell_screen_pos__(cell_pos, self.cell_size)
            rect = pygame.rect.Rect(screen_pos, self.cell_size)
            image = self.images[cell.image_key]
            self.screen.blit(image, rect)
        # draw hero
        hero = game_model.hero
        print(hero.cell_pos)
        screen_pos = self.__get_cell_screen_pos__(hero.cell_pos, self.cell_size)
        rect = pygame.rect.Rect(screen_pos, self.cell_size)
        image = self.images[hero.image_key]
        self.screen.blit(image, rect)

        pygame.display.update()
