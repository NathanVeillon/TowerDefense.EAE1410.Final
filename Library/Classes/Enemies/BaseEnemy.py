#BaseEnemy.py
# 
# File Contributors
#       David Mirabile
# 
# Purpose:
# Holds basic information about health and displaying of an enemy.

import pygame, math
from Library.Classes.Tiles.Path import *
from Library.Classes.Bullets.Vector import *
from random import randint

## Implementation notice:
## This class is an individual enemy.
## This class will be managed by the EnemyWave class

## This class is unfinished.
class newEnemy:

    def __init__(self, pos, surf, speed, health, tileSize, image):
        self.pos = pos
        self.SURF = surf
        self.SPEED = speed
        self.TILESIZE = tileSize
        self.health = health
        self.change = self.SPEED
        self.feed = False

        self.IMAGE = image

    ## Checks to see if the enemy has reached the next tile, and then...
    ## if the enemy has reached the next tile, requests new info
    ## BUGGED NEEDS FIXING
    ## BUGGED NEEDS FIXING
    ## BUGGED NEEDS FIXING
    def __moveEnemy(self):
        if (self.pos % self.TILESIZE < self.SPEED):
            self.change = self.POS % self.TILESIZE
            self.feed = True

        self.pos += self.change
        self.change = self.SPEED

    ## this function will be called by the Enemy Wave class to see if an enemy needs new information.
    ## if it returns true, the enemy wave will feed it more info.
    def checkFeed(self):
        if (self.feed):
            return True

        return False

    def updateEnemy(self, speed):
        self.SPEED = speed
    
    def getPosition(self):
        return self.POS

    ## Damages the enemy.
    def damage_enemy(self, damage):
        self.health -= damage
    
    ## displays the enemy.
    def disp_enemy(self):
        __moveEnemy()
        self.SURF.blit(IMAGE, pos)



