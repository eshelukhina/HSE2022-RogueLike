import pygame

from src.config import Config
from src.handlers.game_handler import GameHandler
from src.handlers.inventory_handler import InventoryHandler
from src.handlers.system_handler import SystemHandler
from src.loader.default_level_loader import DefaultLeverLoader
from src.state import State


class App:
    """
    Главный класс, ответственный за запуск игры
    """

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.cur_state = State.MENU

        self.level_loader = DefaultLeverLoader()
        self.game_model = self.level_loader.load('default')

        self.game_handler = GameHandler(Config.WINDOW_SIZE, self.game_model)
        self.inventory_handler = InventoryHandler()

        self.system_handler = SystemHandler()

    def run(self):
        """
        Запуск игры
        :return: None
        """
        while self.cur_state != State.EXIT:
            self.clock.tick(Config.FPS)
            for event in pygame.event.get():
                if self.cur_state == State.MENU:
                    self.cur_state = self.system_handler.run(event)
                elif self.cur_state == State.GAME:
                    self.cur_state = self.game_handler.run(event)
                elif self.cur_state == State.INVENTORY:
                    pass
        pygame.quit()


if __name__ == '__main__':
    app = App()
    app.run()
