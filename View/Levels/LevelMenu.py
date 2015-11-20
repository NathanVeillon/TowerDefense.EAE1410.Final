# LevelMenu.py
#
# File Contributors
#     Joshua Rosen
#
# Purpose:
# Panel on the right hand side of the window for containing
#   the buttons for the player to purchase and place towers.

import pygame, sys
from pygame.locals import *
from View.SimpleButton import *
from Library.Classes.Towers.BaseTower import *

class LevelMenu():

    def __init__(self):
        self.window = pygame.display.get_surface()

        #The size of the tile map (the tile map is a square - this value is both the width and the height)
        self.map_size = self.window.get_height()

        #The menu_base is the panel surface that contains all of the tower buttons
        self.menu_base = pygame.Surface((self.window.get_width() - self.map_size, self.window.get_height()), flags=SRCALPHA, depth=32)

        self.base_tower_button = SimpleButton(50, 150, (100, 120, 90), (0, 0, 0), "Base Tower", 25, self.menu_base, (10, 20))

    def display_start_menu(self):
        self.base_tower_button.display_button()
        self.window.blit(self.menu_base,(self.map_size,0))

    def clicked(self, mouse_pos, tile_size, tile_map_size):
        #Subtract the width of the tile_map (map_size) from mouse_pos to get an x-coordinate relative to the start menu panel
        level_menu_mouse_pos = (mouse_pos[0] - self.map_size, mouse_pos[1])

        #Player clicked on the spawn tower button
        if (self.base_tower_button.clicked(level_menu_mouse_pos)):
            newTower = BaseTower(tile_size - 10, mouse_pos, 30, [], tile_map_size)
            return newTower #Return the newly created tower
        else:
            return None #Otherwise return nothing