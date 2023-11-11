import pygame
from game import Game
from core.player import Player
from core.camera import CameraGroup
from core.world_object import WorldObject
from core.events import EventHandler

# TODO:
# * Movement interpolation (https://www.pygame.org/wiki/Interpolator): 
#   * Camera
#   * Character
# * Use world coordinates instead of pixels.
# * Collisions between player and static world objects.

Game().run()
