import pygame
import random
from client.core import Player

pygame.init()
delta_time = 0
is_running = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

player = Player(color=(105, 245, 135), size=35, speed=440.0)
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
            case pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.set_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    screen.fill((42, 42, 42))
    player.draw(screen)

    keys = pygame.key.get_pressed()
    direction = pygame.Vector2(0, 0)

    if keys[pygame.K_w]:
        direction.y = -1
    if keys[pygame.K_s]:
        direction.y = 1
    if keys[pygame.K_a]:
        direction.x = -1
    if keys[pygame.K_d]:
        direction.x = 1

    player.transform.set_direction(direction)
    player.move(delta_time)
    pygame.display.update()
    delta_time = clock.tick(144) / 1000

pygame.quit()
