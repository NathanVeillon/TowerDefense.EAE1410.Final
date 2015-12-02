#EnemyWave.py
# 
# File Contributors
#       David Mirabile
# 
# Purpose:
# Manage and construct waves of enemies.


from Library.Classes.Enemies.BaseEnemy import *


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
        self.image_location = enemy_wave_info['image_location']
        self.speed = enemy_wave_info['speed']
        self.size = enemy_wave_info['size']
        self.health = enemy_wave_info['health']
        ##self.__newWave(numEnemies)
        self.num_enemies = enemy_wave_info['num_enemies']

        self.deploy_delay = enemy_wave_info['deploy_delay']
        self.count = 0
        self.deployed_enemies = 0
        self.dead_enemies = 0

    def __iter__(self):
        return self.enemy_list.__iter__()

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


    ## one call to tick all enemies forward one more frame.
    def tick(self):
        self.count += 1
        if (self.count % self.deploy_delay == 0) and (self.deployed_enemies < self.num_enemies):
            self.enemy_list.append(BaseEnemy(self.tile_map.start_position, self.image_location, self.speed, self.size, self.health, self.tile_size))
            self.deployed_enemies += 1
        
        self.__cull_enemies()
        for enemy in self.enemy_list:
            enemy.display_enemy()
        self.__check_enemy_status()








