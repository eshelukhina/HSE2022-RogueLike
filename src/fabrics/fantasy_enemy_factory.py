import random
from typing import List

from src.entities.enemy.aggressive_state import AggressiveState
from src.entities.enemy.coward_state import CowardState
from src.entities.enemy.enemy import Enemy
from src.entities.enemy.passive_state import PassiveState
from src.entities.enemy.replicating_state import ReplicatingState
from src.fabrics.abstract_enemy_factory import AbstractEnemyFactory


class FantasyEnemyFactory(AbstractEnemyFactory):
    """
    Фабрика по созданию мобов
    """

    def __init__(self):
        random.seed()
        self.images = {
            PassiveState.__name__: ['skeleton.png', 'tiny_zombie.png'],
            AggressiveState.__name__: ['devil.png'],
            CowardState.__name__: ['green_lizard.png'],
            ReplicatingState.__name__: ['goblin.png', 'wood_goblin.png']
        }

    def get_required_images(self) -> List[str]:
        res: List[str] = []
        for elem in self.images.values():
            res += elem
        return res

    def __get_image__(self, enemy):
        enemy_images = self.images[enemy.__name__]
        return enemy_images[random.randint(0, len(enemy_images) - 1)]

    def create_passive_enemy(self, health: int, max_health: int, cell_pos, damage: int, exp_gain: int) -> Enemy:
        passive_enemy_image = self.__get_image__(PassiveState)
        return Enemy(health=health, max_health=max_health, cell_pos=cell_pos, damage=damage,
                     exp_gain=exp_gain, image_name=passive_enemy_image, state=PassiveState())

    def create_aggressive_enemy(self, health: int, max_health: int, cell_pos, damage: int, exp_gain: int,
                                attack_radius: int) -> Enemy:
        aggressive_enemy_image = self.__get_image__(AggressiveState)
        return Enemy(health=health, max_health=health, cell_pos=cell_pos, damage=damage, exp_gain=exp_gain,
                     image_name=aggressive_enemy_image, state=AggressiveState(attack_radius=attack_radius))

    def create_coward_enemy(self, health, max_health: int, cell_pos, damage: int, exp_gain: int,
                            scare_radius: int) -> Enemy:
        coward_enemy_image = self.__get_image__(CowardState)
        return Enemy(health=health, max_health=health, cell_pos=cell_pos, image_name=coward_enemy_image,
                     damage=damage, exp_gain=exp_gain, state=CowardState(scare_radius=scare_radius))

    def create_replicating_enemy(self, health, max_health: int, cell_pos, damage: int, exp_gain: int,
                                 chance_of_cloning: float) -> Enemy:
        replicating_enemy_image = self.__get_image__(ReplicatingState)
        return Enemy(health=health, max_health=health, cell_pos=cell_pos, image_name=replicating_enemy_image,
                     damage=damage, exp_gain=exp_gain, state=ReplicatingState(chance_of_cloning))
