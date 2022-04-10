
import pygame


class Entity(pygame.sprite.Sprite):
    """
    Базовый класс, от которого наследуется любой отображаемый на игровом экране обьект.
    """
    def __init__(self, x: float, y: float, image: pygame.image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def draw(self, screen):
        """
        Метод для отрисовки объекта
        :param screen: экран
        :return: None
        """
        screen.blit(self.image, self.rect)
