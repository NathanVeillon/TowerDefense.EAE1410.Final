#Start.py
# 
# File Contributors
#     Nathan Veillon
#

from .Path import *

class Start(Path):

    def __init__(self,tile_size,current_direction,previous_direction):
        Path.__init__(self,tile_size,current_direction,previous_direction,'Library/Assets/Tiles/Start.png')
        self.type = 'Start'
        self.can_place_tower = False



