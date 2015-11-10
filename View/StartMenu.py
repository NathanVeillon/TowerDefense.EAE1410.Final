# StartMenu.py
# 
# File Contributors
#     
# 
# Purpose:
#
import pygame
from pygame.locals import *
class StartMenu():

    def __init__(self):
        self.window = pygame.display.get_surface()
        self.menu_base = pygame.Surface((self.window.get_width(), self.window.get_height()), flags=SRCALPHA, depth=32)

    #player clicked on the start menu
    def clicked(self, mouse_pos):
        return None 

