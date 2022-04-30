from typing import List

from src.entities.passive_enemy import PassiveEnemy
from src.entities.aggressive_enemy import AggressiveEnemy
from src.entities.coward_enemy import CowardEnemy


class AbstractEnemyFactory:
    def get_required_images(self) -> List[str]:
        pass

    def create_passive_enemy(self, health: int, max_health: int, cell_pos, damage: int, exp_gain: int) -> PassiveEnemy:
        pass

    def create_aggressive_enemy(self, health: int, max_health: int, cell_pos, damage: int,
                                exp_gain: int, attack_radius: int) -> AggressiveEnemy:
        pass

    def create_coward_enemy(self, health, max_health: int, cell_pos, damage: int,
                            exp_gain: int, scare_radius: int) -> CowardEnemy:
        pass
