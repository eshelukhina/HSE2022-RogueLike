import pygame

from src.entities.cell import CellType
from src.entities.hero import Hero
from src.model.game_model import GameModel
from src.state import State


class GameHandler:
    """
    Класс ответственный за обработку game event'ов
    """
    SPEED = 48

    def __check_collision__(self, hero, cells):
        for cell in cells:
            if cell.cell_type == CellType.Wall and hero.colliderect(cell.rect):
                return True

    def __move_hero__(self, key_event, hero: Hero, cells):
        shift_x = 0
        shift_y = 0
        if key_event == pygame.K_LEFT:
            shift_x = -self.SPEED
            if self.__check_collision__(hero.rect.move(shift_x, shift_y), cells):
                shift_x = 0
        elif key_event == pygame.K_RIGHT:
            shift_x = self.SPEED
            if self.__check_collision__(hero.rect.move(shift_x, shift_y), cells):
                shift_x = 0
        elif key_event == pygame.K_UP:
            shift_y = -self.SPEED
            if self.__check_collision__(hero.rect.move(shift_x, shift_y), cells):
                shift_y = 0
        elif key_event == pygame.K_DOWN:
            shift_y = self.SPEED
            if self.__check_collision__(hero.rect.move(shift_x, shift_y), cells):
                shift_y = 0
        hero.move(shift_x, shift_y)

    def run(self, events, game_model: GameModel) -> State:
        """
        Обрабатывает нажатия с клавиатуры
        :param game_model: обьекты карты
        :return: состояние игры
        """
        for event in events:
            if event.type == pygame.QUIT:
                return State.exit
            elif event.type == pygame.KEYDOWN:
                self.__move_hero__(event.key, game_model.get_hero(), game_model.get_cells())
        return State.game
