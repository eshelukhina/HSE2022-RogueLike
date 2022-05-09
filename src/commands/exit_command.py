from typing import Optional

from src.model.game_model import GameModel
from src.state import State
from src.views.inventory_view import InventoryView
from src.views.system_view import SystemView


class ExitCommand:
    """Класс, ответственный за команду выхода из игры"""

    def __init__(self, game_model: Optional[GameModel] = None, system_view: SystemView = None,
                 inventory_view: InventoryView = None):
        self.game_model = game_model
        self.system_view = system_view
        self.inventory_view = inventory_view

    def execute(self, key: int = None) -> State:
        """
        Логика обработки выхода из игры
        :param key: pygame.key: Int, кнопка которую нажал игрок
        :return State
        """
        if self.inventory_view is not None:
            self.inventory_view.close_inventory()
        return State.EXIT
