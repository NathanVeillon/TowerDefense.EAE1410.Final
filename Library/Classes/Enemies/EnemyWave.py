#EnemyWave.py
# 
# File Contributors
#     David Mirabile
#     Nathan Veillon
#     Joshua Rosen
#
# Purpose:
# Manage and construct waves of enemies.


from Library.Classes.Enemies.ImportEnemies import *


## implementation notice:
## This class is designed to manage enemies, and generate waves of enemies.
## This class should be used when dealing with enemies

class EnemyWave():

    ## The init requires requires all the information for the type of enemy it will be displaying
    ## as well as how many enemies it will display, and how often to launch a new enemy.
    ## speed must be an integer.

    def __init__(self, tile_map, enemy_wave_info):
        self.enemy_list = []
        self.tile_map = tile_map
        self.tile_size = self.tile_map.tile_size

        self.enemy_wave_info = enemy_wave_info

        self.enemy_type = self.parse_enemy_info('type')
        self.image_location = self.parse_enemy_info('image_location')
        self.speed = self.parse_enemy_info('speed')
        self.size = self.parse_enemy_info('size')
        self.health = self.parse_enemy_info('health')
        ##self.__newWave(numEnemies)
        self.num_enemies = enemy_wave_info['num_enemies']

        self.deploy_delay = enemy_wave_info['deploy_delay']
        self.count = 0
        self.deployed_enemies = 0
        self.dead_enemies = 0
        self.reached_end = 0 #Ticks to 1 if enemy reaches the end, then is subtracted from lives and set to 0 again

    #def __iter__(self):
    #    return self.enemy_list.__iter__()

    def parse_enemy_info(self, variable_name):
        if variable_name in self.enemy_wave_info:
            return self.enemy_wave_info[variable_name]
        else:
            return None

    ## passes the enemy list to a function that requests it
    def get_enemy_list(self):
        return self.enemy_list

    ### Obsolete
    ## generates a new wave of a specified number of enemies
    ## def __newWave(self):
    ##    
    ##     for i in range(numEnemies):
    ##         self.enemyList.append(newEnemy(self.TILEMAP.start_position, self.SURF, self.SPEED, self.SIZE, self.health, self.TILESIZE, self.IMAGE))

    ## checks an enemies status, and if it needs new information, updates the enemy

    def __check_enemy_status(self):
        
        for enemy in self.enemy_list:
            if(enemy.check_feed()):
                enemy_tile_position = enemy.get_tile_position()
                current_tile = self.tile_map.tile_map[enemy_tile_position[0]][enemy_tile_position[1]]
                if(current_tile.type == 'End'):
                    self.dead_enemies += 1
                    self.reached_end += 1
                    self.enemy_list.remove(enemy)
                    return
                if current_tile.current_direction == 'U':
                    speed = (0, -self.speed)
                elif current_tile.current_direction == 'D':
                    speed = (0, self.speed)
                elif current_tile.current_direction == 'L':
                    speed = (-self.speed, 0)
                else:
                    speed = (self.speed, 0)
                enemy.update_enemy(speed)

    ## kills enemies that have no health
    def __cull_enemies(self):
        for enemy in self.enemy_list:
            if enemy.health <= 0:
                self.dead_enemies += 1
                self.enemy_list.remove(enemy)

    def spawn_enemies(self):
        # this tries creating enemies based on the declared type and if it fails then defaults to creating a
        # BaseEnemy Type.

        #Note that is a parameter is None it will default to whatever is specified in BaseEnemy
        try:
            new_enemy = eval(self.enemy_type)(self.tile_map, self.speed, self.health, self.size, self.image_location)
        except:
            new_enemy = BaseEnemy(self.tile_map, self.speed, self.health, self.size, self.image_location)

        self.speed = new_enemy.speed #Sets the Wave Speed variable to the created enemy speed,
        # Note: if this changes as the waves spawns enemies weird things will happen
        self.enemy_list.append(new_enemy)
        self.deployed_enemies += 1


    ## one call to tick all enemies forward one more frame.
    ## no_display is a bool that prevents the enemies from being displayed
    def tick(self, no_display=False):
        self.__cull_enemies()

        if (no_display == False):
            self.count += 1
            if (self.count % self.deploy_delay == 0) and (self.deployed_enemies < self.num_enemies):
                self.spawn_enemies()

            for enemy in self.enemy_list:
                enemy.display_enemy()

        self.__check_enemy_status()
