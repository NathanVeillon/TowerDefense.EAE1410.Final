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


class newEnemy:

    def __init__(self, pos, surf, speed, size, health, tileSize, image):
        ## position information
        self.pos = pos
        self.TILESIZE = tileSize
        self.truePositionY = pos[1] * self.TILESIZE
        self.truePositionX = pos[0] * self.TILESIZE
        self.SPEED = speed
        self.SIZE = size

        self.SURF = surf
        self.health = health
        self.feed = False

        self.YDIRECTION = False
        if self.SPEED[0] ==0:
            self.YDIRECTION = True
        self.IMAGE = image

    ## Moves the enemy, then checks to see if the enemy has reached the next tile
    ## if the enemy has reached the next tile, requests new info
    def __moveEnemy(self):

        ## changes position according to speed
        self.truePositionX += self.SPEED[0]
        self.truePositionY += self.SPEED[1]

        ## Checks to see if enemy is within 1 tick of the next tile
        if self.YDIRECTION:
            if self.truePositionY % self.SPEED[1] < abs(self.SPEED[1]):
                self.SPEED[1] = self.truePositionY % self.SPEED[1]
                self.feed = True

        else:
            if self.truePositionX % self.SPEED[0] < abs(self.SPEED[0]):
                self.SPEED[0] = self.truePositionX % self.SPEED[0]
                self.feed = True


    ## this function will be called by the Enemy Wave class to see if an enemy needs new information.
    ## if it returns true, the enemy wave will feed it more info.
    def checkFeed(self):
        if (self.feed):
            return True

        return False

    def updateEnemy(self, speed):
        self.SPEED = speed
        self.YDIRECTION = False
        if self.SPEED[0] ==0:
            self.YDIRECTION = True
    
    def getPosition(self):
        return self.pos

    ## Damages the enemy.
    def damage_enemy(self, damage):
        self.health -= damage
    
    ## displays the enemy.
    def disp_enemy(self):
        self.__moveEnemy()
        self.SURF.blit(IMAGE, self.__findBlitPosition())

    ## determines where to blit the enemy to the screen
    def __findBlitPosition(self):
        xPosition = truePositionX - (self.SIZE//2)
        yPosition = truePositionY - (self.SIZE//2)

        return xPosition, yPosition



