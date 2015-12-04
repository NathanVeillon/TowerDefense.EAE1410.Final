#DisplayLevel.py
# 
# File Contributors
#     Nathan Veillon
#     Joshua Rosen

import pygame
from pygame.locals import *
from View.Levels.ImportLevels import *
from Library.Classes.Tiles.TileMap import *
from Library.Classes.Enemies.EnemyWave import *
from View.StartMenu import *
from Library.Classes.PlayerModel import *
from View.GameOverScreen import *

empty_wave={'num_enemies':0,'deploy_delay':1,'type':'BaseEnemy','speed':1,'health':25,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'}

class DisplayLevel:

    def __init__(self,level_file_name):
        self.player = PlayerModel(500, 5) #Player starts with 500 dollars and 5 lives

        self.level_name = level_file_name
        self.level = eval(level_file_name)()
        self.letter_map = self.level.letter_map
        self.tile_map = TileMap(self.letter_map)

        self.enemy_waves = self.level.enemy_waves
        self.current_enemy_wave_number = 0
        self.total_enemy_waves = len(self.enemy_waves)
        self.current_enemy_wave = EnemyWave(self.tile_map,empty_wave)

        self.display_level = self
        self.level_menu = LevelMenu(self.display_level)
        self.tower_list = [] #List of all towers currently on the screen

        self.level_finished = False
        self.game_over = None #Game over screen

    def get_next_wave(self):
        if(self.current_enemy_wave_number == self.total_enemy_waves):
            self.check_level_finished()
            return
        if(self.current_enemy_wave.dead_enemies == self.current_enemy_wave.num_enemies):
            self.current_enemy_wave = EnemyWave(self.tile_map, self.enemy_waves[self.current_enemy_wave_number])
            self.current_enemy_wave_number += 1
            self.update_tower_enemies()

    def update_tower_enemies(self):
        for tower in self.tower_list:
            tower.get_new_wave(self.current_enemy_wave.enemy_list)

    def display_towers(self):
        for tower in self.tower_list:
            tower.display_tower()

    def display_tile_map(self):
        self.tile_map.display_tile_map()

    def display_level_menu(self):
        self.level_menu.display_start_menu()

    def display_enemies(self):
        self.current_enemy_wave.tick()

    def check_collide(self):
        for tower in self.tower_list:
            for e in self.current_enemy_wave:
                    for b in tower.bullet_list:
                        if (pygame.sprite.collide_rect(e, b)):
                            e.damage_enemy(tower.bullet_damage)
                            tower.bullet_list.remove(b)

    def check_level_finished(self):
        if(self.current_enemy_wave.dead_enemies == self.current_enemy_wave.num_enemies):
            self.level_finished = True

    def update(self):
        self.check_collide()

        #Update live counter by subtracting each enemy that reached the end
        self.player.lives -= self.current_enemy_wave.reached_end
        self.current_enemy_wave.reached_end = 0
        if (self.player.lives < 1):
            if (isinstance(self.game_over, GameOverScreen)):
                self.game_over.display_self()
                if (self.game_over.timer > 450):
                    #Exit game
                    #In the future, we should definitely make a method for proper quitting
                    pygame.quit()
                    sys.exit()
            else:
                self.game_over = GameOverScreen()

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
                    clickedObj = self.level_menu.clicked()
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
                if (selected_tile.tower == None):
                    self.player.wallet -= tower.cost
                selected_tile.place_tower(tower) #Assign the tower variable of the selected_tile
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

