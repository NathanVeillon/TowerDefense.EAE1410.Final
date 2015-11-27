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

    def __init__(self, tileMap, tileSize, surf):
        self.enemyList = []
        self.TILEMAP = tileMap
        self.TILESIZE = tileSize
        self.SURF = surf

    ## passes the enemy list to a function that requests it
    def getEnemyList(self):
        return enemyList

    ## generates a new wave of a specified number of enemies
    def newWave(self, numEnemies, speed, health, enemyImage):
        
        for i in range(numEnemies):
            enemyList.append(newEnemy(self.TILEMAP.find_start(), self.SURF, speed, health, self.TILESIZE, enemyImage))

    ## checks an enemies status, and if it needs new information, updates the enemy
    ## NOT FINISHED NEEDS WORK
    ## NOT FINISHED NEEDS WORK
    ## NOT FINISHED NEEDS WORK
    def __checkEnemyStatus(self):
        
        for enemy in enemyList:
            if(enemyList[enemy].checkFeed()):
                enemyList[enemy].updateEnemy(speed)






