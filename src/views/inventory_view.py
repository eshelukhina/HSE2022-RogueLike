from typing import Tuple

import pygame


class InventoryView:
    """
    Класс ответственный за отображение инвентаря
    """

    def __init__(self, window_size: Tuple[int, int]):
        self.option_button = {}
        self.buttons = {"Equipped gear": ["Discard", "Put Off", "Cancel"],
                        "Unequipped gear": ["Discard", "Put On", "Cancel"],
                        "Potion": ["Discard", "Use", "Cancel"]}

        self.current_item = 0
        self.show_item_buttons = False

        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        self.color_black = (0, 0, 0)
        self.color_red = (170, 0, 0)
        self.color_options = (36, 30, 42)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.smallfont = pygame.font.SysFont('Corbel', 25)
        self.bigfont = pygame.font.SysFont('Corbel', 40)
        self.len = 4
        self.num_of_items = self.len * 3

        mid_w, mid_h = 160, 190

        counter = 0
        x = 20
        y = 20
        self.items = []
        for i in range(self.num_of_items):
            if counter % self.len == 3:
                rect = pygame.Rect(mid_w + x, mid_h + y, 50, 50)
                y += 70
                x = 20
            else:
                rect = pygame.Rect(mid_w + x, mid_h + y, 50, 50)
                x += 100
            self.items.append(rect)
            counter += 1

    def add_inventory(self, inventory) -> None:
        self.inventory = inventory

    def display_inventory(self) -> None:
        self.screen.fill((60, 25, 60))
        self.display_windows()
        self.display_items()
        self.display_current_items()
        pygame.display.update()

    def display_item_handling(self) -> None:
        self.show_item_buttons = True
        rect = self.items[self.current_item]
        current_item_options_rect = pygame.Rect(rect.centerx, rect.centery, 200, 100)
        current_item_options_rect.bottomleft = rect.center
        pygame.draw.rect(self.screen, self.color_options, current_item_options_rect)
        is_equipped = "Unequipped gear"
        if self.current_item == self.inventory.equipped_weapon or self.current_item == self.inventory.equipped_armor:
            is_equipped = "Equipped gear"
        diff = 0
        for text in self.buttons[is_equipped]:
            unequipped_text = self.smallfont.render(text, True, self.color)
            x, y = current_item_options_rect.x + 10, current_item_options_rect.y + 5
            unequipped_rect = pygame.Rect(x, y + diff, 180, 25)
            diff += 33
            self.option_button[text] = (unequipped_text, unequipped_rect)
            self.display_options()
        pygame.display.update()

    def display_options(self) -> None:
        for key, value in self.option_button.items():
            pygame.draw.rect(self.screen, self.color_light, value[1])
            rect = value[0].get_rect()
            rect.center = value[1].center
            self.screen.blit(value[0], rect)

    def display_windows(self) -> None:
        current_items_rect = pygame.Rect(150, 10, 400, 150)
        pygame.draw.rect(self.screen, self.color_black, current_items_rect)
        all_items_rect = pygame.Rect(150, 180, 400, 250)
        pygame.draw.rect(self.screen, self.color_black, all_items_rect)
        description_rect = pygame.Rect(150, 450, 400, 45)
        pygame.draw.rect(self.screen, self.color_black, description_rect)

    def display_items(self) -> None:
        for i in range(self.num_of_items):
            if i == self.current_item:
                pygame.draw.rect(self.screen, self.color_light, self.items[i])
            elif i == self.inventory.equipped_armor or i == self.inventory.equipped_weapon:
                pygame.draw.rect(self.screen, self.color_red, self.items[i])
            else:
                pygame.draw.rect(self.screen, self.color_dark, self.items[i])

    def display_current_items(self) -> None:
        current_item1_rect = pygame.Rect(170, 30, 355, 45)
        current_item2_rect = pygame.Rect(170, 100, 355, 45)
        pygame.draw.rect(self.screen, self.color_dark, current_item1_rect)
        pygame.draw.rect(self.screen, self.color_dark, current_item2_rect)

    def update_current_elem(self, direction, index, arr) -> str:
        return (index + direction) % len(arr)

    def move_cursor_menu(self, key) -> None:
        if key == pygame.K_DOWN:
            self.current_item = self.update_current_elem(self.len, self.current_item, self.items)
        elif key == pygame.K_UP:
            self.current_item = self.update_current_elem(-self.len, self.current_item, self.items)
        elif key == pygame.K_LEFT:
            self.current_item = self.update_current_elem(-1, self.current_item, self.items)
        elif key == pygame.K_RIGHT:
            self.current_item = self.update_current_elem(1, self.current_item, self.items)
        self.display_inventory()

    def move_cursor_item_handling(self, key) -> None:
        pass

    def move_cursor(self, key) -> None:
        if self.show_item_buttons:
            self.move_cursor_item_handling(key)
        else:
            self.move_cursor_menu(key)

    def press_button(self):
        pass
