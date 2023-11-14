import pygame
import random
from core.constants import WORLD_WIDTH, WORLD_HEIGHT, CELL_SIZE


class FoodSpawner:
    food_position: pygame.Vector2

    def spawn_food(self):
        self.food_position = pygame.Vector2(
            CELL_SIZE * round(random.randint(CELL_SIZE, WORLD_WIDTH - CELL_SIZE) / 50),
            CELL_SIZE * round(random.randint(CELL_SIZE, WORLD_HEIGHT - CELL_SIZE) / 50)
        )

    def consume_food(self):
        self.spawn_food()
