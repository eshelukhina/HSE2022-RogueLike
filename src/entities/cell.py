import enum


class CellType(enum.Enum):
    Empty = 0
    Wall = 1
    Chest = 2
    CairnOfPassage = 3


class Cell:
    """
    Элемент карты
    """
    images = []

    def __init__(self, *, image_key: int, cell_type: CellType):
        self.image_key = image_key
        self.cell_type = cell_type
