import pygame
from core.transform import Transform


class WorldObject(pygame.sprite.Sprite):
    rect: pygame.Rect
    color: pygame.Color
    transform: Transform

    def __init__(self, color: pygame.Color):
        super().__init__()
        self.color = color
        self.transform = Transform()
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.transform.add_listener(self.handle_transform)

    def handle_transform(self, transform: Transform):
        self.rect.center = transform.position
