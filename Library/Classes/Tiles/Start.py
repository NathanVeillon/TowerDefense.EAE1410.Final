#Start.py
# 
# File Contributors
#     Nathan Veillon
#

from .Path import *

class Start(Path):

    def __init__(self,tile_size):
        Path.__init__(self,tile_size,'Library/Assets/Tiles/Start.png')
        self.type = 'Start'
        self.can_place_tower = False



