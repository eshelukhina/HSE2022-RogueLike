import random

import numpy as np

from src.entities.hero import Hero
from src.entities.inventory import Inventory
from src.loader.default_level_loader import DefaultLeverLoader
from src.model.game_model import GameModel


class MapBuilder:
    def __init__(self, load, load_path='', height=30, width=22, max_tunnels=80, max_length=12):
        self.load = load
        self.load_path = load_path
        self.height, self.width, self.max_tunnels, self.max_length = height, width, max_tunnels, max_length
        self.level_loader = DefaultLeverLoader(path_to_levels='levels', path_to_textures='textures')
        self.hero_health, self.hero_damage, self.hero_exp, self.hero_image_name = 100, 12, 0, "hero.png"
        self.amount_of_enemies = 5
        self.enemy_damage, self.enemy_health, self.enemy_exp_gain = 15, 100, 200
        self.max_chests_amount = 4

    def add_size(self, height, width):
        self.load = False
        self.height, self.width = height, width
        return self

    def add_max_tunnels(self, max_tunnels):
        self.load = False
        self.max_tunnels = max_tunnels
        return self

    def add_max_length(self, max_length):
        self.load = False
        self.max_length = max_length
        return self

    def add_load_path(self, load_path):
        self.load = False
        self.load = True
        self.load_path = load_path
        return self

    def generate_cells(self):
        cells = np.ones((self.height, self.width))
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        cur_row = np.random.randint(low=0, high=self.height, size=1)[0]
        cur_column = np.random.randint(low=0, high=self.width, size=1)[0]
        last_direction = None

        for _ in range(self.max_tunnels):
            while True:
                cur_direction = random.choice(directions)
                if last_direction is None or (
                        (cur_direction[0] != -last_direction[0] or cur_direction[1] != -last_direction[1]) and (
                        cur_direction != last_direction)):
                    break

            random_length = np.random.randint(low=2, high=self.max_length, size=1)[0]
            if cur_direction[0] == 1:
                cells[cur_row:min(self.height, cur_row + random_length), cur_column] = 0
                cur_row = min(self.height - 1, cur_row + random_length)
            elif cur_direction[0] == -1:
                cells[max(0, cur_row - random_length):cur_row+1, cur_column] = 0
                cur_row = max(0, cur_row - random_length)
            if cur_direction[1] == 1:
                cells[cur_row, cur_column:min(self.width, cur_column + random_length)] = 0
                cur_column = min(self.width - 1, cur_column + random_length)
            elif cur_direction[1] == -1:
                cells[cur_row, max(0, cur_column - random_length):cur_column+1] = 0
                cur_column = max(0, cur_column - random_length)
            last_direction = cur_direction
        cell_images = self.create_cell_images(cells)
        map_dict = {"cells_amount": [self.height, self.width], "map": {"cell_types": cells, "cell_images": cell_images}}
        return map_dict

    def generate_hero(self, cells):
        hero_cell_x, hero_cell_y = np.argwhere(cells == 0)[0]
        return Hero(health=self.hero_health, max_health=self.hero_health, exp=self.hero_exp, level=0,
                    cell_pos=(hero_cell_x, hero_cell_y), image_name=self.hero_image_name, damage=self.hero_damage)

    def create_cell_images(self, cells):
        cell_images = cells.copy()
        for i in range(self.height):
            for j in range(self.width):
                if cell_images[i][j] == 0:
                    continue
                if (i + 1 < self.height and cell_images[i + 1][j] == 0) or (
                        j + 1 < self.width and cell_images[i][j + 1] == 0):
                    continue
                if (i > 0 and cell_images[i - 1][j] == 0) or (j > 0 and cell_images[i][j - 1] == 0):
                    continue
                cell_images[i][j] = 5
        return cell_images

    def generate_enemy(self):
        enemy = {}
        enemy["strategy"] = random.choice(list(self.level_loader.STRATEGY_TO_ENEMY.keys()))
        enemy["fabric"] = random.choice(list(self.level_loader.FABRIC_TO_CLASS.keys()))
        enemy["damage"] = self.enemy_damage
        enemy["health"] = np.random.randint(low=10, high=self.enemy_health, size=1)[0]
        enemy["exp_gain"] = np.random.randint(low=enemy["health"], high=self.enemy_health, size=1)[0]
        enemy["attack_radius"] = 3
        enemy["scare_radius"] = 5
        enemy["chance_of_cloning"] = 0.1
        return enemy

    def generate_enemies(self, cells):
        empty_cells = np.argwhere(cells == 0)[self.amount_of_enemies:]
        enemies = []
        for _ in range(self.amount_of_enemies):
            enemy_pos = random.choice(empty_cells)
            enemy = self.generate_enemy()
            enemy["position"] = enemy_pos
            enemies.append(enemy)
        return enemies

    def generate_images(self):
        return {
            "0": "empty_block.png",
            "1": "wall1.png",
            "2": "hero.png",
            "4": "chest.png",
            "5": "wall2.png"
        }

    def generate_chests(self, cells):
        empty_cells = np.argwhere(cells == 0)[self.amount_of_enemies:]
        chests = []
        for _ in range(self.max_chests_amount):
            chest_pos = random.choice(empty_cells)
            chests.append({"position": chest_pos, "image_key": "4"})
        return chests

    def build(self):
        if self.load:
            return self.level_loader.load(self.load_path)
        map_info = self.generate_cells()
        cell_types = map_info["map"]["cell_types"]
        enemies_info = self.generate_enemies(cell_types)
        images_info = self.generate_images()
        chests_info = self.generate_chests(cell_types)
        hero = self.generate_hero(cell_types)

        map_info["map"]["cell_types"] = np.array([str(int(i)) for i in np.ravel(map_info["map"]["cell_types"])])
        map_info["map"]["cell_images"] = np.array([str(int(i)) for i in np.ravel(map_info["map"]["cell_images"])])
        info = {"images": images_info, "cells_amount": map_info["cells_amount"], "map": map_info["map"],
                "enemies": enemies_info, "chests": chests_info}

        fabrics = self.level_loader.__load_fabrics__(info)
        images = self.level_loader.__load_images__(info, fabrics)
        cells_dict = self.level_loader.__load_cells__(info, images)
        enemies = self.level_loader.__load_enemies__(info, fabrics)
        chests = self.level_loader.__load_chests__(info, images)
        return GameModel(hero=hero, enemies=enemies, chests=chests, inventory=Inventory(),
                         cells_dict=cells_dict, image_dict=images)
