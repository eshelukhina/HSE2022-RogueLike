import pygame

from src.handlers.input_handler import InputHandler


class App:

    def __init__(self):
        pygame.init()
        self.input_handler = InputHandler()

    def run(self):
        self.input_handler.handle_input()
