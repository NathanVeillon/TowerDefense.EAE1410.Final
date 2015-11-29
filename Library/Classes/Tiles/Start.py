#Start.py
# 
# File Contributors
#     Nathan Veillon
#

from .Path import *

class Start(Path):

    def __init__(self,tile_size,current_direction,previous_direction):
        # As the start is a path subclass we initialize the path object.
        Path.__init__(self,tile_size,current_direction,previous_direction,'Start')
        self.type = 'Start'
        self.can_place_tower = False



