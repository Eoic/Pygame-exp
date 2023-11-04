from pygame import Vector2


class Transform:
    rotation: float
    position: Vector2
    direction: Vector2

    def __init__(self):
        self.rotation = 0
        self.position = Vector2(0, 0)
        self.direction = Vector2(0, 0)

    def set_rotation(self, rotation: float) -> None:
        self.rotation = rotation

    def set_position(self, position: Vector2) -> None:
        self.position = position

    def set_direction(self, direction: Vector2) -> None:
        self.direction = direction
