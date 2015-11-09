#DisplayLevel.py
# 
# File Contributors
#     Nathan Veillon
#

import pygame
from pygame.locals import *
from View.Levels.ImportLevels import *
from Library.Classes.Tiles.TileMap import *
from View.StartMenu import *

class DisplayLevel:

    def __init__(self,level_file_name):
        self.level_name = level_file_name
        self.level = eval(level_file_name)()
        self.letter_map = self.level.letter_map
        self.tile_map = TileMap(self.letter_map)

        self.start_menu = StartMenu()

    def display_tile_map(self):
        self.tile_map.display_tile_map()

    def window_clicked(self):
        for event in pygame.event.get(MOUSEBUTTONUP):
            mouse_pos = pygame.mouse.get_pos()
            if ((mouse_pos[0] > 0 and mouse_pos[0] < self.tile_map.map_size) and (mouse_pos[1] > 0 and mouse_pos[1] < self.tile_map.map_size)): #if mouse is within the tile_map bounds
                self.tile_map.clicked(mouse_pos)
            elif ((mouse_pos[0] > self.tile_map.map_size and mouse_pos[0] < self.tile_map.window.get_width()) and (mouse_pos[1] > 0 and mouse_pos[1] < self.tile_map.window.get_height())):
                self.start_menu.clicked(mouse_pos)




