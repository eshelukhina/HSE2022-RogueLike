from src.entities.enemy import Enemy


class CowardEnemy(Enemy):
    def __init__(self, health, cell_pos, image_key: int, damage: int, exp_gain: int, scare_radius: int):
        super().__init__(health, cell_pos, image_key, damage, exp_gain)
        self.scare_radius = scare_radius

    def move(self):
        pass