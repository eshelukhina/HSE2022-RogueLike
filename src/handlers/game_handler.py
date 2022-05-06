from typing import List, Tuple, Optional

import numpy as np
import pygame

from src.entities.armor import Armor
from src.entities.cell import CellType
from src.entities.enemy.confused_state import ConfusedState
from src.entities.enemy.enemy import Enemy
from src.entities.hero import Hero
from src.entities.weapon import Weapon
from src.model.game_model import GameModel
from src.state import State
from src.views.game_view import GameView


def __fight__(hero: Hero, enemy: Enemy):
    hero.health -= enemy.damage - hero.damage_taken_modifier
    enemy.health -= hero.damage


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

    def __init__(self, game_view: GameView, game_model: Optional[GameModel]):
        self.game_view = game_view
        self.game_model = game_model

    def __get_next_hero_pos__(self, key_event: int, hero: Hero) -> Tuple[int, int]:
        next_pos = (hero.cell_pos[0] + self.movement[key_event][0],
                    hero.cell_pos[1] + self.movement[key_event][1])
        return next_pos

    def __get_entity_by_pos__(self, entities, cell_pos: Tuple[int, int]):
        res_entity = None
        for entity in entities:
            if entity.cell_pos[0] == cell_pos[0] and entity.cell_pos[1] == cell_pos[1]:
                if res_entity is not None:
                    raise ValueError(f'Two enemies is on the same cell - {entity.cell_pos}')
                res_entity = entity
        return res_entity

    def __set_confused_enemy__(self, enemies: List[Enemy], enemy: Enemy):
        for i in range(len(enemies)):
            if enemies[i] is enemy:
                enemies[i].cur_state = ConfusedState()
                return

    def set_game_model(self, game_model: GameModel):
        self.game_model = game_model

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
            if event.key == pygame.K_i:
                return State.INVENTORY
            if event.key in self.movement:
                hero = self.game_model.hero
                cells = self.game_model.cells_dict
                enemies = self.game_model.enemies
                chests = self.game_model.chests
                next_pos = self.__get_next_hero_pos__(event.key, hero)
                # todo block hp and exp bars
                if next_pos not in cells or cells[next_pos].cell_type == CellType.Wall:
                    return State.GAME
                if cells[next_pos].cell_type == CellType.Empty:
                    enemy = self.__get_entity_by_pos__(enemies, next_pos)
                    chest = self.__get_entity_by_pos__(chests, next_pos)
                    if enemy:
                        __fight__(hero, enemy)
                        # TODO confused mobs set a rule
                        if hero.damage > 10:
                            self.__set_confused_enemy__(enemies, enemy)
                    elif chest:
                        # TODO store items in chest, not generate the in place
                        chest_item = self.generate_item()
                        self.game_model.inventory.add_item(chest_item)
                        chests.remove(chest)
                    else:
                        hero.cell_pos = next_pos
                for i in range(len(enemies)):
                    enemy = enemies[i]
                    if enemy.health > 0:
                        enemy.move(hero, enemies, cells)
                # if hero is dead
                if hero.health <= 0:
                    # todo YOU ARE DEAD screen with button to return to menu
                    return State.EXIT
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
                      strength=np.random.randint(low=1, high=self.game_model.hero.level + 2, size=1)[0], name="")

    def generate_armor(self):
        return Armor(image="armor1.jpg",
                     defence=np.random.randint(low=1, high=self.game_model.hero.level + 2, size=1)[0], name="")
