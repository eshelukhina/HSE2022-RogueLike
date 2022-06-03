from src.model.game_model import GameModel


class LevelLoader:
    """
    Интерфейс для загрузчиков уровней
    """

    def load(self, file_name: str) -> GameModel:
        """
        Конструирует и возвращает модель уровня, а также все загруженные картинки.

        :param file_name: имя файла уровня
        :return: модель уровня, содержащую все считаные из файла обьекты
        """
        pass
