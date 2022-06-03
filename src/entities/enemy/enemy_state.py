class EnemyState:
    """Интерфейс для стратегий моба"""

    def move(self, enemy, hero, enemies, cells):
        """
        Метод, отвечающий за ход противника согласно стратегии

        :param enemy: моб, который делает ход
        :param hero: герой
        :param enemies: список мобов
        :param cells: клетки карты
        :return: None
        """
        pass
