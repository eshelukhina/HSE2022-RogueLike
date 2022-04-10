from entities.entity import Entity

import pygame
import enum


class CellType(enum.Enum):
    Empty = 0
    Wall = 1
    Chest = 2
    CairnOfPassage = 3


class Cell(Entity):
    """
    Элемент карты
    """
    def __init__(self, *, x: int, y: int, cell_type: CellType, image: pygame.image):
        self.cell_type = cell_type
        super().__init__(x, y, image)
