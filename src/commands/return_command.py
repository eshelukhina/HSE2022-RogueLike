from typing import Optional

from src.model.game_model import GameModel
from src.state import State
from src.views.system_view import SystemView


class ReturnCommand:
    def __init__(self, game_model: Optional[GameModel] = None, system_view: SystemView = None):
        self.game_model = game_model
        self.system_view = system_view

    def execute(self, key: int):
        if self.system_view is not None:
            if self.system_view.current_window == "Menu":
                if self.system_view.current_item == "Exit":
                    self.system_view.press_exit()
                    self.system_view.close_menu()
                    return State.EXIT
                if self.system_view.current_item == "Start":
                    self.system_view.close_menu()
                    return State.GAME
        else:
            return State.GAME
