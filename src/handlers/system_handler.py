import pygame

from src.config import Config
from src.save_slot import SaveSlot
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
        self.save_slots = SaveSlot().save_slots
        self.current_state = State.MENU
        self.init_menu = False

    def print_game(self):
        if not self.init_menu:
            self.system_view.display_menu()
        self.init_menu = True

    def close_menu(self):
        self.init_menu = False

    def run(self, event):
        """
        Определение и вызов обработки Event'ов
        """
        self.print_game()
        if event.type == pygame.QUIT:
            # no more for this iteration
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
                        self.system_view.press_start(self.save_slots)
                    if self.system_view.current_item == "Reset progress":
                        self.system_view.press_reset_(self.save_slots)
                elif self.system_view.current_window == "Save slots":
                    if self.system_view.current_save_slots_state == "Start":
                        self.close_menu()
                        self.current_state = State.GAME
                    elif self.system_view.current_save_slots_state == "Reset":
                        self.system_view.press_choose_reset_save_slot()
        return self.current_state
