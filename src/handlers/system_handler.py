import pygame

from src.commands.exit_command import ExitCommand
from src.commands.keydown_command import KeydownCommand
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
        self.commands = {
            pygame.QUIT: ExitCommand(system_view=self.system_view),
            pygame.KEYDOWN: KeydownCommand(system_view=self.system_view)
        }

    def print_game(self) -> None:
        """Показать окно с меню, если оно еще не показывается"""
        if not self.system_view.init_menu:
            self.system_view.display_menu()
        self.system_view.init_menu = True

    def close_menu(self) -> None:
        """Поставить флаг, что окно с меню больше не показывается"""
        self.system_view.init_menu = False

    def run(self, event) -> State:
        """
        Определение и вызов обработки Event'ов
        :param event: Event, вызванный игроком
        :return State
        """
        self.print_game()
        if event.type in self.commands:
            if event.type == pygame.QUIT:
                self.current_state = self.commands[event.type].execute()
            else:
                self.current_state = self.commands[event.type].execute(event.key)
        return self.current_state
