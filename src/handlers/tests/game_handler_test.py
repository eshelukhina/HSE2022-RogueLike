import pygame
import copy

from src.entities.cell import Cell, CellType
from src.entities.hero import Hero
from src.entities.passive_enemy import PassiveEnemy
from src.entities.aggressive_enemy import AggressiveEnemy
from src.entities.coward_enemy import CowardEnemy
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
    hero=Hero(health=100, max_health=100, exp=0, level=0,
              cell_pos=(0, 0), damage=10, image_key=1),
    enemies=[],
    image_dict={0: 'block', 1: 'hero'},
    inventory=None,
    chests=[]
)

no_walls_g_model = GameModel(
    cells_dict={
        (0, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (0, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (0, 2): Cell(image_key=0, cell_type=CellType.Empty),
        (0, 3): Cell(image_key=0, cell_type=CellType.Empty),
        (0, 4): Cell(image_key=0, cell_type=CellType.Empty),

        (1, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (1, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (1, 2): Cell(image_key=0, cell_type=CellType.Empty),
        (1, 3): Cell(image_key=0, cell_type=CellType.Empty),
        (1, 4): Cell(image_key=0, cell_type=CellType.Empty),

        (2, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (2, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (2, 2): Cell(image_key=0, cell_type=CellType.Empty),
        (2, 3): Cell(image_key=0, cell_type=CellType.Empty),
        (2, 4): Cell(image_key=0, cell_type=CellType.Empty),

        (3, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 2): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 3): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 4): Cell(image_key=0, cell_type=CellType.Empty),

        (3, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 2): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 3): Cell(image_key=0, cell_type=CellType.Empty),
        (3, 4): Cell(image_key=0, cell_type=CellType.Empty),

        (4, 0): Cell(image_key=0, cell_type=CellType.Empty),
        (4, 1): Cell(image_key=0, cell_type=CellType.Empty),
        (4, 2): Cell(image_key=0, cell_type=CellType.Empty),
        (4, 3): Cell(image_key=0, cell_type=CellType.Empty),
        (4, 4): Cell(image_key=0, cell_type=CellType.Empty),
    },
    hero=Hero(health=100, max_health=100, exp=0, level=0,
              cell_pos=(0, 0), damage=10, image_key=1),
    enemies=[],
    image_dict={0: 'block', 1: 'hero'},
    inventory=None,
    chests=[]
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


def test_passive_enemy():
    game_model = copy.deepcopy(no_walls_g_model)
    hero = game_model.hero
    enemy = PassiveEnemy(health=20, max_health=20, cell_pos=(0, 2), image_key=1, damage=10, exp_gain=30)
    game_model.enemies = [enemy]
    game_handler = GameHandler(game_model=game_model, game_view=MockView())

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    assert next_state == State.GAME

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    assert next_state == State.GAME
    assert hero.cell_pos == (0, 1)
    assert hero.health == 90
    assert hero.exp == 0
    assert len(game_model.enemies) == 1
    assert enemy.cell_pos == (0, 2)
    assert enemy.health == 10

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    assert next_state == State.GAME
    assert hero.cell_pos == (0, 1)
    assert hero.health == 80
    assert hero.exp == 30
    assert len(game_model.enemies) == 0


def test_aggressive_enemy():
    game_model = copy.deepcopy(no_walls_g_model)
    hero = game_model.hero
    enemy = AggressiveEnemy(
        health=20, max_health=20, cell_pos=(0, 2),
        image_key=1, damage=10, exp_gain=30, attack_radius=2)
    game_model.enemies = [enemy]
    game_handler = GameHandler(game_model=game_model, game_view=MockView())

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    assert next_state == State.GAME
    assert hero.cell_pos == (0, 1)
    assert hero.health == 90
    assert hero.exp == 0
    assert len(game_model.enemies) == 1
    assert enemy.cell_pos == (0, 2)
    assert enemy.health == 10

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
    assert next_state == State.GAME
    assert hero.cell_pos == (1, 1)
    assert hero.health == 90
    assert hero.exp == 0
    assert len(game_model.enemies) == 1
    assert enemy.cell_pos == (1, 2)
    assert enemy.health == 10

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN))
    assert next_state == State.GAME
    assert hero.cell_pos == (1, 1)
    assert hero.health == 80
    assert hero.exp == 30
    assert len(game_model.enemies) == 0


def test_coward_enemy():
    game_model = copy.deepcopy(no_walls_g_model)
    hero = game_model.hero
    enemy = CowardEnemy(health=20, max_health=20, cell_pos=(3, 1), image_key=1, damage=10, exp_gain=30, scare_radius=3)
    game_model.enemies = [enemy]
    game_handler = GameHandler(game_model=game_model, game_view=MockView())

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
    assert next_state == State.GAME
    assert hero.cell_pos == (1, 0)
    assert enemy.cell_pos == (3, 1)
    assert enemy.health == 20

    next_state = game_handler.run(event=pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
    assert next_state == State.GAME
    assert hero.cell_pos == (2, 0)
    assert enemy.cell_pos == (4, 1)
    assert enemy.health == 20
