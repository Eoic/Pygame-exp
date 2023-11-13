import pygame
from core.events import EventHandler
from core.player import Player


# Examples
# Text:
# font = pygame.freetype.SysFont('Cascadia Mono', 16)
# self.surface.fill((42, 42, 42))
# text_surface_one, _ = font.render(f'Player: {player.transform.position}', (255, 255, 255))
# self.surface.blit(text_surface_one, (40, 40))


class GameId:
    pass


class Game(GameId):
    is_running: bool
    delta_time: float
    clock: pygame.time.Clock
    surface: pygame.Surface
    target_fps: int
    resolution = (1920, 1080)

    def __init__(self, target_fps: int = 60):
        pygame.init()
        EventHandler.add_listener(GameId, self)
        self.delta_time = 0.0
        self.is_running = False
        self.target_fps = target_fps
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)

    def run(self):
        self.is_running = True
        player = Player(speed=220.0, size=50, color=pygame.Color(64, 255, 64))
        player.transform.set_position(pygame.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2))

        while self.is_running:
            for event in pygame.event.get():
                EventHandler.notify(event)

            self.surface.fill((42, 42, 42))
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
