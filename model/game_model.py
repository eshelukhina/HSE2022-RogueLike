from entities.hero import Hero


class GameModel:
    def __init__(self, cells, hero, enemies):
        self.cells = cells
        self.hero: Hero = hero
        self.enemies = enemies

    def get_all_entities(self):
        return self.get_cells() + self.get_enemies() + ([] if self.hero is None else [self.hero])

    def get_cells(self):
        if self.cells is None:
            return []
        return self.cells

    def get_hero(self):
        return self.hero

    def get_enemies(self):
        if self.enemies is None:
            return []
        return self.enemies
