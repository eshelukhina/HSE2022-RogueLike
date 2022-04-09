import pygame

from src.views.system_view import SystemView


class SystemHandler:
    def __init__(self):
        self.slots = []
        self.current_item = "Start"
        self.system_view = SystemView()
        self.system_view.display_menu()

    def run_event(self, key_event):
        if key_event == pygame.K_DOWN or key_event == pygame.K_UP:
            self.system_view.move_cursor(key_event)
        elif key_event == pygame.K_RETURN:
            self.system_view.choose_item()

