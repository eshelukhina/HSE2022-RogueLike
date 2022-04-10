import pygame

# from src.handler.game_handler import GameHandler
from src.handler.game_handler import GameHandler
from src.loader.default_level_loader import DefaultLeverLoader
from src.view.game_view import GameView
from src.state import State
# from src.handler import GameHandler
from src.handler.inventory_handler import InventoryHandler

# from src.loader.default_level_loader import DefaultLeverLoader

# from src.view import GameView
from src.view.inventory_view import InventoryView


class App:
    """
    Главный класс, ответственный за запуск игры
    """
    WINDOW_SIZE = (720, 528)
    BLOCK_WIDTH = 48
    BLOCK_HEIGHT = 48
    FPS = 60

    def __init__(self):
        pygame.init()
        self.cur_state = State.game
        self.game_handler = GameHandler()
        self.inventory_handler = InventoryHandler()

        self.game_view = GameView(self.WINDOW_SIZE)
        self.inventory_view = InventoryView()

        self.level_loader = DefaultLeverLoader(block_width=self.BLOCK_WIDTH, block_height=self.BLOCK_HEIGHT)
        self.game_model = None


    def run(self):
        """
        Запуск игры
        :return: None
        """
        self.game_model = self.level_loader.load('default')
        while self.cur_state != State.exit:
            if self.cur_state == State.menu:
                pass
            elif self.cur_state == State.game:
                #TODO bootstrap game mode from menu
                self.game_view.view_load(self.game_model.get_all_entities())
                self.cur_state = self.game_handler.run(self.game_model)
            elif self.cur_state == State.inventory:
                pass
        pygame.quit()


if __name__ == '__main__':
    app = App()
    app.run()
