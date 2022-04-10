import pygame

from src.save_slot import SaveSlot
from src.state import State
from src.views.system_view import SystemView


class SystemHandler:
    def __init__(self):
        self.slots = []
        self.current_item = "Start"
        self.system_view = SystemView()
        self.system_view.display_menu()
        self.save_slots = SaveSlot().save_slots
        self.current_state = State.menu

    def run(self):
        for key_event in pygame.event.get():
            if key_event.type == pygame.QUIT:
                # no more for this iteration
                self.current_state = State.exit
            if key_event.type == pygame.KEYDOWN:
                if key_event.key == pygame.K_DOWN or key_event.key == pygame.K_UP:
                    self.system_view.move_cursor(key_event.key)
                elif key_event.key == pygame.K_RETURN:
                    if self.system_view.current_window == "Menu":
                        if self.system_view.current_item == "Exit":
                            self.system_view.press_exit()
                            self.current_state = State.exit
                        if self.system_view.current_item == "Start":
                            self.system_view.press_start(self.save_slots)
                        if self.system_view.current_item == "Reset progress":
                            self.system_view.press_reset_(self.save_slots)
                    elif self.system_view.current_window == "Save slots":
                        if self.system_view.current_save_slots_state == "Start":
                            self.current_state = State.game
                        elif self.system_view.current_save_slots_state == "Reset":
                            self.save_slots = self.system_view.press_choose_reset_save_slot()
        return self.current_state
