import pygame.image

from model.game_model import GameModel

from typing import List
from entities.hero import Hero
from entities.cell import Cell, CellType

import json
import os


class DefaultLeverLoader:
    PATH_TO_LEVELS = "levels"
    PATH_TO_TEXTURES = 'textures'

    def __init__(self, *, block_width, block_height):
        self.block_width = block_width
        self.block_height = block_height

    def __load_cells__(self, info) -> List[Cell]:
        block_width = info['block_width']
        block_height = info['block_height']
        num_blocks_width = info['blocks_amount'][0]
        num_blocks_height = info['blocks_amount'][1]
        cells = []
        for i in range(num_blocks_height):
            for j in range(num_blocks_width):
                cell_id = info['map'][i * num_blocks_width + j]
                pos_x = j * block_width
                pos_y = i * block_height
                if cell_id == '0':
                    cell_type = CellType.Empty
                elif cell_id == '1':
                    cell_type = CellType.Wall
                else:
                    raise ValueError(f'Not known cell_id provided: {cell_id}')
                image_name = os.path.join(self.PATH_TO_TEXTURES, info['block_image'][cell_id])
                cell_image = pygame.image.load(image_name)
                cells.append(Cell(x=pos_x, y=pos_y, cell_type=cell_type, image=cell_image))
        return cells

    def __load_hero__(self, info) -> Hero:
        block_width = info['block_width']
        block_height = info['block_height']

        hero_info = info['hero']
        hero_pos_x = hero_info['position'][0] * block_width
        hero_pos_y = hero_info['position'][1] * block_height
        image_name = os.path.join(self.PATH_TO_TEXTURES, hero_info['image'])
        hero_image = pygame.image.load(image_name)
        return Hero(x=hero_pos_x, y=hero_pos_y, image=hero_image)

    def __load_enemies__(self):
        raise NotImplemented()

    def load(self, level_name: str) -> GameModel:
        level_file = os.path.join(self.PATH_TO_LEVELS, level_name + '.json')
        with open(level_file, 'r') as level:
            info = json.load(level)
            cells = self.__load_cells__(info)
            hero = self.__load_hero__(info)
        return GameModel(cells, hero, None)
