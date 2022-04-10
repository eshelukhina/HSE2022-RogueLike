# import pygame
#
# from handler.game_handler import GameHandler
# from state import State
# from view.game_view import GameView
#
#
# class InputHandler:
#
#     def __init__(self):
#         self.state = State.menu
#         self.game_running = True
#         self.game_handler = GameHandler()
#         self.view = GameView()
#
#     def handle_input(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.game_running = False
#             if event.type == pygame.KEYDOWN:
#                 if self.state == State.game:
#                     self.game_handler.run_event(event.key)
# TODO УБИТЬ НАХУЙ