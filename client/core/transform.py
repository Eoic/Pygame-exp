from typing import Callable
from pygame import Vector2


class Transform:
    rotation: float
    position: Vector2
    direction: Vector2
    listeners: list[Callable[['Transform'], None]]

    def __init__(
        self,
        rotation: float = 0,
        position: Vector2 = Vector2(0, 0),
        direction: Vector2 = Vector2(0, 0)
    ):
        self.listeners = []
        self.rotation = rotation
        self.position = position
        self.direction = direction

    def set_rotation(self, rotation: float) -> None:
        self.rotation = rotation
        self.notify_listeners()

    def set_position(self, position: Vector2) -> None:
        self.position.x = round(position.x)
        self.position.y = round(position.y)
        self.notify_listeners()

    def set_direction(self, direction: Vector2) -> None:
        self.direction = direction
        self.notify_listeners()

    def add_listener(self, listener: Callable[['Transform'], None]):
        self.listeners.append(listener)

    def remove_listener(self, listener: Callable[['Transform'], None]):
        self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener(self)
