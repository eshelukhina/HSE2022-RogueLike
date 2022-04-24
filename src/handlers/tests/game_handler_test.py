import pygame
import copy

from src.entities.cell import Cell, CellType
from src.entities.hero import Hero
from src.model.game_model import GameModel
from src.handlers.game_handler import GameHandler
from src.state import State


g_model = GameModel(
    cells_dict={
        (2, 0): Cell(image_key=0, cell_type=CellType.Wall),
        (2, 1): Cell(image_key=0, cell_type=CellType.Wall),
        (2, 2): Cell(image_key=0, cell_type=CellType.Wall),

        (1, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (1, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (1, 2): Cell(image_key=0, cell_type=CellType.Empty),

        (0, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (0, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (0, 2): Cell(image_key=0, cell_type=CellType.Empty),
    },
    hero=Hero(cell_pos=(0, 0), image_key=1),
    enemies=[],
    image_dict={0: 'block', 1: 'hero'}
)


class MockView:
    def view_load(self, game_model: GameModel):
        pass


def test_quit():
    game_handler = GameHandler(game_model=copy.deepcopy(g_model), game_view=MockView())
    next_state = game_handler.run(event=pygame.event.Event(pygame.QUIT))
    assert next_state == State.EXIT


def test_move():
    game_handler = GameHandler(game_model=copy.deepcopy(g_model), game_view=MockView())
    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
    updated_g_mod = game_handler.game_model
    assert next_state == State.GAME
    assert updated_g_mod.hero.cell_pos == (1, 0)


def test_move_out_of_map():
    game_handler = GameHandler(game_model=copy.deepcopy(g_model), game_view=MockView())
    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
    updated_g_mod = game_handler.game_model
    assert next_state == State.GAME
    assert updated_g_mod.hero.cell_pos == (0, 0)


def test_move_in_wall():
    game_model = copy.deepcopy(g_model)
    game_model.hero.cell_pos = (1, 0)
    game_handler = GameHandler(game_model=game_model, game_view=MockView())
    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
    updated_g_mod = game_handler.game_model
    assert next_state == State.GAME
    assert updated_g_mod.hero.cell_pos == (1, 0)
