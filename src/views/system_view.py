from typing import Tuple

import pygame


class SystemView:
    def __init__(self):
        self.items = ["Start", "Learn about", "Exit"]
        self.current_item = self.items[0]
        self.res = (720, 720)
        self.screen = pygame.display.set_mode(self.res)
        self.color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.smallfont = pygame.font.SysFont('Corbel', 35)
        start_text = self.smallfont.render(self.items[0], True, self.color)
        learn_about_text = self.smallfont.render(self.items[1], True, self.color)
        exit_text = self.smallfont.render(self.items[2], True, self.color)

        mid_w, mid_h = self.width / 2, self.height / 2
        start_rect = pygame.Rect(mid_w, mid_h, 150, 50)
        learn_about_rect = pygame.Rect(mid_w, mid_h + 60, 150, 50)
        exit_rect = pygame.Rect(mid_w, mid_h + 120, 150, 50)
        self.buttons = {self.items[0]: (start_text, start_rect), self.items[1]: (learn_about_text, learn_about_rect),
                        self.items[2]: (exit_text, exit_rect)}

    def display_menu(self):
        self.screen.fill((60, 25, 60))
        self.display_items()
        pygame.display.update()

    def display_items(self):
        for button_key in self.buttons:
            button = self.buttons[button_key]
            if button_key == self.current_item:
                pygame.draw.rect(self.screen, self.color_light, button[1])
            else:
                pygame.draw.rect(self.screen, self.color_dark, button[1])
            self.screen.blit(button[0], (button[1].x + button[1].width / 3, button[1].y + button[1].height / 2))

    def update_current_item(self, direction):
        index = self.items.index(self.current_item)
        self.current_item = self.items[(index + direction) % len(self.items)]

    def move_cursor(self, key):
        if key == pygame.K_DOWN:
            self.update_current_item(1)
        elif key == pygame.K_UP:
            self.update_current_item(-1)
        self.display_menu()
