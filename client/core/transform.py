from pygame import Vector2


class Transform:
    rotation: float
    position: Vector2
    direction: Vector2

    def __init__(
        self,
        rotation: float = 0,
        position: Vector2 = Vector2(0, 0),
        direction: Vector2 = Vector2(0, 0)
    ):
        self.rotation = rotation
        self.position = position
        self.direction = direction

    def set_rotation(self, rotation: float) -> None:
        self.rotation = rotation

    def set_position(self, position: Vector2) -> None:
        self.position = position

    def set_direction(self, direction: Vector2) -> None:
        self.direction = direction
