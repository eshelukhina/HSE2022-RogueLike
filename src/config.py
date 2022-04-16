class Config:
    """
    Класс, хранящий в себе разделяемые всем приложением константные значения
    """
    WINDOW_SIZE = (720, 528)
    BLOCK_WIDTH = 24
    BLOCK_HEIGHT = 24
    FPS = 60
    PATH_TO_LEVELS = "levels"
    PATH_TO_TEXTURES = "textures"
    EXPERIENCE_TO_NEXT_LEVEL = 100
    CONFUSED_TIME = 3

    class Colors:
        RED = (153, 0, 0)
        GREY = (94, 94, 94)
        BLACK = (0, 0, 0)
        YELLOW = (255, 227, 112)
        BACKGROUND_COLOR = (0, 0, 0)
        WHITE = (255, 255, 255)
