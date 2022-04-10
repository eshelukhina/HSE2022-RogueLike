import pygame

from src.save_slot import SaveSlot
from src.views.system_view import SystemView


class SystemHandler:
    def __init__(self):
        self.slots = []
        self.current_item = "Start"
        self.system_view = SystemView()
        self.system_view.display_menu()
        self.save_slots = SaveSlot().save_slots

    def run_event(self, key_event):
        if key_event == pygame.K_DOWN or key_event == pygame.K_UP:
            self.system_view.move_cursor(key_event)
        elif key_event == pygame.K_RETURN:
            if self.system_view.current_item == "Exit":
                self.system_view.press_exit()
            if self.system_view.current_item == "Start":
                self.system_view.press_start(self.save_slots)
            if self.system_view.current_item == "Reset progress":
                if self.system_view.current_slot == "Save slot 1":
                    self.save_slots[0] = None
                else:
                    self.save_slots[1] = None
                self.system_view.display_saving_slots(self.save_slots)
