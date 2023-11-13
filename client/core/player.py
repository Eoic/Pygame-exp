import uuid
import pygame.transform
from pygame import key, K_w, K_s, K_a, K_d
from core.constants import PIXELS_PER_UNIT
from core.world_object import WorldObject


class Player(WorldObject):
    id: uuid.UUID
    speed: float
    direction: pygame.Vector2

    def __init__(self, size: float, color: pygame.Color, speed: float = 0.0) -> None:
        super().__init__(color=color)
        self.id = uuid.uuid4()
        self.speed = speed
        self.acc_position = self.transform.position
        self.rect.size = [size, size]
        self.direction = pygame.Vector2(0, 0)

    def handle_input(self):
        keys = key.get_pressed()

        if keys[K_w] and self.direction.y != 1:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[K_s] and self.direction.y != -1:
            self.direction.x = 0
            self.direction.y = 1

        if keys[K_a] and self.direction.x != 1:
            self.direction.x = -1
            self.direction.y = 0
        elif keys[K_d] and self.direction.x != -1:
            self.direction.x = 1
            self.direction.y = 0

        self.transform.set_direction(self.direction)

    def handle_update(self, delta_time: float):
        if self.transform.direction.length() != 0:
            self.acc_position = self.acc_position + self.speed * delta_time * self.transform.direction.normalize()
            self.transform.position = pygame.Vector2(
                PIXELS_PER_UNIT * round(self.acc_position.x / PIXELS_PER_UNIT),
                PIXELS_PER_UNIT * round(self.acc_position.y / PIXELS_PER_UNIT)
            )

    def handle_render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def set_speed(self, value: float) -> None:
        if value < 0:
            raise ValueError('Speed cannot be negative.')

        self.speed = value

    def __str__(self) -> str:
        return f'Player(id={self.id})'
