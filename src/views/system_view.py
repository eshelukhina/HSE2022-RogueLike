import pygame

from typing import Tuple


class SystemView:
    """
    Класс ответственный за отображение главного меню игры
    """

    def __init__(self, window_size: Tuple[int, int]):
        self.items = ["Start", "Reset progress", "Exit"]
        self.windows = ["Menu", "Save slots", "Choose job"]
        self.save_slots = ["Save slot 1", "Save slot 2"]
        self.save_slots_states = ["Start", "Reset"]
        self.save_slots_info = None

        self.current_item = self.items[0]
        self.current_window = self.windows[0]
        self.current_slot = self.save_slots[0]
        self.current_save_slots_state = None

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
        exit_text = self.bigfont.render(self.items[2], True, self.color)

        rect_w, rect_h = 250, 80
        mid_w, mid_h = self.width / 2, self.height / 2
        start_rect = pygame.Rect(mid_w, mid_h, rect_w, rect_h)
        start_rect.center = mid_w, mid_h - 100
        learn_about_rect = pygame.Rect(mid_w, mid_h + 60, rect_w, rect_h)
        learn_about_rect.center = mid_w, mid_h
        exit_rect = pygame.Rect(mid_w, mid_h + 120, rect_w, rect_h)
        exit_rect.center = mid_w, mid_h + 100

        self.buttons = {self.items[0]: (start_text, start_rect), self.items[1]: (learn_about_text, learn_about_rect),
                        self.items[2]: (exit_text, exit_rect)}

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
        :param arr: массив в котором находятся элементы на которые изменим текущий
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

    def move_cursor_save_slots(self, key) -> None:
        """
        Передвижение курсора по слотам
        :param key: кнопка нажатая пользователем
        :return: None
        """
        if key == pygame.K_DOWN:
            self.current_slot = self.update_current_elem(1, self.current_slot, self.save_slots)
        elif key == pygame.K_UP:
            self.current_slot = self.update_current_elem(-1, self.current_slot, self.save_slots)
        self.display_saving_slots()

    def move_cursor(self, key) -> None:
        """
        Передвижение курсора
        :param key: кнопка нажатая пользователем
        :return: None
        """
        if self.current_window == "Menu":
            self.move_cursor_menu(key)
        if self.current_window == "Save slots":
            self.move_cursor_save_slots(key)

    def display_saving_slots(self, slots=None) -> None:
        """
        Создание и отрисовка слотов
        :param slots: сохраненные состояния слотов
        :return: None
        """
        self.screen.fill((60, 25, 60))
        if slots is not None:
            self.save_slots_info = slots
        count_slots = 0
        y = 0
        for slot in self.save_slots_info:
            if count_slots == 0:
                y = 0
            elif count_slots == 1:
                y = 210
            if self.current_slot == self.save_slots[count_slots]:
                pygame.draw.rect(self.screen, self.color_dark, pygame.Rect(100, 100 + y, 500, 200))
            else:
                pygame.draw.rect(self.screen, self.color_light, pygame.Rect(100, 100 + y, 500, 200))
            if slot is None:
                slot_text = self.bigfont.render(self.save_slots[count_slots], True, self.color)
                rect_text = slot_text.get_rect()
                rect_text.center = (350, 120 + y)
                self.screen.blit(slot_text, rect_text)

                foremptyfont = pygame.font.SysFont('Corbel', 70)
                empty_slot_text = foremptyfont.render("Empty Slot", True, self.color)
                rect_text = empty_slot_text.get_rect()
                rect_text.center = (350, 200 + y)
                self.screen.blit(empty_slot_text, rect_text)

            if slot is not None:
                IMAGE = pygame.image.load('weapon.png').convert()
                rect_image = IMAGE.get_rect()
                rect_image.center = (550, 200 + y)
                self.screen.blit(IMAGE, rect_image)

                slot_text = self.bigfont.render(self.save_slots[count_slots], True, self.color)
                rect_text = slot_text.get_rect()
                rect_text.center = (350, 120 + y)
                self.screen.blit(slot_text, rect_text)

                slot_text = self.smallfont.render(self.save_slots[count_slots], True, self.color)
                rect_text = slot_text.get_rect()
                rect_text.topleft = (120, 145 + y)
                self.screen.blit(slot_text, rect_text)

                x = 145
                for i in range(1, 4):
                    x += 35
                    slot_text = self.smallfont.render(self.save_slots[count_slots], True, self.color)
                    rect_text = slot_text.get_rect()
                    rect_text.topleft = (120, x + y)
                    self.screen.blit(slot_text, rect_text)
                    x += 5
            count_slots += 1

        pygame.display.update()

    def press_exit(self) -> None:
        """
        Закрытие игры
        :return: None
        """
        pygame.quit()
        # clear later

    def press_start(self, slots) -> None:
        """
        Начало игры
        :param slots: сохраненные состояния слотов
        :return: None
        """
        self.current_window = "Save slots"
        self.current_save_slots_state = "Start"
        self.display_saving_slots(slots)

    def press_reset_(self, slots) -> None:
        """
        Стирание состояния слотов
        :param slots: сохраненные состояния слотов
        :return: None
        """
        self.current_window = "Save slots"
        self.current_save_slots_state = "Reset"
        self.display_saving_slots(slots)

    def press_choose_reset_save_slot(self) -> None:
        """
        Стирание выбранного слота
        :return: None
        """
        self.current_slot = None
        if self.save_slots_info is not None:
            if self.save_slots[0] == self.current_slot:
                self.save_slots_info[0] = None
            else:
                self.save_slots_info[1] = None
        self.current_window = "Menu"
        self.display_menu()
        return self.save_slots_info
