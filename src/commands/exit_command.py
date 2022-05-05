from typing import Optional

from src.model.game_model import GameModel
from src.state import State
from src.views.system_view import SystemView


class ExitCommand:

    def __init__(self, game_model: Optional[GameModel] = None, system_view: SystemView = None):
        self.game_model = game_model
        self.system_view = system_view

    def execute(self, key: int):
        return State.EXIT
