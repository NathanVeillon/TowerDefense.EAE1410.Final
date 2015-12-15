# LevelMenu.py
#
# File Contributors
#     Joshua Rosen
#     Nathan Veillon
#
# Purpose:
# Panel on the right hand side of the window for containing
#   the buttons for the player to purchase and place towers.

import pygame, sys
from pygame.locals import *
from Library.Classes.Display.DisplayLevel import *
from View.SimpleButton import *
from Library.Classes.Towers.BaseTower import *

class LevelMenu():

    def __init__(self, display_level):
        self.display_level = display_level #DisplayLevel passes itself by self-reference

        self.window = pygame.display.get_surface()

        #The size of the tile map (the tile map is a square - this value is both the width and the height)
        self.map_size = self.window.get_height()

        #The menu_base is the panel surface that contains all of the tower buttons
        self.menu_base = pygame.Surface((self.window.get_width() - self.map_size, self.window.get_height()), flags=SRCALPHA, depth=32)

        self.base_tower_button = SimpleButton((150, 50), 'Library/Assets/Buttons/BaseTower_Button.png', self.menu_base, (10, 80))
        self.next_wave_button = SimpleButton((150, 50), 'Library/Assets/Buttons/NextWave_Button.png', self.menu_base, (10, 150))
        self.logo = pygame.image.load('Library/Assets/Logo.png')
        self.menu_font = pygame.font.SysFont("Lucida Console", 80)

    def display_start_menu(self):
        self.menu_base.fill((255,215,168))

        self.base_tower_button.display_button(BaseTower.cost)
        self.next_wave_button.display_button()
        self.menu_base.blit(self.logo,(15, 400))
        self.draw_text("Lives: " + str(self.display_level.player.lives), (15, 350)) #Lives display
        self.draw_text("Money: " + str(self.display_level.player.wallet), (15, 15)) #Wallet display
        self.display_wave_info()

        self.window.blit(self.menu_base,(self.map_size,0))

    def draw_text(self, text, coordinates):
        text_surface = self.menu_font.render(text, True, (76, 50, 25), None)
        text_surface = pygame.transform.scale(text_surface, (145, 45))
        self.menu_base.blit(text_surface, coordinates)

    def display_wave_info(self):
        current_wave_number = str(self.display_level.current_enemy_wave_number)
        total_wave_number = str(self.display_level.total_enemy_waves)

        self.draw_text('Wave '+current_wave_number+' out of '+total_wave_number, (15, 200))

        current_wave = self.display_level.current_enemy_wave
        enemies_remaining = current_wave.num_enemies-current_wave.dead_enemies
        if(enemies_remaining == 1):
            string = ' enemy'
        else:
            string = ' enemies'
        enemies_remaining = str(enemies_remaining)+string

        self.draw_text(enemies_remaining+' remaining', (15, 250))


    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        tile_size = self.display_level.tile_map.tile_size
        tile_map_size = self.display_level.tile_map.map_size

        #Subtract the width of the tile_map (map_size) from mouse_pos to get an x-coordinate relative to the start menu panel
        level_menu_mouse_pos = (mouse_pos[0] - self.map_size, mouse_pos[1])

        #Player clicked on the spawn tower button
        if (self.base_tower_button.clicked(level_menu_mouse_pos)):
            newTower = BaseTower(tile_size - 10, mouse_pos, 150, self.display_level.current_enemy_wave, tile_map_size)

            return newTower #Return the newly created tower
        elif(self.next_wave_button.clicked(level_menu_mouse_pos)):
            self.display_level.get_next_wave()
        else:
            return None #Otherwise return nothing