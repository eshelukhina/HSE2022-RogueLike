from typing import Optional

import pygame

from src.commands.inventory_command import InventoryCommand
from src.commands.movement_command import MovementCommand
from src.commands.return_command import ReturnCommand
from src.config import Config
from src.model.game_model import GameModel
from src.state import State
from src.views.inventory_view import InventoryView
from src.views.system_view import SystemView


class KeydownCommand:
    """Класс, ответственный за логику управления в игре и меню"""

    def __init__(self, game_model: Optional[GameModel] = None, system_view: SystemView = None,
                 inventory_view: InventoryView = None):
        self.game_model = game_model
        self.system_view = system_view
        self.inventory_view = inventory_view
        self.commands = {
            pygame.K_i: InventoryCommand(game_model=self.game_model, inventory_view=self.inventory_view),
            pygame.K_LEFT: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_LEFT],
                                           system_view=self.system_view, inventory_view=self.inventory_view),
            pygame.K_RIGHT: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_RIGHT],
                                            system_view=self.system_view, inventory_view=self.inventory_view),
            pygame.K_UP: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_UP],
                                         system_view=self.system_view, inventory_view=self.inventory_view),
            pygame.K_DOWN: MovementCommand(game_model=self.game_model, movement=Config.movement[pygame.K_DOWN],
                                           system_view=self.system_view, inventory_view=self.inventory_view),
            pygame.K_RETURN: ReturnCommand(game_model=self.game_model, system_view=self.system_view,
                                           inventory_view=self.inventory_view)
        }

    def execute(self, key: int) -> State:
        """
        Логика обработки нажатия кнопок
        :param key: pygame.key: Int, кнопка которую нажал игрок
        :return State
        """
        if key in self.commands:
            return self.commands[key].execute(key=key)
        else:
            if self.inventory_view is not None:
                return State.INVENTORY
            elif self.system_view is not None:
                return State.MENU
            return State.GAME
