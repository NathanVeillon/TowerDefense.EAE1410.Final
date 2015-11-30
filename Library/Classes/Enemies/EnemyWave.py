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

## This class is unfinished
class enemyWave():

    def __init__(self, tileMap, surf, speed, health, enemyImage):
        self.enemyList = []
        self.TILEMAP = tileMap
        self.TILESIZE = self.TILEMAP.tile_size
        self.IMAGE = enemyImage
        self.SURF = surf
        self.SPEED = speed
        self.health = health

    ## passes the enemy list to a function that requests it
    def getEnemyList(self):
        return enemyList

    ## generates a new wave of a specified number of enemies
    def newWave(self, numEnemies, speed, health, enemyImage):
        
        for i in range(numEnemies):
            enemyList.append(newEnemy(self.TILEMAP.start_position, self.SURF, self.SPEED, self.health, self.TILESIZE, self.IMAGE))

    ## checks an enemies status, and if it needs new information, updates the enemy
    ## NOT FINISHED NEEDS WORK
    ## NOT FINISHED NEEDS WORK
    ## NOT FINISHED NEEDS WORK
    def __checkEnemyStatus(self):
        
        for enemy in enemyList:
            if(enemyList[enemy].checkFeed()):
                enemyList[enemy].updateEnemy(speed)

    def tick(self, enemiesToStart):
        pass






