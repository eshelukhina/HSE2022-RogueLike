import json
import os
from typing import Dict, Tuple

from src.entities.aggressive_enemy import AggressiveEnemy
from src.entities.cell import Cell, CellType
from src.entities.chest import Chest
from src.entities.coward_enemy import CowardEnemy
from src.entities.enemy import Enemy
from src.entities.hero import Hero
from src.entities.inventory import Inventory
from src.entities.passive_enemy import PassiveEnemy
from src.model.game_model import GameModel
from src.fabrics.fantasy_enemy_factory import FantasyEnemyFactory
from src.fabrics.abstract_enemy_factory import AbstractEnemyFactory


def __load_base_enemy_info__(enemy_info):
    return (enemy_info['health'], (enemy_info['position'][0], enemy_info['position'][1]),
            enemy_info['fabric'], enemy_info['damage'], enemy_info['exp_gain'])


def __load_passive_enemy__(enemy_info, fabrics: Dict[str, AbstractEnemyFactory]) -> PassiveEnemy:
    health, cell_pos, fabric, damage, exp_gain = __load_base_enemy_info__(enemy_info)
    if fabric not in fabrics:
        raise ValueError(f"Unknown fabric {fabric}")
    return fabrics[fabric].create_passive_enemy(
        health=health, max_health=health, cell_pos=cell_pos, damage=damage, exp_gain=exp_gain)


def __load_coward_enemy__(enemy_info, fabrics: Dict[str, AbstractEnemyFactory]) -> CowardEnemy:
    health, cell_pos, fabric, damage, exp_gain = __load_base_enemy_info__(enemy_info)
    if fabric not in fabrics:
        raise ValueError(f"Unknown fabric {fabric}")
    scare_radius = enemy_info['scare_radius']
    return fabrics[fabric].create_coward_enemy(
        health=health, max_health=health, cell_pos=cell_pos,
        scare_radius=scare_radius, damage=damage, exp_gain=exp_gain)


def __load_aggressive_enemy__(enemy_info, fabrics: Dict[str, AbstractEnemyFactory]) -> AggressiveEnemy:
    health, cell_pos, fabric, damage, exp_gain = __load_base_enemy_info__(enemy_info)
    attack_radius = enemy_info['attack_radius']
    if fabric not in fabrics:
        raise ValueError(f"Unknown fabric {fabric}")
    return fabrics[fabric].create_aggressive_enemy(
        health=health, max_health=health, cell_pos=cell_pos, attack_radius=attack_radius, damage=damage, exp_gain=exp_gain)


def __load_chest__(chest_info, image_map, images):
    image_key = chest_info['image_key']
    image_name = image_map[image_key]
    if image_name not in images:
        raise ValueError(f'Image {image_name} is unknown')
    return Chest(image_name=image_name, cell_pos=chest_info['position'])


class DefaultLeverLoader:
    """
        Класс DefaultLeverLoader ответственен за загрузку уровеней.
        Извлекает необходмую информацию из json файлов согласно внутреннему инварианту.
    """

    def __init__(self, *, path_to_levels: str, path_to_textures: str):
        self.path_to_levels = path_to_levels
        self.path_to_textures = path_to_textures

    CELL_TYPES_DICT = {
        '0': CellType.Empty,
        '1': CellType.Wall,
        '2': CellType.Chest
    }
    STRATEGY_TO_ENEMY = {
        'passive': __load_passive_enemy__,
        'coward': __load_coward_enemy__,
        'aggressive': __load_aggressive_enemy__
    }
    FABRIC_TO_CLASS = {
        'fantasy': FantasyEnemyFactory
    }

    def __load_cells__(self, info, images) -> Dict[Tuple[int, int], Cell]:
        num_cells_width = info['cells_amount'][0]
        num_cells_height = info['cells_amount'][1]
        cell_types = info['map']['cell_types']
        cell_images = info['map']['cell_images']
        cells = {}
        for i in range(num_cells_height):
            for j in range(num_cells_width):
                curr = i * num_cells_width + j
                if curr >= len(cell_types) or curr >= len(cell_images):
                    raise ValueError(
                        f'{curr} index out of range. Check cells_amount and cells_images/cell_types are consistent.'
                    )
                image_key = cell_images[curr]
                image_name = info['images'][image_key]
                if image_name not in images:
                    raise ValueError(f'Image {image_name} is unknown')
                type_id = cell_types[curr]
                if type_id not in self.CELL_TYPES_DICT:
                    raise ValueError(f'Type id {type_id} is unknown')
                cell_type = self.CELL_TYPES_DICT[type_id]
                cells[(j, i)] = Cell(cell_type=cell_type, image_name=image_name)
        return cells

    def __load_hero__(self, info, images) -> Hero:
        num_cells_width = info['cells_amount'][0]
        num_cells_height = info['cells_amount'][1]
        hero_info = info['hero']
        hero_cell_x, hero_cell_y = hero_info['position'][0], hero_info['position'][1]
        if hero_cell_x >= num_cells_width or hero_cell_y >= num_cells_height:
            raise ValueError(f'Wrong starting hero position: {hero_cell_x}x{hero_cell_y} out of range')
        image_key = hero_info['image_key']
        image_name = info['images'][image_key]
        if image_name not in images:
            raise ValueError(f'Image {image_name} is unknown')
        health = hero_info['health']
        exp = hero_info['exp']
        damage = hero_info['damage']
        return Hero(health=health, max_health=health, exp=exp, level=0,
                    cell_pos=(hero_cell_x, hero_cell_y), image_name=image_name, damage=damage)

    def __load_enemies__(self, info, fabrics):
        enemies_info = info['enemies']
        enemies = []
        for enemy_info in enemies_info:
            strategy = enemy_info['strategy']
            enemy: Enemy = self.STRATEGY_TO_ENEMY[strategy](enemy_info, fabrics)
            enemies.append(enemy)
        return enemies

    def __load_chests__(self, info, images):
        chests_info = info['chests']
        chests = []
        for chest_info in chests_info:
            chest: Chest = __load_chest__(chest_info, info['images'], images)
            chests.append(chest)
        return chests

    def __load_images__(self, info, fabrics) -> Dict[str, str]:
        images_info = info['images']
        images = {}
        for image_key in images_info:
            image_name = images_info[image_key]
            path_to_image = os.path.join(self.path_to_textures, images_info[image_key])
            images[image_name] = path_to_image

        for fabric_name in fabrics:
            fabric = fabrics[fabric_name]
            for image_name in fabric.get_required_images():
                if image_name not in images:
                    images[image_name] = os.path.join(self.path_to_textures, image_name)
        return images

    def __load_fabrics(self, info):
        fabrics = {}
        for enemy in info['enemies']:
            fabrics[enemy['fabric']] = enemy['fabric']
        for fabric in fabrics:
            fabrics[fabric] = self.FABRIC_TO_CLASS[fabric]()
        return fabrics

    # todo every image key to image_name
    def load(self, file_name: str) -> GameModel:
        """
        Конструирует и возвращает модель уровня, а также все загруженные картинки.
        :param file_name: имя файла уровня
        :return: модель уровня, содержащую все считаные из файла обьекты
        """
        level_file = os.path.join(self.path_to_levels, file_name)
        with open(level_file, 'r') as level:
            info = json.load(level)
            fabrics = self.__load_fabrics(info)
            images = self.__load_images__(info, fabrics)
            cells_dict = self.__load_cells__(info, images)
            chests = self.__load_chests__(info, images)
            enemies = self.__load_enemies__(info, fabrics)
            hero = self.__load_hero__(info, images)
        return GameModel(hero=hero, enemies=enemies, chests=chests, inventory=Inventory(),
                         cells_dict=cells_dict, image_dict=images)
