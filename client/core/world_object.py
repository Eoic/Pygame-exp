import pygame
from core.transform import Transform


class WorldObject(pygame.sprite.Sprite):
    transform: Transform

    def __init__(
        self,
        image_path: str,
        group: pygame.sprite.Group,
        scale: float = 1
    ):
        super().__init__(group)
        self.transform = Transform()
        self.image = pygame.transform.scale_by(pygame.image.load(image_path).convert_alpha(), scale)
        self.rect = self.image.get_rect(center=self.transform.position)
        self.transform.add_listener(self.handle_transform)

    def handle_transform(self, transform: Transform):
        self.rect.center = transform.position
