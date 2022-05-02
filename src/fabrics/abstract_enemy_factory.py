from typing import List

from src.entities.aggressive_enemy import AggressiveEnemy
from src.entities.coward_enemy import CowardEnemy
from src.entities.passive_enemy import PassiveEnemy
from src.entities.replicating_enemy import ReplicatingEnemy


class AbstractEnemyFactory:
    """
    Интерфейс фабрик по созданию мобов
    """

    def get_required_images(self) -> List[str]:
        """
        Получение списка названий всех необходимых для фабрики текстур

        :return: списка названий всех необходимых для фабрики текстур
        """
        pass

    def create_passive_enemy(self, health: int, max_health: int, cell_pos, damage: int, exp_gain: int) -> PassiveEnemy:
        """
        Метод для создания пассивного моба

        :param health: начальное здоровье
        :param max_health: максимальное здоровье
        :param cell_pos: начальное положение
        :param damage: урон моба
        :param exp_gain: количество опыта, начисляемое за убийство этого моба
        :return: экземпляр класса PassiveEnemy
        """
        pass

    def create_aggressive_enemy(self, health: int, max_health: int, cell_pos, damage: int,
                                exp_gain: int, attack_radius: int) -> AggressiveEnemy:
        """
        Метод для создания агрессивного моба

        :param health: начальное здоровье
        :param max_health: максимальное здоровье
        :param cell_pos: начальное положение
        :param damage: урон моба
        :param exp_gain: количество опыта, начисляемое за убийство этого моба
        :param attack_radius: радиус атаки
        :return: экземпляр класса AggressiveEnemy
        """
        pass

    def create_coward_enemy(self, health, max_health: int, cell_pos, damage: int,
                            exp_gain: int, scare_radius: int) -> CowardEnemy:
        """
        Метод для создания трусливого моба

        :param health: начальное здоровье
        :param max_health: максимальное здоровье
        :param cell_pos: начальное положение
        :param damage: урон моба
        :param exp_gain: количество опыта, начисляемое за убийство этого моба
        :param scare_radius: если расстояние до героя становится меньше scare_radius, то моб начинает убегать от героя
        :return: экземпляр класса CowardEnemy
        """
        pass

    def create_replicating_enemy(self, health, max_health: int, cell_pos, damage: int, exp_gain: int,
                                 chance_of_cloning: float) -> ReplicatingEnemy:
        """
        Метод для создания рециплицируещегося моба

        :param health: начальное здоровье
        :param max_health: максимальное здоровье
        :param cell_pos: начальное положение
        :param damage: урон моба
        :param exp_gain: количество опыта, начисляемое за убийство этого моба
        :param chance_of_cloning: шанс создания клона
        :return: экземпляр класса ReplicatingEnemy
        """
        pass
