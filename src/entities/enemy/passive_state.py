from src.entities.enemy.enemy_state import EnemyState


class PassiveState(EnemyState):
    """Класс, ответственный за тактику пассивнного противника"""

    def move(self, enemy, hero, enemies, cells):
        pass
