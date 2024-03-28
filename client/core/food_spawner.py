import pygame
import random
from core.constants import WORLD_WIDTH, WORLD_HEIGHT, CELL_SIZE


class FoodSpawner:
    food_position: pygame.Vector2

    def spawn_food(self, player):
        ignored_cells = [player.transform.position] + player.trail

        while True:
            current_x = CELL_SIZE * round(random.randint(CELL_SIZE, WORLD_WIDTH - CELL_SIZE) / CELL_SIZE)
            current_y = CELL_SIZE * round(random.randint(CELL_SIZE, WORLD_HEIGHT - CELL_SIZE) / CELL_SIZE)

            for position in ignored_cells:
                if current_x == position.x and current_y == position.y:
                    continue
            
            break

        self.food_position = pygame.Vector2(current_x, current_y)