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

import pygame
from pygame.locals import *

class BaseEnemy:

    def __init__(self, pos, image_location, speed, size, health, tileSize):
        ## position information
        self.current_tile_position = pos
        self.tile_size = tileSize
        self.true_position_y = pos[1] * self.tile_size
        self.true_position_x = pos[0] * self.tile_size
        self.speed = speed
        self.size = size

        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.rect()

        self.health = health
        self.feed = False

        self.y_direction = False
        if self.speed[0] ==0:
            self.y_direction = True
        self.window = pygame.display.get_surface()

    ## Moves the enemy, then checks to see if the enemy has reached the next tile
    ## if the enemy has reached the next tile, requests new info
    def __move_enemy(self):

        ## changes position according to speed
        self.true_position_x += self.speed[0]
        self.true_position_y += self.speed[1]

        ## Checks to see if enemy is within 1 tick of the next tile
        if self.y_direction:
            if self.true_position_y % self.speed[1] < abs(self.speed[1]):
                self.speed[1] = self.true_position_y % self.speed[1]
                self.feed = True

        else:
            if self.true_position_x % self.speed[0] < abs(self.speed[0]):
                self.speed[0] = self.true_position_x % self.speed[0]
                self.feed = True


    ## this function will be called by the Enemy Wave class to see if an enemy needs new information.
    ## if it returns true, the enemy wave will feed it more info.
    def check_feed(self):
        if (self.feed):
            return True

        return False

    def update_enemy(self, speed):
        self.speed = speed
        self.y_direction = False
        if self.speed[0] ==0:
            self.y_direction = True
    
    def get_tile_position(self):
        return self.current_tile_position

    ## Damages the enemy.
    def damage_enemy(self, damage):
        self.health -= damage
    
    ## displays the enemy.
    def display_enemy(self):
        self.__move_enemy()
        self.window.blit(self.image, self.__find_blit_position())

    ## determines where to blit the enemy to the screen
    def __find_blit_position(self):
        xPosition = self.true_position_x - (self.size//2)
        yPosition = self.true_position_y - (self.size//2)

        return xPosition, yPosition



