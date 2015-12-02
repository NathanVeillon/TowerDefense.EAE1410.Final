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
from Library.Classes.PlayerModel import *

class DisplayLevel:

    def __init__(self,level_file_name):
        self.player = PlayerModel(500) #Player starts with 500 dollars

        self.level_name = level_file_name
        self.level = eval(level_file_name)()
        self.letter_map = self.level.letter_map
        self.tile_map = TileMap(self.letter_map)

        self.display_level = self
        self.level_menu = LevelMenu(self.display_level)

        self.tower_list = [] #List of all towers currently on the screen

    def display_towers(self):
        for tower in self.tower_list:
            tower.display_tower()

    def display_tile_map(self):
        self.tile_map.display_tile_map()

    def display_level_menu(self):
        self.level_menu.display_start_menu(self.player.wallet)

    def update(self):

        ##FOR TESTING:
        #Circles to emulate enemies on the board - solely for visual testing purposes
        #If the circles are within the towers' attack_radius, then the towers will shoot at them
        pygame.draw.circle(pygame.display.get_surface(), (145,255,255), (186,245), 5)
        pygame.draw.circle(pygame.display.get_surface(), (145,255,255), (184, 27), 5)
        #---------------------------------------------

        #Tower shooting loop
        for tower in self.tower_list:
            if tower.placed == True:
                tower.attack_enemy()

        for event in pygame.event.get(MOUSEBUTTONUP):
            mouse_pos = pygame.mouse.get_pos()

            #If mouse position is within the tile map
            if ((mouse_pos[0] > 0 and mouse_pos[0] < self.tile_map.map_size)):
                self.tile_map_click(mouse_pos)

            #If mouse pos is within the level menu
            elif ((mouse_pos[0] > self.tile_map.map_size and mouse_pos[0] < self.tile_map.window.get_width())):
                if not (self.is_tower_being_placed()):
                    #The level_menu.clicked method returns none if player did not click on a button (e.g. whitespace)
                    clickedObj = self.level_menu.clicked(mouse_pos)
                else:
                    clickedObj = None

                #If the player clicked on the BaseTower button AND can afford a BaseTower
                if (isinstance(clickedObj, BaseTower) and self.player.wallet >= clickedObj.cost):
                    self.tower_list.append(clickedObj)
                else: #Player clicked on level menu whitespace and NOT button
                    self.stop_tower_placement()

    #Player clicked on tile map
    def tile_map_click(self, mouse_pos):
        selected_tile = self.tile_map.clicked(mouse_pos) #Gets the tile that has been clicked on

        if (selected_tile.type == "Path"):
            self.stop_tower_placement()
            return None

        for tower in self.tower_list:
            if (tower.placed == False): #If a tower has not been placed yet
                selected_tile.place_tower(tower) #Assign the tower variable of the selected_tile
                self.player.wallet -= tower.cost
                break

    #Returns true if the player is in the process of placing a tower
    def is_tower_being_placed(self):
        for tower in self.tower_list:
            if (tower.placed == False):
                return True

    #If player is in the process of placing a tower, and decides against it, delete that tower
    def stop_tower_placement(self):
        for tower in self.tower_list:
            if tower.placed == False:
                self.tower_list.remove(tower)

