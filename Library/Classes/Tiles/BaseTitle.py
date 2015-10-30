#BaseTitle.py
# 
# File Contributors
#     Nathan Veillon
#

import pygame
from pygame.locals import *

class BaseTile:

    def __init__(self,tile_size,image_location='Library/Assets/Tiles/BaseTile.png'):
        self.dimension = (tile_size,tile_size)
        self.surface = pygame.image.load(image_location).convert()
        self.surface = pygame.transform.scale(self.surface,self.dimension)
        self.type = 'BaseTile'
        self.can_place_tower = False

    def is_path(self):
        return isinstance(self,'Path')


