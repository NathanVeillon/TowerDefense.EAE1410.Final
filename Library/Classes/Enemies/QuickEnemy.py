#QuickEnemy.py
# 
# File Contributors
#     Nathan Veillon

from .BaseEnemy import *

class QuickEnemy(BaseEnemy):

    def __init__(self, tile_map, speed=None, health=None, size=None, image_location=None):
        self.speed = 5
        self.health = 5
        self.size = (15,15)
        self.image_location = 'Library\Assets\Enemies\BaseEnemy.png'
        BaseEnemy.__init__(self, tile_map, self.speed, self.health, self.size, self.image_location)
