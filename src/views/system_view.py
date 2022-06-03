import pygame

from typing import Tuple


class SystemView:
    """
    Класс ответственный за отображение главного меню игры
    """

    def __init__(self, window_size: Tuple[int, int]):
        self.init_menu = False

        self.items = ["Start", "Exit"]
        self.windows = ["Menu"]

        self.current_item = self.items[0]
        self.current_window = self.windows[0]

        self.window_size = window_size
        self.screen = pygame.display.set_mode(self.window_size)
        self.color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.bigfont = pygame.font.SysFont('Corbel', 40)
        start_text = self.bigfont.render(self.items[0], True, self.color)
        learn_about_text = self.bigfont.render(self.items[1], True, self.color)

        rect_w, rect_h = 250, 80
        mid_w, mid_h = self.width / 2, self.height / 2
        start_rect = pygame.Rect(mid_w, mid_h, rect_w, rect_h)
        start_rect.center = mid_w, mid_h - 100
        learn_about_rect = pygame.Rect(mid_w, mid_h + 60, rect_w, rect_h)
        learn_about_rect.center = mid_w, mid_h
        exit_rect = pygame.Rect(mid_w, mid_h + 120, rect_w, rect_h)
        exit_rect.center = mid_w, mid_h + 100

        self.buttons = {self.items[0]: (start_text, start_rect), self.items[1]: (learn_about_text, learn_about_rect)}

    def close_menu(self) -> None:
        """Поставить флаг, что окно с меню больше не показывается"""
        self.init_menu = False

    def display_menu(self) -> None:
        """
        Создание экрана и вызов отрисовки элементов меню
        :return None
        """
        self.screen.fill((60, 25, 60))
        self.display_items()
        pygame.display.update()

    def display_items(self) -> None:
        """
        Создание и отрисовка элементов меню
        :return: None
        """
        for button_key in self.buttons:
            button = self.buttons[button_key]
            if button_key == self.current_item:
                pygame.draw.rect(self.screen, self.color_light, button[1])
            else:
                pygame.draw.rect(self.screen, self.color_dark, button[1])
            rect = button[0].get_rect()
            rect.center = button[1].center
            self.screen.blit(button[0], rect)

    def update_current_elem(self, direction, elem, arr) -> str:
        """
        Обновляет текущий выбранный элемент
        :param direction: Направление которое указал пользователь
        :param elem: элемент который нужно изменить
        :param arr: массив, в котором находятся элементы на которые изменим текущий
        :return: str
        """
        index = arr.index(elem)
        return arr[(index + direction) % len(arr)]

    def move_cursor_menu(self, key) -> None:
        """
        Передвижение курсора по меню
        :param key: кнопка нажатая пользователем
        :return: None
        """
        if key == pygame.K_DOWN:
            self.current_item = self.update_current_elem(1, self.current_item, self.items)
        elif key == pygame.K_UP:
            self.current_item = self.update_current_elem(-1, self.current_item, self.items)
        self.display_menu()

    def move_cursor(self, key) -> None:
        """
        Передвижение курсора
        :param key: кнопка нажатая пользователем
        :return: None
        """
        if self.current_window == "Menu":
            self.move_cursor_menu(key)

    def press_exit(self) -> None:
        """
        Закрытие игры
        :return: None
        """
        pygame.quit()
