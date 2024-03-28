import pygame


class CameraGroup(pygame.sprite.Group):
    target: pygame.Vector2
    offset: pygame.Vector2
    surface: pygame.Surface

    def __init__(self, target=None):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.offset = pygame.Vector2(0, 0)
        self.target = target
        self.half_width = self.surface.get_size()[0] // 2
        self.half_height = self.surface.get_size()[1] // 2

    def center_to_target(self):
        if self.target is None:
            return

        self.offset.x = self.target.x - self.half_width
        self.offset.y = self.target.y - self.half_height

    def set_half_size(self, half_width: int, half_height: int):
        self.half_width = half_width
        self.half_height = half_height

    def custom_draw(self):
        self.center_to_target()

        for sprite in sorted(self.sprites(), key=lambda item: item.rect.centery):
            offset_position = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_position)

    def set_target(self, target: pygame.Vector2):
        self.target = target
