from src.entities.enemy.enemy_state import EnemyState
from src.entities.enemy.coward_state import CowardState
from src.entities.enemy.confused_state import ConfusedState

from typing import Tuple


class Enemy:
    """Интерфейс для противников"""

    def __init__(self, health: int, max_health: int, cell_pos: Tuple[int, int],
                 image_name: str, damage: int, exp_gain: int, state: EnemyState):
        self.initial_state = state
        self.cur_state = state
        self.health = health
        self.max_health = max_health
        self.cell_pos = cell_pos
        self.image_name = image_name
        self.damage = damage
        self.exp_gain = exp_gain

    def move(self, hero, enemies, cells) -> None:
        """
        Метод, отвечает за обновление состояния и выполнения следующего шага согласно стратегии

        :param hero: герой
        :param enemies: список мобов
        :param cells: клетки карты
        :return: None
        """
        if type(self.initial_state) is CowardState:
            pass
        elif type(self.cur_state) is ConfusedState and self.cur_state.time == 0:
            self.cur_state = self.initial_state
        elif self.health <= self.max_health * 0.2 and type(self.cur_state) is not CowardState:
            self.cur_state = CowardState(scare_radius=3)
        elif self.health > self.max_health * 0.2 and type(self.cur_state) is CowardState:
            self.cur_state = self.initial_state
        self.cur_state.move(self, hero, enemies, cells)
