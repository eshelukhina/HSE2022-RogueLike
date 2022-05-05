from typing import Optional, Tuple, List

import numpy as np

from src.entities.armor import Armor
from src.entities.cell import CellType
from src.entities.confused_enemy import ConfusedEnemy
from src.entities.enemy import Enemy
from src.entities.hero import Hero
from src.entities.weapon import Weapon
from src.model.game_model import GameModel
from src.state import State


class MovementCommand:

    def __init__(self, game_model: Optional[GameModel], movement: Tuple[int, int]):
        self.game_model = game_model
        self.movement = movement

    def __get_next_hero_pos__(self, hero: Hero) -> Tuple[int, int]:
        next_pos = (hero.cell_pos[0] + self.movement[0],
                    hero.cell_pos[1] + self.movement[1])
        return next_pos

    def __get_entity_by_pos__(self, entities, cell_pos: Tuple[int, int]):
        res_entity = None
        for entity in entities:
            if entity.cell_pos[0] == cell_pos[0] and entity.cell_pos[1] == cell_pos[1]:
                if res_entity is not None:
                    raise ValueError(f'Two enemies is on the same cell - {entity.cell_pos}')
                res_entity = entity
        return res_entity

    def __fight__(self, hero: Hero, enemy: Enemy):
        hero.health -= enemy.damage - hero.damage_taken_modifier
        enemy.health -= hero.damage

    def __set_confused_enemy__(self, enemies: List[Enemy], enemy: Enemy, confused_enemy):
        for i in range(len(enemies)):
            if enemies[i] is enemy:
                enemies[i] = confused_enemy
                return

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


    def execute(self):
        hero = self.game_model.hero
        cells = self.game_model.cells_dict
        enemies = self.game_model.enemies
        chests = self.game_model.chests
        next_pos = self.__get_next_hero_pos__(hero)

        if next_pos not in cells or cells[next_pos].cell_type == CellType.Wall:
            return State.GAME

        if cells[next_pos].cell_type == CellType.Empty:
            enemy = self.__get_entity_by_pos__(enemies, next_pos)
            chest = self.__get_entity_by_pos__(chests, next_pos)
            if enemy:
                self.__fight__(hero, enemy)
                # TODO confused mobs set a rule
                if hero.damage > 10:
                    self.__set_confused_enemy__(enemies, enemy, ConfusedEnemy(enemy))
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
        enemies = self.game_model.enemies
        for i in range(len(enemies)):
            enemy = enemies[i]
            if isinstance(enemy, ConfusedEnemy) and enemy.time == 0:
                enemies[i] = enemy.get_enemy()
        return State.GAME
