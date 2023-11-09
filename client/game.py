import pygame
from core.events import EventHandler
from core.camera import CameraGroup
from core.world_object import WorldObject
from core.player import Player


class Game:
    is_running: bool
    delta_time: float
    clock: pygame.time.Clock
    surface: pygame.Surface
    target_fps: int

    def __init__(self, target_fps: int = 60):
        pygame.init()
        self.delta_time = 0.0
        self.is_running = False
        self.target_fps = target_fps
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

    def run(self):
        pygame.init()
        camera = CameraGroup()
        font = pygame.freetype.SysFont('Cascadia Mono', 16)

        tree = WorldObject(scale=0.4, image_path='assets/tree.png', group=camera)
        tree.transform.set_position(pygame.Vector2(0, 0))

        player = Player(speed=440.0, group=camera)
        player.transform.set_position(pygame.Vector2(self.surface.get_width() / 2 - 20, self.surface.get_height() / 2 - 20))
        camera.set_target(player.rect)
        self.is_running = True

        while self.is_running:
            for event in pygame.event.get():
                EventHandler.notify(event)
                #
                # match event.type:
                #     case pygame.VIDEORESIZE:
                #         camera_group.set_half_size(screen.get_size()[0] // 2, screen.get_size()[1] // 2)

            self.surface.fill((42, 42, 42))
            text_surface_one, _ = font.render(f'Player: {player.transform.position}', (255, 255, 255))
            text_surface_two, _ = font.render(f'Camera offset: {camera.offset}', (255, 255, 255))
            self.surface.blit(text_surface_one, (40, 40))
            self.surface.blit(text_surface_two, (40, 80))

            player.handle_input()
            player.handle_update(self.delta_time)

            camera.update()
            camera.custom_draw()

            pygame.display.update()
            self.delta_time = self.clock.tick(self.target_fps) / 1000

    @EventHandler.register(pygame.QUIT)
    def on_exit(self, event):
        print('Quitting...', event)
        # self.is_running = False
        pygame.quit()
        quit(0)
