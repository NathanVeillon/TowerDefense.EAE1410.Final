#Path.py
# 
# File Contributors
#     Nathan Veillon
#

from .BaseTitle import *

class Path(BaseTile):

    def __init__(self,tile_size,current_direction,previous_direction=None,image_location='Library/Assets/Tiles/Path.png'):
        self.current_direction = current_direction
        if(previous_direction):
            self.previous_direction = previous_direction
        else:
            self.previous_direction = current_direction


        BaseTile.__init__(self,tile_size,image_location)
        self.orientation = self.find_orientation()
        self.surface = pygame.transform.rotate(self.surface,self.orientation)
        self.type = 'Path'
        self.can_place_tower = False

    def find_orientation(self):
        orientation = 45
        if(self.current_direction == 'U'):
            orientation = 0
        elif(self.current_direction == 'L'):
            orientation = 90
        elif(self.current_direction == 'D'):
            orientation = 180
        elif(self.current_direction == 'R'):
            orientation = 270
        return orientation

    def select_correct_image(self):
        if(self.previous_direction != self.current_direction):
            pass
        return




