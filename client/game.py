import pygame
from core.events import EventHandler
from core.camera import CameraGroup
from core.world_object import WorldObject
from core.player import Player
from core.math.interpolator import Interpolator


class GameId:
    pass


class Game(GameId):
    is_running: bool
    delta_time: float
    clock: pygame.time.Clock
    surface: pygame.Surface
    target_fps: int
    camera: CameraGroup
    resolution = (1280, 720)

    def __init__(self, target_fps: int = 60):
        pygame.init()
        EventHandler.add_listener(GameId, self)
        self.delta_time = 0.0
        self.is_running = False
        self.target_fps = target_fps
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.resolution, pygame.RESIZABLE)

    def run(self):
        font = pygame.freetype.SysFont('Cascadia Mono', 16)

        self.camera = CameraGroup()
        tree = WorldObject(scale=0.4, image_path='assets/tree.png', group=self.camera)
        tree.transform.set_position(pygame.Vector2(0, 0))

        player = Player(speed=440.0, group=self.camera)
        player.transform.set_position(pygame.Vector2(self.surface.get_width() / 2 - 20, self.surface.get_height() / 2 - 20))
        self.camera.set_target(pygame.Vector2(self.resolution[0] // 2, self.resolution[1] // 2))
        self.is_running = True

        interpolator = Interpolator((0, 0), self.resolution, 5, self.target_fps, shape=1.2)

        while self.is_running:
            for event in pygame.event.get():
                EventHandler.notify(event)

            self.surface.fill((42, 42, 42))
            text_surface_one, _ = font.render(f'Player: {player.transform.position}', (255, 255, 255))
            text_surface_two, _ = font.render(f'Camera offset: {self.camera.offset}', (255, 255, 255))
            self.surface.blit(text_surface_one, (40, 40))
            self.surface.blit(text_surface_two, (40, 80))

            player.handle_input()
            player.handle_update(self.delta_time)

            # pygame.draw.circle(self.surface, pygame.Color(255, 128, 64), interpolator.pos, 25.0)
            # interpolator.next()

            self.camera.update()
            self.camera.custom_draw()

            pygame.display.update()
            self.delta_time = self.clock.tick(self.target_fps) / 1000

    @EventHandler.register(GameId, pygame.VIDEORESIZE)
    def on_resize(self, _event):
        self.camera.set_half_size(self.surface.get_size()[0] // 2, self.surface.get_size()[1] // 2)

    @EventHandler.register(GameId, pygame.QUIT)
    def on_exit(self, _event):
        self.is_running = False
        pygame.quit()
        quit(0)
