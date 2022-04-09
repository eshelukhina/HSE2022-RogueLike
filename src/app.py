import pygame

from src.activity import Activity
from src.handlers.input_handler import InputHandler
from src.views.system_view import SystemView


class App:

    def __init__(self):
        pygame.init()
        self.menu = SystemView()
        self.input_handler = InputHandler()

    def run(self):
        self.menu.display_menu()
        self.input_handler.handle_input()
