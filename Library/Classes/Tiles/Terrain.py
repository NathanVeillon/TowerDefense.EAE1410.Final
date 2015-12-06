#Terrain.py
# 
# File Contributors
#     Nathan Veillon
#     Kathy Huang
#
import random
from .BaseTile import *

class Terrain(BaseTile):

    def __init__(self,tile_size):
        terrain_type = random.randint(1,5)
        BaseTile.__init__(self,tile_size,'Library/Assets/Tiles/Terrain'+str(terrain_type)+'.png')
        self.type = 'Terrain'
        self.Tower = None
        self.can_place_tower = True



