#QuickEnemy.py
# 
# File Contributors
#     Nathan Veillon

from .BaseEnemy import *

class QuickEnemy(BaseEnemy):



    def __init__(self, tile_map, speed=None, health=None, cash=None, size=None, image_location=None):
        self.speed = 5
        self.health = 5
        self.cash = 10
        self.size = (20,20)
        self.image_location = 'Library\Assets\Enemies\BaseEnemy.png'
        BaseEnemy.__init__(self, tile_map, self.speed, self.health, self.cash, self.size, self.image_location)

