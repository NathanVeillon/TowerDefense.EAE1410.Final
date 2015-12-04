#Path.py
# 
# File Contributors
#     Nathan Veillon
#

import random
from .BaseTile import *

class Path(BaseTile):

    directions = ['U','R','D','L']

    def __init__(self,tile_size,current_direction,previous_direction=None,type='Path'):
        self.current_direction = current_direction

        # if no previous direction is specified the previous direction defaults to the current direction
        if(previous_direction):
            self.previous_direction = previous_direction
        else:
            self.previous_direction = current_direction
        self.type = type

        # Have to decide what image to use, and is purely visual
        image_location = self.select_correct_image()
        self.orientation = self.find_orientation()

        BaseTile.__init__(self,tile_size,image_location,self.orientation)
        self.type = type
        self.can_place_tower = False

    def find_orientation(self):
        orientation = 0
        # checks that it isn't rotating a corner piece
        if(self.previous_direction == self.current_direction):
            if(self.current_direction == 'R'):
                orientation = 0
            elif(self.current_direction == 'U'):
                orientation = 90
            elif(self.current_direction == 'L'):
                orientation = 180
            elif(self.current_direction == 'D'):
                orientation = 270
        return orientation

    def select_correct_image(self):
        if(self.type == 'Start'):
            return 'Library/Assets/Tiles/StartPath.png'
        elif(self.type == 'End'):
            return 'Library/Assets/Tiles/EndPath.png'
        else:
            return self.select_path_image()



    def select_path_image(self):
        if(self.previous_direction != self.current_direction):
            return 'Library/Assets/Tiles/Corner'+self.previous_direction+self.current_direction+'.png'
        path_type = random.randint(1,3)
        return 'Library/Assets/Tiles/Path'+str(path_type)+'.png'


