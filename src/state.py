from enum import Enum, auto


class State(Enum):
    """
    Enum класс, обозначающий текущее состояние приложения
    """
    INVENTORY = auto()
    MENU = auto()
    GAME = auto()
    EXIT = auto()
