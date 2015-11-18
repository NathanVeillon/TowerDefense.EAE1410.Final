#TileMap.py
# 
# File Contributors
#     Nathan Veillon
#     Josh Rosen

import copy
import pygame
from pygame.locals import *
from .BaseTile import *
from .Terrain import *
from .Path import *
from .Start import *
from .End import *

class TileMap():

    def __init__(self,letter_map):
        self.window = pygame.display.get_surface()
        self.tile_size = (self.window.get_height()//len(letter_map))
        self.map_size = self.window.get_height()
        self.map_base = pygame.Surface((self.map_size, self.map_size), flags=SRCALPHA, depth=32)
        self.letter_map = letter_map
        self.start_position = self.find_start()
        self.tile_map = self.create_tiles()

    def create_tiles(self):
        tile_map = self.create_path()
        y = 0
        for column in self.letter_map:
            x=0
            for item in column:
                if(isinstance(tile_map[x][y],BaseTile)):
                    x += 1
                    continue

                current_tile = Terrain(self.tile_size)
                tile_map[x][y] = current_tile
                x += 1
            y += 1
        return tile_map

    def create_path(self):
        tile_map = copy.deepcopy(self.letter_map)
        current_x_pos = self.start_position[0]
        current_y_pos = self.start_position[1]
        previous_tile_text = self.letter_map[current_y_pos][current_y_pos]

        tile_map[current_x_pos][current_y_pos] =  Start(self.tile_size,previous_tile_text[1],None)

        while True:
            previous_direction = previous_tile_text[1]

            if(previous_direction == 'U'):
                current_y_pos += -1
            elif(previous_direction == 'D'):
                current_y_pos += 1
            elif(previous_direction == 'R'):
                current_x_pos += 1
            elif(previous_direction == 'L'):
                current_x_pos += -1

            current_tile_text = self.letter_map[current_y_pos][current_x_pos]
            current_direction = current_tile_text[1]
            if(current_tile_text[0]=='E'):
                tile_map[current_x_pos][current_y_pos] = End(self.tile_size, current_direction, previous_direction)
                break

            tile_map[current_x_pos][current_y_pos] = Path(self.tile_size, current_direction, previous_direction)
            previous_tile_text = current_tile_text

        return tile_map

    def find_start(self):
        y = 0
        for column in self.letter_map:
            x=0
            for item in column:
                if(item[0] == 'S'):
                    return (x,y)
                x += 1
            y += 1

    def display_tile_map(self):
        tile_y_coord = 0
        for column in self.tile_map:
            tile_x_coord = 0
            for tile in column:
                self.map_base.blit(tile.surface,(tile_y_coord,tile_x_coord))
                tile_x_coord += self.tile_size
            tile_y_coord += self.tile_size

        self.window.blit(self.map_base,(0,0))

    #player has clicked somewhere within the tile map
    def clicked(self, mouse_pos):
        x_mouse_pos = mouse_pos[0]
        y_mouse_pos = mouse_pos[1]

        x_tile_pos = x_mouse_pos//self.tile_size
        y_tile_pos = y_mouse_pos//self.tile_size

        selected_tile = self.tile_map[x_tile_pos][y_tile_pos]
        return selected_tile #Return the tile that the player clicked on



