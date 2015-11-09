#DisplayLevel.py
# 
# File Contributors
#     Nathan Veillon
#     Josh Rosen
#

from View.Levels.ImportLevels import *
from Library.Classes.Tiles.TileMap import *

class DisplayLevel:

    def __init__(self,level_file_name):
        self.level_name = level_file_name
        self.level = eval(level_file_name)()
        self.letter_map = self.level.letter_map
        self.tile_map = TileMap(self.letter_map)
        # self.level_menu = LevelMenu()

    def display_tile_map(self):
        self.tile_map.display_tile_map()

    def window_clicked(self):
        for event in pygame.event.get(MOUSEBUTTONUP):
            mouse_position = event.pos
            if self.mouse_position_in_tile_map(mouse_position):
                self.tile_map.clicked(mouse_position)
            elif self.mouse_position_in_level_menu(mouse_position):
                self.level_menu.clicked(mouse_position)

    def mouse_position_in_tile_map(self,mouse_position):
        x,y = mouse_position
        if(x <= self.tile_map.map_size):
            return True
        return False

    def mouse_position_in_level_menu(self,mouse_position):
        x,y = mouse_position
        if(x >= self.tile_map.map_size):
            return True
        return False




