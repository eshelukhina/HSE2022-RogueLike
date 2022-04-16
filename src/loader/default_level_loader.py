import json
import os
from typing import Dict

import pygame.image

from src.entities.cell import Cell, CellType
from src.entities.hero import Hero
from src.model.game_model import GameModel
from src.views.game_view import GameView


class DefaultLeverLoader:
    """
        Класс DefaultLeverLoader ответственен за загрузку уровеней.
        Извлекает необходмую информацию из json файлов согласно внутреннему инварианту.
    """
    PATH_TO_LEVELS = "levels"
    PATH_TO_TEXTURES = "textures"
    CELL_TYPES_DICT = {
        '0': CellType.Empty,
        '1': CellType.Wall
    }

    def __load_cells__(self, info):
        num_cells_width = info['cells_amount'][0]
        num_cells_height = info['cells_amount'][1]
        cell_types = info['map']['cell_types']
        cell_images = info['map']['cell_images']
        cells = {}
        for i in range(num_cells_height):
            for j in range(num_cells_width):
                curr = i * num_cells_width + j
                image_key = cell_images[curr]
                type_id = cell_types[curr]
                cell_type = self.CELL_TYPES_DICT[type_id]
                cells[(j, i)] = Cell(cell_type=cell_type, image_key=image_key)
        return cells

    def __load_hero__(self, info) -> Hero:
        hero_info = info['hero']
        hero_cell_pos = hero_info['position'][0], hero_info['position'][1]
        image_key = hero_info['image_key']
        return Hero(cell_pos=hero_cell_pos, image_key=image_key)

    def __load_enemies__(self):
        raise NotImplemented()

    def __load_images__(self, info) -> Dict[str, pygame.Surface]:
        images_info = info['images']
        images = {}
        for image_key in images_info:
            path_to_image = os.path.join(self.PATH_TO_TEXTURES, images_info[image_key])
            image = pygame.image.load(path_to_image)
            images[image_key] = image
        return images

    def load(self, level_name: str) -> GameModel:
        """
        Конструирует и возвращает модель уровня, загружает все необходимые
        картинки в GameView.
        :param level_name: название уровня
        :return: модель уровня, содержащую все считаные из файла обьекты
        """
        level_file = os.path.join(self.PATH_TO_LEVELS, level_name + '.json')
        with open(level_file, 'r') as level:
            info = json.load(level)
            cells = self.__load_cells__(info)
            hero = self.__load_hero__(info)
            # load images into view
            GameView.images = self.__load_images__(info)
        return GameModel(cells, hero, None)
