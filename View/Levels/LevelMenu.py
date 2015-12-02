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

    def __init__(self, display_level):
        #Change passed parameters to getting it from display_level
        self.display_level = display_level #DisplayLevel passes itself by self-reference

        self.window = pygame.display.get_surface()

        #The size of the tile map (the tile map is a square - this value is both the width and the height)
        self.map_size = self.window.get_height()

        #The menu_base is the panel surface that contains all of the tower buttons
        self.menu_base = pygame.Surface((self.window.get_width() - self.map_size, self.window.get_height()), flags=SRCALPHA, depth=32)

        self.base_tower_button = SimpleButton((150, 50), 'Library/Assets/Buttons/BaseTower_Button.png', self.menu_base, (10, 80))

    def display_start_menu(self):
        self.menu_base.fill((255,255,255))
        self.base_tower_button.display_button(BaseTower.cost)

        cash_font = pygame.font.SysFont("Cambria", 80)
        self.wallet_surf = cash_font.render("Money: " + str(self.display_level.player.wallet), True, (25, 60, 80), None)
        self.wallet_surf = pygame.transform.scale(self.wallet_surf, (110, 50))

        self.menu_base.blit(self.wallet_surf, (30, 15))
        self.window.blit(self.menu_base,(self.map_size,0))

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        tile_size = self.display_level.tile_map.tile_size
        tile_map_size = self.display_level.tile_map.map_size

        #Subtract the width of the tile_map (map_size) from mouse_pos to get an x-coordinate relative to the start menu panel
        level_menu_mouse_pos = (mouse_pos[0] - self.map_size, mouse_pos[1])

        #Player clicked on the spawn tower button
        if (self.base_tower_button.clicked(level_menu_mouse_pos)):

            #FOR TESTING:
            #I pass the enemy list as a list of points simply for the purpose of demonstrating tower shooting
            #I also draw these points on the window, for the purpose of demonstrating, in DisplayLevel
            newTower = BaseTower(tile_size - 10, mouse_pos, 150, [(184, 27), (186, 245)], tile_map_size)

            return newTower #Return the newly created tower
        else:
            return None #Otherwise return nothing