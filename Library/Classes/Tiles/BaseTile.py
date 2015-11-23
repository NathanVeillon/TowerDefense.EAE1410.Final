#BaseTitle.py
# 
# File Contributors
#     Nathan Veillon
#     Joshua Rosen

import pygame
from Library.Classes.Towers.BaseTower import *
from pygame.locals import *

class BaseTile:

    def __init__(self,tile_size,image_location='Library/Assets/Tiles/BaseTile.png'):
        self.tile_size = tile_size

        self.dimension = (tile_size,tile_size)
        self.surface = pygame.image.load(image_location).convert()
        self.surface = pygame.transform.scale(self.surface,self.dimension)
        self.type = 'BaseTile'
        self.can_place_tower = False

        self.tower = None

        self.position = (0,0) #Position of the tile on the main window - is assigned in TileMap
        self.middle_position = self.find_middle_position()

    def is_path(self):
        return isinstance(self,'Path')

    def set_position(self,new_position): #Function added to set position so we can also set the middle position
        self.position = new_position
        self.middle_position = self.find_middle_position()

    def find_middle_position(self):
        x = self.position[0] + (self.dimension[0]//2)
        y = self.position[1] + (self.dimension[1]//2)
        return (x,y)


    #Place the passed tower onto the tile, assign the tile's tower attribute
    def place_tower(self, tower):
        if not (isinstance(self.tower, BaseTower)) and (self.type == "Terrain"):
            self.tower = tower
            tower.placed = True

            tower.tile_surface = self.surface
            tower.position = self.position #HERE



