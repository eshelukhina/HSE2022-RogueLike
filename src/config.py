import pygame


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

    movement = {
        pygame.K_LEFT: (-1, 0),
        pygame.K_RIGHT: (1, 0),
        pygame.K_UP: (0, -1),
        pygame.K_DOWN: (0, 1)
    }

    class Colors:
        RED = (153, 0, 0)
        GREY = (94, 94, 94)
        BLACK = (0, 0, 0)
        YELLOW = (255, 227, 112)
        BACKGROUND_COLOR = (28, 17, 23)
        WHITE = (255, 255, 255)
