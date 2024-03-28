import uuid
import pygame.transform
from pygame import key, K_w, K_s, K_a, K_d
from core.constants import PIXELS_PER_UNIT, CELL_SIZE, WORLD_WIDTH, WORLD_HEIGHT
from core.world_object import WorldObject
from core.food_spawner import FoodSpawner


class Player(WorldObject):
    id: uuid.UUID
    size = 0
    speed: float
    direction: pygame.Vector2
    trail: list[pygame.Vector2] = []

    def __init__(self, size: float, color: pygame.Color, food_spawner: FoodSpawner, speed: float = 0.0) -> None:
        super().__init__(color=color)
        self.id = uuid.uuid4()
        self.speed = speed
        self.acc_position = self.transform.position
        self.rect.size = [size, size]
        self.direction = pygame.Vector2(0, 0)
        self.food_spawner = food_spawner

    def handle_input(self):
        keys = key.get_pressed()

        if keys[K_w] and self.direction.y != 1:
            self.direction.x = 0
            self.direction.y = -1
        elif keys[K_s] and self.direction.y != -1:
            self.direction.x = 0
            self.direction.y = 1
        elif keys[K_a] and self.direction.x != 1:
            self.direction.x = -1
            self.direction.y = 0
        elif keys[K_d] and self.direction.x != -1:
            self.direction.x = 1
            self.direction.y = 0

        self.transform.set_direction(self.direction)

    def handle_update(self, delta_time: float):
        if self.transform.direction.length() != 0:
            self.acc_position = self.acc_position + self.speed * delta_time * self.transform.direction.normalize()

            next_position = pygame.Vector2(
                PIXELS_PER_UNIT * round(self.acc_position.x / PIXELS_PER_UNIT),
                PIXELS_PER_UNIT * round(self.acc_position.y / PIXELS_PER_UNIT)
            )

            if self.transform.position == next_position:
                return

            prev_position = pygame.Vector2(self.transform.position.x, self.transform.position.y)

            if next_position.x >= WORLD_WIDTH:
                next_position.x = 50
                self.acc_position.x = 50
            elif next_position.x < 50:
                next_position.x = WORLD_WIDTH - 50
                self.acc_position.x = WORLD_WIDTH - 50

            if next_position.y >= WORLD_HEIGHT:
                next_position.y = 50
                self.acc_position.y = 50
            elif next_position.y < 50:
                next_position.y = WORLD_HEIGHT - 50
                self.acc_position.y = WORLD_HEIGHT - 50

            if self.is_food_reachable(self.food_spawner.food_position):
                self.size += 1
                self.food_spawner.spawn_food(self)

            if self.size > 0:
                self.trail.append(prev_position)
                self.trail = self.trail[-self.size:]

            self.transform.position = next_position

    def is_food_reachable(self, food_position: pygame.Vector2):
        if self.transform.position.x == food_position.x and self.transform.position.y == food_position.y:
            return True

        return False

    def handle_render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

        for pos in self.trail:
            pygame.draw.rect(surface, self.color, pygame.Rect(pos.x - 25, pos.y - 25, 50, 50))

    def set_speed(self, value: float) -> None:
        if value < 0:
            raise ValueError('Speed cannot be negative.')

        self.speed = value

    def __str__(self) -> str:
        return f'Player(id={self.id})'
