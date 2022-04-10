from enum import Enum, auto


class State(Enum):
    inventory = auto()
    menu = auto()
    game = auto()
    exit = auto()
