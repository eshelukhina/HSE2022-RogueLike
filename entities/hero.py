import pygame
from entities.entity import Entity


class Hero(Entity):
    def __init__(self, *, x: int, y: int, image):
        super().__init__(x, y, image)

    def move(self, shift_x, shift_y):
        self.rect.x += shift_x
        self.rect.y += shift_y

