from typing import Optional

from src.model.game_model import GameModel
from src.state import State


class InventoryCommand:

    def __init__(self, game_model: Optional[GameModel]):
        self.game_model = game_model

    def execute(self):
        return State.INVENTORY
