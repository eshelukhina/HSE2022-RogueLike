import pygame

from src.config import Config
from src.state import State
from src.views.system_view import SystemView


class SystemHandler:
    """
    Отвечает за работу с главным меню
    """

    def __init__(self):
        self.slots = []
        self.current_item = "Start"
        self.system_view = SystemView(Config.WINDOW_SIZE)
        self.system_view.display_menu()
        self.current_state = State.MENU
        self.init_menu = False

    def print_game(self) -> None:
        """Показать окно с меню, если оно еще не показывается"""
        if not self.init_menu:
            self.system_view.display_menu()
        self.init_menu = True

    def close_menu(self) -> None:
        """Поставить флаг, что окно с меню больше не показывается"""
        self.init_menu = False

    def run(self, event) -> State:
        """
        Определение и вызов обработки Event'ов
        :param event: Event, вызванный игроком
        :return State
        """
        self.print_game()
        if event.type == pygame.QUIT:
            self.current_state = State.EXIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                self.system_view.move_cursor(event.key)
            elif event.key == pygame.K_RETURN:
                if self.system_view.current_window == "Menu":
                    if self.system_view.current_item == "Exit":
                        self.system_view.press_exit()
                        self.close_menu()
                        self.current_state = State.EXIT
                    if self.system_view.current_item == "Start":
                        self.close_menu()
                        self.current_state = State.GAME
        return self.current_state