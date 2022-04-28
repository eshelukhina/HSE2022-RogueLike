import pygame

from src import state
from src.config import Config
from src.entities.armor import Armor
from src.entities.inventory import Inventory
from src.entities.weapon import Weapon
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
        self.game_model = None

    def print_game(self):
        if not self.init_inventory:
            self.inventory_view.display_inventory()
        self.init_inventory = True

    def close_inventory(self):
        self.init_inventory = False

    def set_game_model(self, game_model):
        self.game_model = game_model
        self.inventory_view.add_inventory(self.game_model.inventory)

    def run(self, event) -> State:
        """
        Определение и вызов обработки Event'ов
        :return: State
        """
        self.print_game()
        if event.type == pygame.QUIT:
            self.close_inventory()
            return State.EXIT
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP \
                    or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.inventory_view.move_cursor(event.key)
            elif event.key == pygame.K_RETURN:
                if self.inventory_view.show_item_buttons:
                    self.press_button()
                else:
                    self.inventory_view.display_item_handling()
            elif event.key == pygame.K_i:
                self.close_inventory()
                return State.GAME
        return State.INVENTORY

    def unequip_item(self):
        if self.game_model.inventory.equipped_armor == self.inventory_view.current_item:
            self.game_model.hero.unequip_armor()
        elif self.game_model.inventory.equipped_weapon == self.inventory_view.current_item:
            self.game_model.hero.unequip_weapon()
        self.game_model.inventory.unequip_item(self.inventory_view.current_item)

    def equip_item(self):
        if isinstance(self.game_model.inventory.items[self.inventory_view.current_item], Weapon):
            self.game_model.hero.equip_weapon(self.game_model.inventory.items[self.inventory_view.current_item])
        elif isinstance(self.game_model.inventory.items[self.inventory_view.current_item], Armor):
            self.game_model.hero.equip_armor(self.game_model.inventory.items[self.inventory_view.current_item])
        self.game_model.inventory.equip_item(self.inventory_view.current_item)

    def press_button(self):
        if self.inventory_view.current_option_button == 0:
            self.unequip_item()
            self.game_model.inventory.discard_item(self.inventory_view.current_item)
        elif self.inventory_view.current_option_button == 1:
            if not self.inventory_view.is_item_equipped():
                self.equip_item()
            else:
                self.unequip_item()
        self.inventory_view.show_item_buttons = False
        self.inventory_view.display_inventory()
