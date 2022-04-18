import pygame

from src import state
from src.config import Config
from src.entities.inventory import Inventory
from src.state import State
from src.views.inventory_view import InventoryView


class InventoryHandler:
    """
    Класс ответственен за обработку взаимодействия с инвентарем
    """

    def __init__(self):
        self.inventory = None
        self.inventory_view = InventoryView(Config.WINDOW_SIZE)
        self.current_state = State.INVENTORY
        self.init_inventory = False

    def print_game(self):
        if not self.init_inventory:
            self.inventory_view.display_inventory()
        self.init_inventory = True

    def close_inventory(self):
        self.init_inventory = False

    def set_inventory(self, inventory):
        self.inventory = inventory
        self.inventory_view.add_inventory(inventory)

    def run(self, event) -> State:
        """
        Определение и вызов обработки Event'ов
        :return: State
        """
        self.print_game()
        if event.type == pygame.QUIT:
            # no more for this iteration
            state.state_machine = State.EXIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP \
                    or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.inventory_view.move_cursor(event.key)
            elif event.key == pygame.K_RETURN:
                if self.inventory_view.show_item_buttons:
                    self.inventory_view.press_button()
                else:
                    self.inventory_view.display_item_handling()
        return self.current_state
