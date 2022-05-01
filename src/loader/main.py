from src.loader.random_level_builder import RandomLevelBuilder
import numpy as np

if __name__ == '__main__':
    rndlvl = RandomLevelBuilder()
    rndlvl.load(30, 22)

    print(rndlvl.room_rects)
    print(np.matrix(rndlvl.cell_types))



