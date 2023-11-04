import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.surface.blit(sprite.image, sprite.rect)
