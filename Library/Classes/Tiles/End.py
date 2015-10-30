#End.py
# 
# File Contributors
#     Nathan Veillon
#

from .Path import *

class End(Path):

    def __init__(self,tile_size):
        Path.__init__(self,tile_size,'Library/Assets/Tiles/End.png')
        self.type = 'End'
        self.can_place_tower = False



