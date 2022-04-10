from enum import Enum, auto


class State(Enum):
    """
    Enum класс, обозначающий текущее состояние приложения
    """
    inventory = auto()
    menu = auto()
    game = auto()
    exit = auto()
