import numpy as np
import os
import pygame

from typing import Tuple, Dict

from src.config import Config
from src.model.game_model import GameModel


def reddening(surf, alpha):
    assert 0 <= alpha <= 255
    redshade = pygame.Surface(surf.get_rect().size).convert_alpha()
    redshade.fill((255, 0, 0, alpha))
    alpha_basemask = pygame.surfarray.array_alpha(surf)
    alpha_redmask = pygame.surfarray.pixels_alpha(redshade)
    np.minimum(alpha_basemask, alpha_redmask, out=alpha_redmask)

    del alpha_redmask

    redsurf = surf.copy()
    redsurf.blit(redshade, (0, 0))
    return redsurf

class GameView:
    """
    Класс ответственный за вывод на экран карты и других обьектов
    """
    images = None
    BAR_WIDTH = Config.BLOCK_WIDTH * 3
    BAR_HEIGHT = Config.BLOCK_HEIGHT

    def __init__(self, *, window_size: Tuple[int, int], cell_size: Tuple[int, int], image_dict: Dict[str, str]):
        self.screen = pygame.display.set_mode(window_size)
        self.cell_size = cell_size
        self.images = {}
        for image_key in image_dict:
            path_to_image: str = image_dict[image_key]
            image = pygame.image.load(path_to_image)
            image = pygame.transform.scale(image, (Config.BLOCK_WIDTH, Config.BLOCK_WIDTH))
            image.set_colorkey(Config.Colors.WHITE)
            self.images[image_key] = image
        path_to_frame = os.path.join(Config.PATH_TO_TEXTURES, "frame.png")
        self.frame = pygame.image.load(path_to_frame)
        self.frame = pygame.transform.scale(self.frame, (self.BAR_WIDTH, self.BAR_HEIGHT))
        # TODO fix hardcode font size
        self.font = pygame.font.SysFont('Corbel', 25)

    def __get_cell_screen_pos__(self, cell_pos: Tuple[int, int], cell_size: Tuple[int, int]):
        cell_width, cell_height = cell_size
        cell_pos_x, cell_pos_y = cell_pos
        return cell_pos_x * cell_width, cell_pos_y * cell_height

    def __draw_bar__(self, pos: Tuple[int, int], fill: int, fill_color: Tuple[int, int, int],
                     main_color: Tuple[int, int, int], text: str):
        full_bar = pygame.rect.Rect(pos, (self.BAR_WIDTH, self.BAR_HEIGHT))
        fill_bar = pygame.rect.Rect(pos, (fill, self.BAR_HEIGHT))
        pygame.draw.rect(self.screen, main_color, full_bar)
        pygame.draw.rect(self.screen, fill_color, fill_bar)
        self.screen.blit(self.frame, pos)
        text_render = self.font.render(text, True, Config.Colors.WHITE)
        text_pos = pos[0] + (self.BAR_WIDTH - text_render.get_width()) / 2, \
                   pos[1] + (self.BAR_HEIGHT - text_render.get_height()) / 2
        self.screen.blit(text_render, text_pos)

    def __draw_health__(self, health: int, max_health: int):
        pos = 0, Config.WINDOW_SIZE[1] - self.BAR_HEIGHT
        fill = health / max_health * self.BAR_WIDTH
        self.__draw_bar__(pos, fill, Config.Colors.RED, Config.Colors.GREY, str(health))

    def __draw_exp__(self, exp: int):
        cur_exp = exp % Config.EXPERIENCE_TO_NEXT_LEVEL
        pos = Config.WINDOW_SIZE[0] - self.BAR_WIDTH, Config.WINDOW_SIZE[1] - self.BAR_HEIGHT
        fill = cur_exp / Config.EXPERIENCE_TO_NEXT_LEVEL * self.BAR_WIDTH
        level = exp // Config.EXPERIENCE_TO_NEXT_LEVEL
        self.__draw_bar__(pos, fill, Config.Colors.YELLOW, Config.Colors.GREY, str(level) + " lvl")

    def view_load(self, game_model: GameModel):
        """
        Выводит на экран переданные объекты
        :param game_model: обьекты карты
        :return: None
        """
        if self.images is None:
            raise ValueError('images is not set')
        self.screen.fill(Config.Colors.BACKGROUND_COLOR)
        # draw cells
        cells_dict = game_model.cells_dict
        for cell_pos in cells_dict:
            cell = cells_dict[cell_pos]
            screen_pos = self.__get_cell_screen_pos__(cell_pos, self.cell_size)
            rect = pygame.rect.Rect(screen_pos, self.cell_size)
            image = self.images[cell.image_key]
            self.screen.blit(image, rect)
        # draw hero
        hero = game_model.hero
        screen_pos = self.__get_cell_screen_pos__(hero.cell_pos, self.cell_size)
        rect = pygame.rect.Rect(screen_pos, self.cell_size)
        image = self.images[hero.image_key]
        self.screen.blit(image, rect)
        # draw enemies
        for enemy in game_model.enemies:
            screen_pos = self.__get_cell_screen_pos__(enemy.cell_pos, self.cell_size)
            rect = pygame.rect.Rect(screen_pos, self.cell_size)
            image = self.images[enemy.image_key].convert_alpha()
            if enemy.health < enemy.max_health:
                alpha = 100 * (1 - (enemy.health / float(enemy.max_health))) + 10
                image = reddening(image, alpha)
            self.screen.blit(image, rect)
        # draw health
        health = hero.health
        max_health = hero.max_health
        self.__draw_health__(health, max_health)
        # draw experience
        exp = hero.exp
        self.__draw_exp__(exp)

        pygame.display.update()
