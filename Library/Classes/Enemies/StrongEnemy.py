#StrongEnemy.py
# 
# File Contributors
#     Nathan Veillon

from .BaseEnemy import *

class StrongEnemy(BaseEnemy):

    def __init__(self, tile_map, speed=None, health=None, cash=None, size=None, image_location=None):
        self.speed = 1
        self.health = 50
        self.cash = 15
        self.size = (40,40)
        self.image_location = 'Library\Assets\Enemies\BaseEnemy.png'
        BaseEnemy.__init__(self, tile_map, self.speed, self.health, self.cash, self.size, self.image_location)
