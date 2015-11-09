#Terrain.py
# 
# File Contributors
#     Nathan Veillon
#

from .BaseTitle import *

class Terrain(BaseTile):

    def __init__(self,tile_size):
        BaseTile.__init__(self,tile_size,'Library/Assets/Tiles/Terrain.png')
        self.type = 'Terrain'
        self.Tower = None
        self.can_place_tower = True



