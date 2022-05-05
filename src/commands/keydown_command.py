from typing import Optional

import pygame

from src.commands.inventory_command import InventoryCommand
from src.commands.movement_command import MovementCommand
from src.config import Config
from src.model.game_model import GameModel
from src.state import State


class KeydownCommand:

    def __init__(self, game_model: Optional[GameModel]):
        self.game_model = game_model
        self.commands = {
            pygame.K_i: InventoryCommand(self.game_model),
            pygame.K_LEFT: MovementCommand(self.game_model, Config.movement[pygame.K_LEFT]),
            pygame.K_RIGHT: MovementCommand(self.game_model, Config.movement[pygame.K_RIGHT]),
            pygame.K_UP: MovementCommand(self.game_model, Config.movement[pygame.K_UP]),
            pygame.K_DOWN: MovementCommand(self.game_model, Config.movement[pygame.K_DOWN])
        }

    def execute(self, key: int):
        if key in self.commands:
            return self.commands[key].execute()
        else:
            return State.GAME
