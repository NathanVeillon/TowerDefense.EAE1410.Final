#DisplayLevel.py
# 
# File Contributors
#     Nathan Veillon
#     Joshua Rosen

import pygame
from pygame.locals import *
from View.Levels.ImportLevels import *
from Library.Classes.Tiles.TileMap import *
from View.StartMenu import *

class DisplayLevel:

    def __init__(self,level_file_name):
        self.level_name = level_file_name
        self.level = eval(level_file_name)()
        self.letter_map = self.level.letter_map
        self.tile_map = TileMap(self.letter_map)

        self.level_menu = LevelMenu()
        self.tower_list = [] #List of all towers currently on the screen

    def display_towers(self):
        for tower in self.tower_list:
            tower.display_tower()

    def display_tile_map(self):
        self.tile_map.display_tile_map()

    def display_level_menu(self):
        self.level_menu.display_start_menu()

    def window_clicked(self):
        for event in pygame.event.get(MOUSEBUTTONUP):
            mouse_pos = pygame.mouse.get_pos()

            #If mouse_pos is within the tile map
            if ((mouse_pos[0] > 0 and mouse_pos[0] < self.tile_map.map_size) and (mouse_pos[1] > 0 and mouse_pos[1] < self.tile_map.map_size)): #if mouse is within the tile_map bounds
                self.tile_map_click(mouse_pos)

            #If mouse pos is within the level menu
            elif ((mouse_pos[0] > self.tile_map.map_size and mouse_pos[0] < self.tile_map.window.get_width()) and (mouse_pos[1] > 0 and mouse_pos[1] < self.tile_map.window.get_height())):

                if not (self.is_tower_being_placed()): #Only spawn a new tower if currently a tower is NOT being placed
                    #The level_menu.clicked method returns none if player did not click on a button (e.g. whitespace)
                    #This method is also passed the tile_size, so it can adjust the size of the tower according to the tile
                    newTower = self.level_menu.clicked(mouse_pos, self.tile_map.tile_size)
                else:
                    newTower = None

                if (isinstance(newTower, BaseTower)):
                    self.tower_list.append(newTower)
                else: #Player clicked on level menu whitespace and NOT button
                      #So if they are in the process of placing a tower, remove that tower
                    for tower in self.tower_list:
                        if tower.placed == False:
                            self.tower_list.remove(tower)

    #Player clicked on tile map
    def tile_map_click(self, mouse_pos):
        selected_tile = self.tile_map.clicked(mouse_pos) #Gets the tile that has been clicked on

        for tower in self.tower_list:
            if tower.placed == False: #If a tower has not been placed yet
                selected_tile.place_tower(tower) #Assign the tower attribute of the selected_tile
                break

    #Returns true if the player is in the process of placing a tower
    def is_tower_being_placed(self):
        for tower in self.tower_list:
            if (tower.placed == False):
                return True

