import pygame
from core.events import EventHandler
from core.player import Player
from core.constants import WORLD_WIDTH, WORLD_HEIGHT, CELL_SIZE
from core.food_spawner import FoodSpawner


# Examples
# Text:
#
# self.surface.fill((42, 42, 42))



class GameId:
    pass


class Game(GameId):
    is_running: bool
    delta_time: float
    clock: pygame.time.Clock
    surface: pygame.Surface
    target_fps: int
    resolution = (WORLD_WIDTH, WORLD_HEIGHT)
    border_width = 25

    def __init__(self, target_fps: int = 60):
        pygame.init()
        EventHandler.add_listener(GameId, self)
        self.delta_time = 0.0
        self.is_running = False
        self.target_fps = target_fps
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.resolution)

    def run(self):
        self.is_running = True
        food_spawner = FoodSpawner()
        food_spawner.spawn_food()
        player = Player(speed=420.0, size=50, color=pygame.Color(64, 255, 64), food_spawner=food_spawner)
        player.transform.set_position(pygame.Vector2(
            CELL_SIZE * round(self.surface.get_width() / 2 / CELL_SIZE),
            CELL_SIZE * round(self.surface.get_height() / 2 / CELL_SIZE)
        ))

        font = pygame.freetype.SysFont('Cascadia Mono', 16)

        while self.is_running:
            for event in pygame.event.get():
                EventHandler.notify(event)

            self.surface.fill((42, 42, 42))

            text_surface_one, _ = font.render(f'Player: {player.transform.position}', (255, 255, 255))
            self.surface.blit(text_surface_one, (40, 40))

            pygame.draw.rect(self.surface, (128, 100, 255), (0, 0, WORLD_WIDTH, WORLD_HEIGHT), self.border_width)

            if food_spawner.food_position is not None:
                pygame.draw.rect(self.surface, (255, 128, 128), (food_spawner.food_position.x - 25, food_spawner.food_position.y - 25, 50, 50))

            player.handle_input()
            player.handle_update(self.delta_time)
            player.handle_render(self.surface)

            pygame.display.update()
            self.delta_time = self.clock.tick(self.target_fps) / 1000

    @EventHandler.register(GameId, pygame.QUIT)
    def on_exit(self, _event):
        self.is_running = False
        pygame.quit()
        quit(0)
