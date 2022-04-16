from typing import Tuple

import pygame

from src.entities.cell import CellType
from src.model.game_model import GameModel
from src.state import State
from src.views.game_view import GameView


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

    def __init__(self, windows_size: Tuple[int, int], game_model: GameModel):
        self.game_view = GameView(windows_size, (48, 48))
        self.game_model = game_model

    def __move_hero__(self, key_event: int, game_model: GameModel) -> None:
        hero = game_model.hero
        cells = game_model.cells
        next_pos = (hero.cell_pos[0] + self.movement[key_event][0],
                    hero.cell_pos[1] + self.movement[key_event][1])
        if next_pos not in cells or cells[next_pos].cell_type == CellType.Wall:
            return
        hero.cell_pos = next_pos

    def run(self, event: pygame.event.Event) -> State:
        """
        Обрабатывает нажатия с клавиатуры и отображает изменения на экране
        :param event: событие нажатия клавиатуры
        :return: состояние игры
        """
        if event.type == pygame.QUIT:
            return State.EXIT
        elif event.type == pygame.KEYDOWN:
            if event.key in self.movement:
                self.__move_hero__(event.key, self.game_model)
        self.game_view.view_load(self.game_model)
        return State.GAME
