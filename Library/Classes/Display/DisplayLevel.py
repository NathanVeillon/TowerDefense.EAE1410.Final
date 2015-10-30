#DisplayLevel.py
# 
# File Contributors
#     Nathan Veillon
#

from View.Levels.ImportLevels import *
from Library.Classes.Tiles.TileMap import *

class DisplayLevel:

    def __init__(self,level_file_name):
        self.level_name = level_file_name
        self.level = eval(level_file_name)()
        self.letter_map = self.level.letter_map
        self.tile_map = TileMap(self.letter_map)

    def display_tile_map(self):
        self.tile_map.display_tile_map()




