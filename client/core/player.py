import uuid
from typing import Tuple
from client.core import Transform
from pygame import draw, Vector2, Surface, gfxdraw


class Player:
    id: uuid.UUID
    size: int
    speed: float
    direction: Vector2
    transform: Transform
    color: Tuple[int, int, int]

    def __init__(self, color=(0, 0, 0), size=25, speed=0) -> None:
        self.id = uuid.uuid4()
        self.color = color
        self.size = size
        self.speed = speed
        self.transform = Transform()

    def set_speed(self, value: float) -> None:
        if value < 0:
            raise ValueError('Speed cannot be negative.')

        self.speed = value

    def move(self, delta_time: float):
        if self.transform.direction.length() == 0:
            return

        self.transform.position += self.speed * delta_time * self.transform.direction.normalize()

    def set_color(self, color: Tuple[int, int, int]):
        self.color = color

    def draw(self, screen: Surface) -> None:
        gfxdraw.aacircle(screen, int(self.transform.position.x), int(self.transform.position.y), self.size, self.color)
        gfxdraw.filled_circle(screen, int(self.transform.position.x), int(self.transform.position.y), self.size, self.color)
        # draw.circle(screen, self.color, (self.transform.position.x, self.transform.position.y), self.size)

    def __str__(self) -> str:
        return f'Player(id={self.id})'
