import pygame

from src.handlers.system_handler import SystemHandler
from src.state import State


class InputHandler:

    def __init__(self):
        self.state = State.menu
        self.game_running = True
        self.system_handler = SystemHandler()

    def handle_input(self):
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # no more for this iteration
                    self.game_running = False
                if event.type == pygame.KEYDOWN:
                    if self.state == State.menu:
                        self.system_handler.run_event(event.key)
