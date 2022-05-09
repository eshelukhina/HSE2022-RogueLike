from typing import Optional

from src.entities.armor import Armor
from src.entities.weapon import Weapon
from src.model.game_model import GameModel
from src.state import State
from src.views.inventory_view import InventoryView
from src.views.system_view import SystemView


class ReturnCommand:
    """Класс, ответственный за логику выбора пользователя в игре"""

    def __init__(self, game_model: Optional[GameModel] = None, system_view: SystemView = None,
                 inventory_view: InventoryView = None):
        self.game_model = game_model
        self.system_view = system_view
        self.inventory_view = inventory_view

    def unequip_item(self) -> None:
        """Снять с персонажа выбранный в инвентаре предмет"""
        if self.game_model.inventory.equipped_armor == self.inventory_view.current_item:
            self.game_model.hero.unequip_armor()
        elif self.game_model.inventory.equipped_weapon == self.inventory_view.current_item:
            self.game_model.hero.unequip_weapon()
        self.game_model.inventory.unequip_item(self.inventory_view.current_item)

    def equip_item(self) -> None:
        """Надеть на персонажа выбранный в инвентаре предмет"""
        if isinstance(self.game_model.inventory.items[self.inventory_view.current_item], Weapon):
            self.game_model.hero.equip_weapon(self.game_model.inventory.items[self.inventory_view.current_item])
        elif isinstance(self.game_model.inventory.items[self.inventory_view.current_item], Armor):
            self.game_model.hero.equip_armor(self.game_model.inventory.items[self.inventory_view.current_item])
        self.game_model.inventory.equip_item(self.inventory_view.current_item)

    def press_button(self) -> None:
        """Нажать на кнопку для возможных действий с выбраннным предметом (discard, equip/unequip, cancel)"""
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

    def execute(self, key: int) -> State:
        """
        Логика обработки выбора пользователя
        :param key: pygame.key: Int, кнопка которую нажал игрок
        :return State
        """
        if self.inventory_view is not None:
            if self.inventory_view.show_item_buttons:
                self.press_button()
            else:
                self.inventory_view.display_item_handling()
            return State.INVENTORY
        elif self.system_view is not None:
            if self.system_view.current_window == "Menu":
                if self.system_view.current_item == "Exit":
                    self.system_view.press_exit()
                    self.system_view.close_menu()
                    return State.EXIT
                if self.system_view.current_item == "Start":
                    self.system_view.close_menu()
                    return State.GAME
        else:
            return State.GAME
