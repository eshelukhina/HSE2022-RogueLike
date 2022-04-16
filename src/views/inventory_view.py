from typing import Tuple

import pygame


class InventoryView:
    """
    Класс ответственный за отображение инвентаря
    """
    def __init__(self, window_size: Tuple[int, int]):
        self.items = ["", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10", "item11",
                      "item12"]

        self.current_item = self.items[0]

        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        self.color_black = (0, 0, 0)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.bigfont = pygame.font.SysFont('Corbel', 40)
        start_text = self.smallfont.render(self.items[0], True, self.color)

        mid_w, mid_h = 160, 260

        counter = 0
        x = 20
        y = 20
        self.buttons = {}
        for item in self.items:
            if counter % 4 == 3:
                rect = pygame.Rect(mid_w + x, mid_h + y, 50, 50)
                y += 70
                x = 20
            else:
                rect = pygame.Rect(mid_w + x, mid_h + y, 50, 50)
                x += 100
            self.buttons[item] = (start_text, rect)
            counter += 1

    def display_menu(self) -> None:
        self.screen.fill((60, 25, 60))
        self.display_windows()
        self.display_items()
        self.display_current_items()
        pygame.display.update()

    def display_windows(self) -> None:
        current_items_rect = pygame.Rect(150, 50, 400, 150)
        pygame.draw.rect(self.screen, self.color_black, current_items_rect)
        all_items_rect = pygame.Rect(150, 250, 400, 250)
        pygame.draw.rect(self.screen, self.color_black, all_items_rect)

    def display_items(self) -> None:
        for button_key in self.buttons:
            button = self.buttons[button_key]
            if button_key == self.current_item:
                pygame.draw.rect(self.screen, self.color_light, button[1])
            else:
                pygame.draw.rect(self.screen, self.color_dark, button[1])
            self.screen.blit(button[0], (button[1].x + button[1].width / 3, button[1].y + button[1].height / 2))

    def display_current_items(self) -> None:
        current_item1_rect = pygame.Rect(170, 70, 355, 45)
        current_item2_rect = pygame.Rect(170, 135, 355, 45)
        pygame.draw.rect(self.screen, self.color_dark, current_item1_rect)
        pygame.draw.rect(self.screen, self.color_dark, current_item2_rect)

    def update_current_elem(self, direction, elem, arr) -> str:
        index = arr.index(elem)
        return arr[(index + direction) % len(arr)]

    def move_cursor_menu(self, key) -> None:
        if key == pygame.K_DOWN:
            self.current_item = self.update_current_elem(1, self.current_item, self.items)
        elif key == pygame.K_UP:
            self.current_item = self.update_current_elem(-1, self.current_item, self.items)
        self.display_menu()

    def move_cursor(self, key) -> None:
        self.move_cursor_menu(key)