import random
import pygame


class RandomLevelBuilder:

    def __init__(self):
        self.room_rects = []
        self.cell_types = []

    def load(self, width: int, height: int):

        for i in range(height + 1):
            temp = []
            for j in range(width + 1):
                temp.append(1)
            self.cell_types.insert(i, temp)
        print(height, width)

        max_room_size = int(height / 3)
        min_room_size = 4

        max_room_number = int(height * width / ((max_room_size + 2) * (max_room_size + 2)))
        min_room_number = 4

        room_number = random.randint(min_room_number, max_room_number)

        counter = 0
        for i in range(0, room_number):
            w, h = random.randint(min_room_size, max_room_size), random.randint(min_room_size, max_room_size)
            diff_x = 1
            diff_y = 1

            if counter != 0:
                pred_rect = self.room_rects[counter - 1]
                diff_x = pred_rect.x + pred_rect.width + 2
                diff_y = pred_rect.y + pred_rect.height + 2

            is_smaller_x = diff_x <= width
            is_smaller_y = diff_y <= height

            if is_smaller_x and is_smaller_y:
                pos_x, pos_y = random.randint(diff_x, width), random.randint(diff_y, height)
                if pos_x + w < width and pos_y + h < height:
                    counter += 1
                    self.room_rects.append(
                        pygame.rect.Rect(pos_x, pos_y, w, h)
                    )

                    for j in range(pos_y, pos_y + h):
                        for k in range(pos_x, pos_x + w):
                            print(j, k)
                            self.cell_types[j][k] = 0
