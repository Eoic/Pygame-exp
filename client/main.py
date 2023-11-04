import pygame
import random
from core.player import Player
from core.camera import CameraGroup

pygame.init()
delta_time = 0
is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
camera_group = CameraGroup()

player = Player(
    group=camera_group,
    color=(105, 245, 135),
    size=35,
    speed=440.0,
)

player.transform.set_position(
    pygame.Vector2(
        screen.get_width() / 2 - player.size / 2,
        screen.get_height() / 2 - player.size / 2
    )
)

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
