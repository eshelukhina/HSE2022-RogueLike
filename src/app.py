import pygame

from src.config import Config
from src.entities.inventory import Inventory
from src.handlers.game_handler import GameHandler
from src.handlers.inventory_handler import InventoryHandler
from src.handlers.system_handler import SystemHandler
from src.loader.default_level_loader import DefaultLeverLoader
from src.state import State
from src.views.game_view import GameView


class App:
    """
    Главный класс, ответственный за запуск игры
    """

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.cur_state = State.MENU

        level_loader = DefaultLeverLoader(path_to_levels='levels', path_to_textures='textures')
        self.game_model = level_loader.load('default.json')

        self.game_handler = GameHandler(
            game_view=GameView(window_size=Config.WINDOW_SIZE,
                               cell_size=(Config.BLOCK_WIDTH, Config.BLOCK_HEIGHT),
                               image_dict=self.game_model.image_dict),
            game_model=self.game_model)
        self.inventory = Inventory()
        self.inventory_handler = InventoryHandler(self.inventory)

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
                    # todo not pretty but this what is needed to be done
                    if self.cur_state == State.GAME:
                        self.game_handler.print_game()
                elif self.cur_state == State.GAME:
                    self.cur_state = self.game_handler.run(event)
                elif self.cur_state == State.INVENTORY:
                    self.cur_state = self.inventory_handler.run(event)
        pygame.quit()


if __name__ == '__main__':
    app = App()
    app.run()
