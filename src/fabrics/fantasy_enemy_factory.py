import random
from typing import List

from src.entities.aggressive_enemy import AggressiveEnemy
from src.entities.coward_enemy import CowardEnemy
from src.entities.passive_enemy import PassiveEnemy
from src.entities.replicating_enemy import ReplicatingEnemy
from src.fabrics.abstract_enemy_factory import AbstractEnemyFactory


class FantasyEnemyFactory(AbstractEnemyFactory):
    def __init__(self):
        random.seed()
        self.images = {
            PassiveEnemy.__name__: ['skeleton.png', 'tiny_zombie.png'],
            AggressiveEnemy.__name__: ['devil.png'],
            CowardEnemy.__name__: ['green_lizard.png'],
            ReplicatingEnemy.__name__: ['goblin.png', 'wood_goblin.png']
        }

    def get_required_images(self) -> List[str]:
        res: List[str] = []
        for elem in self.images.values():
            res += elem
        return res

    def __get_image__(self, enemy):
        enemy_images = self.images[enemy.__name__]
        return enemy_images[random.randint(0, len(enemy_images) - 1)]

    def create_passive_enemy(self, health: int, max_health: int, cell_pos, damage: int, exp_gain: int) -> PassiveEnemy:
        passive_enemy_image = self.__get_image__(PassiveEnemy)
        return PassiveEnemy(health=health, max_health=max_health, cell_pos=cell_pos, damage=damage,
                            exp_gain=exp_gain, image_name=passive_enemy_image)

    def create_aggressive_enemy(self, health: int, max_health: int, cell_pos, damage: int, exp_gain: int,
                                attack_radius: int) -> AggressiveEnemy:
        aggressive_enemy_image = self.__get_image__(AggressiveEnemy)
        return AggressiveEnemy(health=health, max_health=health, cell_pos=cell_pos, attack_radius=attack_radius,
                               damage=damage, exp_gain=exp_gain, image_name=aggressive_enemy_image)

    def create_coward_enemy(self, health, max_health: int, cell_pos, damage: int, exp_gain: int,
                            scare_radius: int) -> CowardEnemy:
        coward_enemy_image = self.__get_image__(CowardEnemy)
        return CowardEnemy(health=health, max_health=health, cell_pos=cell_pos, scare_radius=scare_radius,
                           image_name=coward_enemy_image, damage=damage, exp_gain=exp_gain)

    def create_replicating_enemy(self, health, max_health: int, cell_pos, damage: int, exp_gain: int,
                                 chance_of_cloning: float) -> ReplicatingEnemy:
        replicating_enemy_image = self.__get_image__(ReplicatingEnemy)
        return ReplicatingEnemy(health=health, max_health=health, cell_pos=cell_pos,
                                chance_of_cloning=chance_of_cloning,
                                image_name=replicating_enemy_image, damage=damage, exp_gain=exp_gain)
