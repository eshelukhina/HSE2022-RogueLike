from typing import Optional

import pygame

from src.commands.inventory_command import InventoryCommand
from src.commands.movement_command import MovementCommand
from src.commands.return_command import ReturnCommand
from src.config import Config
from src.model.game_model import GameModel
from src.state import State
from src.views.system_view import SystemView


class KeydownCommand:

    def __init__(self, game_model: Optional[GameModel] = None, system_view: SystemView = None):
        self.game_model = game_model
        self.system_view = system_view
        self.commands = {
            pygame.K_i: InventoryCommand(game_model=self.game_model),
            pygame.K_LEFT: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_LEFT], system_view=self.system_view),
            pygame.K_RIGHT: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_RIGHT], system_view=self.system_view),
            pygame.K_UP: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_UP], system_view=self.system_view),
            pygame.K_DOWN: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_DOWN], system_view=self.system_view),
            pygame.K_RETURN: ReturnCommand(game_model=self.game_model, system_view=self.system_view)
        }

    def execute(self, key: int):
        if key in self.commands:
            return self.commands[key].execute(key=key)
        else:
            return State.GAME
