from src.entities.enemy import Enemy


class PassiveEnemy(Enemy):
    def __init__(self, health, cell_pos, image_key: int, damage: int, exp_gain: int):
        super().__init__(health, cell_pos, image_key, damage, exp_gain)
