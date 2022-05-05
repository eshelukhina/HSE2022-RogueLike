from typing import Optional

import pygame

from src.commands.exit_command import ExitCommand
from src.commands.keydown_command import KeydownCommand
from src.model.game_model import GameModel
from src.state import State
from src.views.game_view import GameView


class GameHandler:
    """
    Класс ответственный за обработку game event'ов
    """

    def __init__(self, game_view: GameView, game_model: Optional[GameModel]):
        self.game_view = game_view
        self.game_model = game_model
        self.commands = {
            pygame.QUIT: ExitCommand(game_model=self.game_model),
            pygame.KEYDOWN: KeydownCommand(game_model=self.game_model)
        }

    def set_game_model(self, game_model: GameModel):
        self.game_model = game_model
        self.commands = {
            pygame.QUIT: ExitCommand(self.game_model),
            pygame.KEYDOWN: KeydownCommand(self.game_model)
        }

    def print_game(self):
        self.game_view.view_load(self.game_model)

    def run(self, event: pygame.event.Event):
        """
        Обрабатывает нажатия с клавиатуры и отображает изменения на экране
        :param event: событие нажатия клавиатуры
        :return: состояние игры
        """
        self.print_game()
        if event.type in self.commands:
            return self.commands[event.type].execute(event.key)
        else:
            return State.GAME


