from typing import List, Tuple, Optional

import pygame

from src.entities.armor import Armor
from src.entities.cell import CellType
from src.entities.hero import Hero
from src.entities.enemy import Enemy
from src.entities.inventory import Inventory
from src.entities.weapon import Weapon
from src.model.game_model import GameModel
from src.views.game_view import GameView

from src import state
from src.state import State

import numpy as np


def __fight__(hero: Hero, enemy: Enemy):
    hero.health -= enemy.damage
    enemy.health -= hero.damage
    pass


class GameHandler:
    """
    Класс ответственный за обработку game event'ов
    """
    movement = {
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1)
    }

    def __init__(self, game_model: GameModel, game_view: GameView):
        self.game_view = game_view
        self.game_model = game_model


    def __get_next_hero_pos__(self, key_event: int, hero: Hero) -> Tuple[int, int]:
        next_pos = (hero.cell_pos[0] + self.movement[key_event][0],
                    hero.cell_pos[1] + self.movement[key_event][1])
        return next_pos

    def __get_enemy_by_pos__(self, enemies: List[Enemy], cell_pos: Tuple[int, int]) -> Optional[Enemy]:
        res_enemy = None
        for enemy in enemies:
            if enemy.cell_pos[0] == cell_pos[0] and enemy.cell_pos[1] == cell_pos[1]:
                if res_enemy is not None:
                    raise ValueError(f'Two enemies is on the same cell - {enemy.cell_pos}')
                res_enemy = enemy
        return res_enemy


    def print_game(self):
        self.game_view.view_load(self.game_model)

    def run(self, event: pygame.event.Event):
        """
        Обрабатывает нажатия с клавиатуры и отображает изменения на экране
        :param event: событие нажатия клавиатуры
        :return: состояние игры
        """
        if event.type == pygame.QUIT:
            return State.EXIT
        elif event.type == pygame.KEYDOWN:
            if event.key in self.movement:
                hero = self.game_model.hero
                cells = self.game_model.cells_dict
                enemies = self.game_model.enemies
                next_pos = self.__get_next_hero_pos__(event.key, hero)
                # todo block hp and exp bars
                if next_pos not in cells or cells[next_pos].cell_type == CellType.Wall:
                    return State.GAME
                enemy = self.__get_enemy_by_pos__(enemies, next_pos)
                if cells[next_pos].cell_type == CellType.Empty:
                    if enemy is None:
                        hero.cell_pos = next_pos
                    else:
                        __fight__(hero, enemy)
                for enemy in enemies:
                    if enemy.health > 0:
                        enemy.move(hero, enemies, cells)
                # if hero is dead
                if hero.health <= 0:
                    # todo YOU ARE DEAD screen with button to return to menu
                    state.state_machine = State.EXIT
                # remove dead enemies
                dead_enemies = list(filter(lambda e: e.health <= 0, enemies))
                # reward
                for dead_enemy in dead_enemies:
                    hero.add_exp(dead_enemy.exp_gain)
                self.game_model.enemies = list(filter(lambda e: e not in dead_enemies, enemies))
        self.print_game()
        return State.GAME

    def generate_item(self):
        n, p = 1, 0.5
        res = np.random.binomial(n, p)
        if res == 0:
            return self.generate_weapon()
        return self.generate_armor()

    def generate_weapon(self):
        return Weapon(image="weapon1.jpg",
                      strength=np.random.randint(low=1, high=self.game_model.hero.level + 2, size=1), name="")

    def generate_armor(self):
        return Armor(image="armor1.jpg", defence=np.random.randint(low=1, high=self.game_model.hero.level + 2, size=1),
                     name="")
