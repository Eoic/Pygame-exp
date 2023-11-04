import uuid
import pygame.transform
from enum import Enum
from typing import Tuple
from core.world_object import WorldObject
from pygame import Vector2, key, K_w, K_s, K_a, K_d, sprite


class Player(WorldObject):
    class Direction(Enum):
        LEFT = 'Left'
        RIGHT = 'Right'

    id: uuid.UUID
    speed: float
    facing_direction: Direction

    def __init__(
        self,
        group: sprite.Group,
        speed: float = 0.0,
        position: Vector2 = Vector2(0, 0)
    ) -> None:
        super().__init__(position=position, image_path='assets/player.png', group=group, scale=0.10)
        self.id = uuid.uuid4()
        self.speed = speed
        self.facing_direction = self.Direction.RIGHT

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
            self.update_facing_direction()

    def set_speed(self, value: float) -> None:
        if value < 0:
            raise ValueError('Speed cannot be negative.')

        self.speed = value

    def set_color(self, color: Tuple[int, int, int]):
        self.color = color

    def get_facing_direction(self):
        if self.transform.direction.x < 0 and self.facing_direction != self.Direction.LEFT:
            return self.Direction.LEFT, True
        elif self.transform.direction.x > 0 and self.facing_direction != self.Direction.RIGHT:
            return self.Direction.RIGHT, True

        return self.facing_direction, False

    def update_facing_direction(self):
        if self.transform.direction.x == 0:
            return

        self.facing_direction, is_flip_x_needed = self.get_facing_direction()
        self.image = pygame.transform.flip(self.image, is_flip_x_needed, False)

    def __str__(self) -> str:
        return f'Player(id={self.id})'
