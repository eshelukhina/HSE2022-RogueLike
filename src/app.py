import pygame

from src.handlers.system_handler import SystemHandler
from src.state import State


class App:
    WINDOW_SIZE = (720, 528)
    BLOCK_WIDTH = 48
    BLOCK_HEIGHT = 48
    FPS = 60

    def __init__(self):
        pygame.init()
        self.cur_state = State.menu
        self.system_handler = SystemHandler()

    def run(self):
        while self.cur_state != State.exit:
            if self.cur_state == State.menu:
                self.cur_state = self.system_handler.run()
