import pygame
from core.player import Player
from core.camera import CameraGroup
from core.world_object import WorldObject

pygame.init()
delta_time = 0
is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
camera_group = CameraGroup()

tree = WorldObject(
    image_path='assets/tree.png',
    scale=0.4,
    group=camera_group,
    position=pygame.Vector2(screen.get_width() / 2 - 200, screen.get_height() / 2)
)

player = Player(
    group=camera_group,
    speed=440.0,
    position=pygame.Vector2(
        screen.get_width() / 2 - 20,
        screen.get_height() / 2 - 20
    )
)

camera_group.set_target(player.rect)

while is_running:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                is_running = False

    screen.fill((42, 42, 42))

    player.handle_input()
    player.handle_update(delta_time)

    camera_group.update()
    camera_group.custom_draw()

    pygame.display.update()
    delta_time = clock.tick(144) / 1000

pygame.quit()
