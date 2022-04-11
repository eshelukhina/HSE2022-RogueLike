import pygame.event

from src.handlers.game_handler import GameHandler
from src.model.game_model import GameModel
from src.state import State


def test_simple():
    game_model = GameModel(None, None, None)
    game_handler = GameHandler()
    pygame.event.Event(256)
    assert game_handler.run([pygame.event.Event(256)], game_model) == State.exit
