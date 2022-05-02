from src.entities.enemy import Enemy


class PassiveEnemy(Enemy):
    """Класс, ответственный за тактику пассивнного противника"""
    def __init__(self, health: int, max_health: int, cell_pos, image_name: str, damage: int, exp_gain: int):
        super().__init__(health, max_health, cell_pos, image_name, damage, exp_gain)