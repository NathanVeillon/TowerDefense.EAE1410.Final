#BaseTitle.py
# 
# File Contributors
#     Nathan Veillon
#     Joshua Rosen

import pygame
from pygame.locals import *
from Library.Classes.Towers.BaseTower import BaseTower

class BaseTile:

    def __init__(self,tile_size,image_location='Library/Assets/Tiles/BaseTile.png',orientation=0):
        self.tile_size = tile_size

        self.dimension = (tile_size,tile_size)
        self.surface = pygame.image.load(image_location).convert()#We load a different image based on what is passed
        # through the parameters
        if(orientation):
            self.surface = pygame.transform.rotate(self.surface, orientation)
        self.surface = pygame.transform.scale(self.surface,self.dimension)
        self.type = 'BaseTile'
        self.can_place_tower = False

        self.tower = None

        self.position = (0,0) #Position of the tile on the main window - is assigned in TileMap

    def is_path(self):
        return isinstance(self,'Path')

    #Place the passed tower onto the tile, assign the tile's tower attribute
    def place_tower(self, tower):
        if not (isinstance(self.tower, BaseTower)) and (self.type == "Terrain"):
            self.tower = tower
            tower.placed = True

            tower.tile_surface = self.surface
            tower.position = self.position



