import pygame
from core.player import Player
from core.camera import CameraGroup
from core.world_object import WorldObject

# TODO:
# * Movement interpolation (https://www.pygame.org/wiki/Interpolator): 
#   * Camera
#   * Character
# * Collisions

pygame.init()
delta_time = 0
is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
camera_group = CameraGroup()

tree = WorldObject(
    scale=0.4,
    image_path='assets/tree.png',
    group=camera_group,
)

tree.transform.set_position(
    pygame.Vector2(
        screen.get_width() / 2 - 200,
        screen.get_height() / 2,
    )
)

player = Player(
    speed=440.0,
    group=camera_group,
)

player.transform.set_position(
    pygame.Vector2(
        screen.get_width() / 2 - 20,
        screen.get_height() / 2 - 20,
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
