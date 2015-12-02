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

class enemyWave():

    ## The init requires requires all the information for the type of enemy it will be displaying
    ## as well as how many enemies it will display, and how often to launch a new enemy.
    ## speed must be an integer.
    def __init__(self, tileMap, surf, speed, size, health, numEnemies, deployDelay, enemyImage):
        self.enemyList = []
        self.TILEMAP = tileMap
        self.TILESIZE = self.TILEMAP.tile_size
        self.IMAGE = enemyImage
        self.SURF = surf
        self.SPEED = speed
        self.SIZE = size
        self.HEALTH = health
        ##self.__newWave(numEnemies)
        self.NUM_ENEMIES = numEnemies

        self.DEPLOYDELAY = deployDelay
        self.count = 0
        self.deployed_enemies = 0

    ## passes the enemy list to a function that requests it
    def getEnemyList(self):
        return self.enemyList

    ### Obsolete
    ## generates a new wave of a specified number of enemies
    ## def __newWave(self):
    ##    
    ##     for i in range(numEnemies):
    ##         self.enemyList.append(newEnemy(self.TILEMAP.start_position, self.SURF, self.SPEED, self.SIZE, self.health, self.TILESIZE, self.IMAGE))

    ## checks an enemies status, and if it needs new information, updates the enemy
    def __checkEnemyStatus(self):
        
        for enemy in range(len(self.enemyList)):
            if(self.enemyList[enemy].checkFeed()):
                tempPos = enemyList[enemy].getPosition()
                if self.TILEMAP.tile_map[tempPos[0]][tempPos[1]].current_direction == 'U':
                    speed = (0, -self.SPEED)
                elif self.TILEMAP.tile_map[tempPos[0]][tempPos[1]].current_direction == 'D':
                    speed = (0, self.SPEED)
                elif self.TILEMAP.tile_map[tempPos[0]][tempPos[1]].current_direction == 'L':
                    speed = (-self.SPEED, 0)
                else:
                    speed = (self.SPEED, 0)
                self.enemyList[enemy].updateEnemy(speed)

    ## kills enemies that have no health
    def __cullEnemies(self):
        for enemy in self.enemyList:
            if self.enemyList[enemy].health <= 0:
                del self.enemyList[enemy]


    ## one call to tick all enemies forward one more frame.
    def tick(self, enemiesToStart):
        self.count += 1
        if (self.count % self.DEPLOYDELAY == 0) and (self.deployed_enemies <= self.NUM_ENEMIES):
            self.enemyList.append(newEnemy(self.TILEMAP.start_position, self.SURF, self.SPEED, self.SIZE, self.health, self.TILESIZE, self.IMAGE))
            self.deployed_enemies += 1
        
        self.__cullEnemies()
        for enemy in range(len(self.enemyList)):
            self.enemyList[enemy].disp_enemy()
        self.__checkEnemyStatus()







