import os
import pytest

from src.entities.cell import CellType
from src.loader.default_level_loader import DefaultLeverLoader


def test_simple():
    path_to_textures = 'path_to_textures'
    loader = DefaultLeverLoader(
        path_to_levels='src/loader/test/resources', path_to_textures=path_to_textures)
    game_model = loader.load('simple_map.json')

    image_dict = game_model.image_dict
    assert image_dict
    assert game_model.image_dict == {
        '0': os.path.join(path_to_textures, 'empty_block.png'),
        '1': os.path.join(path_to_textures, 'wall.png'),
        '2': os.path.join(path_to_textures, 'hero.png')
    }

    cells_dict = game_model.cells_dict
    assert cells_dict
    assert len(cells_dict) == 2 * 2
    for cnt, cell in enumerate(game_model.cells_dict.values()):
        if cnt < 2:
            assert cell.image_name == '0'
            assert cell.cell_type == CellType.Empty
        else:
            assert cell.image_name == '1'
            assert cell.cell_type == CellType.Wall
    hero = game_model.hero
    assert hero
    assert hero.image_name == '2'
    assert hero.cell_pos == (0, 0)


def test_cells_mismatch():
    loader = DefaultLeverLoader(path_to_levels='src/loader/test/resources', path_to_textures='')
    with pytest.raises(ValueError):
        loader.load('cells_mismatch.json')


def test_hero_position():
    loader = DefaultLeverLoader(path_to_levels='src/loader/test/resources', path_to_textures='')
    with pytest.raises(ValueError) as exception:
        loader.load('wrong_hero_position.json')
    assert str(exception.value) == 'Wrong starting hero position: 2x2 out of range'


def test_unknown_image():
    loader = DefaultLeverLoader(path_to_levels='src/loader/test/resources', path_to_textures='')
    with pytest.raises(ValueError) as exception:
        loader.load('unknown_image.json')
    assert str(exception.value) == 'Image with key 239 is unknown'


def test_unknown_cell_type():
    loader = DefaultLeverLoader(path_to_levels='src/loader/test/resources', path_to_textures='')
    with pytest.raises(ValueError) as exception:
        loader.load('unknown_cell_type.json')
    assert str(exception.value) == 'Type id 239 is unknown'
