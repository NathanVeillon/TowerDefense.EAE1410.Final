#DisplayWindow.py
# 
# File Contributors
#     Nathan Veillon
#     Joshua Rosen

import time
import sys
import pygame
from pygame.locals import *
from .DisplayLevel import *

class DisplayWindow:

    frame_rate = 60

    def __init__(self,screen_size=None,window_title='Game'):
        pygame.init()
        self.clock = pygame.time.Clock()

        if(screen_size == None): screen_size = (720,540)

        self.window = pygame.display.set_mode(screen_size, 0, 32)
        pygame.display.set_caption(window_title)

        self.level = None

    def display_window(self):

        while True:
            for event in pygame.event.get(QUIT):
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if(int(1000*time.clock())%1000 > 983):
                pygame.event.clear()


            self.window.fill((255,255,255))

            self.decide_level_to_display()

            self.level.update()

            self.clock.tick(self.frame_rate)
            pygame.display.update()

    def decide_level_to_display(self):
        if(not isinstance(self.level, DisplayLevel)):
            self.level = DisplayLevel("Level01")

        self.level.display_tile_map()
        self.level.display_level_menu()
        self.level.display_towers()




