import uuid
from typing import Tuple

import pygame.transform

from core.transform import Transform
from pygame import Vector2, Surface, gfxdraw, key, K_w, K_s, K_a, K_d, sprite, image


class Player(sprite.Sprite):
    id: uuid.UUID
    size: int
    speed: float
    direction: Vector2
    transform: Transform
    color: Tuple[int, int, int]

    def __init__(
        self,
        group: sprite.Group,
        color: Tuple[int, int, int] = (0, 0, 0),
        size: int = 25,
        speed: float = 0.0
    ) -> None:
        super().__init__(group)
        self.id = uuid.uuid4()
        self.color = color
        self.size = size
        self.speed = speed
        self.transform = Transform()
        self.image = pygame.transform.scale_by(image.load('assets/player.png').convert_alpha(), 0.10)
        self.rect = self.image.get_rect()

    def handle_input(self):
        keys = key.get_pressed()
        direction = Vector2(0, 0)

        if keys[K_w]:
            direction.y = -1
        if keys[K_s]:
            direction.y = 1
        if keys[K_a]:
            direction.x = -1
        if keys[K_d]:
            direction.x = 1

        self.transform.set_direction(direction)

    def handle_update(self, delta_time: float):
        if self.transform.direction.length() != 0:
            self.transform.position += self.speed * delta_time * self.transform.direction.normalize()
            self.rect.center = self.transform.position

    def set_speed(self, value: float) -> None:
        if value < 0:
            raise ValueError('Speed cannot be negative.')

        self.speed = value

    def set_color(self, color: Tuple[int, int, int]):
        self.color = color

    def __str__(self) -> str:
        return f'Player(id={self.id})'
