#Path.py
# 
# File Contributors
#     Nathan Veillon
#

from .BaseTitle import *

class Path(BaseTile):

    def __init__(self,tile_size,image_location='Library/Assets/Tiles/Path.png'):
        BaseTile.__init__(self,tile_size,image_location)
        self.type = 'Path'
        self.can_place_tower = False



