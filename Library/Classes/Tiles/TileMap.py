#TileMap.py
# 
# File Contributors
#     Nathan Veillon

import copy
import pygame
from pygame.locals import *
from  .BaseTitle import *
from  .Terrain import *
from  .Path import *
from  .Start import *
from  .End import *

class TileMap():

    def __init__(self,letter_map):
        self.window = pygame.display.get_surface()
        self.tile_size = (self.window.get_height()//len(letter_map))
        self.map_size = self.window.get_height()
        self.map_base = pygame.Surface((self.map_size, self.map_size), flags=SRCALPHA, depth=32)
        self.letter_map = letter_map
        self.tile_map = self.create_tiles()

    def create_tiles(self):
        tile_map = copy.deepcopy(self.letter_map)
        y = 0
        for column in self.letter_map:
            x=0
            for item in column:
                if(item == 'S' ):
                    current_tile = Start(self.tile_size)
                elif(item == 'E' ):
                    current_tile = End(self.tile_size)
                elif(item == 'P' ):
                    current_tile = Path(self.tile_size)
                else:
                    current_tile = Terrain(self.tile_size)
                tile_map[x][y] = current_tile
                x += 1
            y += 1
        return tile_map


    def display_tile_map(self):
        tile_y_coord = 0
        for column in self.tile_map:
            tile_x_coord = 0
            for tile in column:
                self.map_base.blit(tile.surface,(tile_y_coord,tile_x_coord))
                tile_x_coord += self.tile_size
            tile_y_coord += self.tile_size

        self.window.blit(self.map_base,(0,0))



