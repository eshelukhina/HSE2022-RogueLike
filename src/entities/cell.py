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

    def __init__(self, *, image_name: str, cell_type: CellType):
        self.image_name = image_name
        self.cell_type = cell_type
