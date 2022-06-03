import pygame

from src.commands.exit_command import ExitCommand
from src.commands.keydown_command import KeydownCommand
from src.config import Config
from src.entities.armor import Armor
from src.entities.weapon import Weapon
from src.state import State
from src.views.inventory_view import InventoryView


class InventoryHandler:
    """
    Класс ответственный за обработку взаимодействия с инвентарем
    """

    def __init__(self):
        self.inventory = None
        self.inventory_view = InventoryView(Config.WINDOW_SIZE)
        self.current_state = State.INVENTORY
        self.game_model = None
        self.commands = {
            pygame.QUIT: ExitCommand(game_model=self.game_model, inventory_view=self.inventory_view),
            pygame.KEYDOWN: KeydownCommand(game_model=self.game_model, inventory_view=self.inventory_view)
        }


    def print_game(self) -> None:
        """Показать окно с инвентарем, если оно еще не показывается"""
        if not self.inventory_view.init_inventory:
            self.inventory_view.display_inventory()
        self.inventory_view.init_inventory = True

    def set_game_model(self, game_model) -> None:
        """Добавить информацию об игре (инвентарь, персонаж)
        :param game_model: информация об игре"""
        self.game_model = game_model
        self.commands = {
            pygame.QUIT: ExitCommand(game_model=self.game_model, inventory_view=self.inventory_view),
            pygame.KEYDOWN: KeydownCommand(game_model=self.game_model, inventory_view=self.inventory_view)
        }
        self.inventory_view.add_inventory(self.game_model.inventory)

    def run(self, event) -> State:
        """
        Определение и вызов обработки Event'ов
        :param event: Event, вызванный игроком
        :return: State
        """
        self.print_game()
        if event.type in self.commands:
            return self.commands[event.type].execute(event.key)
        return State.INVENTORY
