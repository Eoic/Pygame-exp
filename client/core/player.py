import uuid
import pygame.transform
from enum import Enum
from typing import Tuple
from core.world_object import WorldObject
from pygame import Vector2, key, K_w, K_s, K_a, K_d, sprite
from core.math.interpolator import Interpolator


class Player(WorldObject):
    id: uuid.UUID
    speed: float

    def __init__(
        self,
        group: sprite.Group,
        speed: float = 0.0,
        position: Vector2 = Vector2(0, 0)
    ) -> None:
        super().__init__(image_path='assets/player.png', group=group, scale=0.10)
        self.id = uuid.uuid4()
        self.speed = speed
        self.acc_position = self.transform.position

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
            base = 50
            new_position = self.acc_position + self.speed * delta_time * self.transform.direction.normalize()
            self.acc_position = new_position
            new_position = pygame.Vector2(base * round(new_position.x / base), base * round(new_position.y / base))
            self.transform.position = new_position
            self.rect.center = self.transform.position

    def set_speed(self, value: float) -> None:
        if value < 0:
            raise ValueError('Speed cannot be negative.')

        self.speed = value

    def set_color(self, color: Tuple[int, int, int]):
        self.color = color

    def __str__(self) -> str:
        return f'Player(id={self.id})'
