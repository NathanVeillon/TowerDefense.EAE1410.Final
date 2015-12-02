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

class BaseEnemy(pygame.sprite.Sprite):

    def __init__(self, current_tile_position, image_location, speed, size, health, tileSize):
        ## position information
        pygame.sprite.Sprite.__init__(self)
        self.current_tile_position = current_tile_position
        self.tile_size = tileSize
        self.x_position = current_tile_position[0] * self.tile_size + (self.tile_size//2)
        self.y_position = current_tile_position[1] * self.tile_size + (self.tile_size//2)
        self.position = (self.x_position,self.y_position)
        print(self.position)
        self.speed = speed
        self.movement = (0,1)
        self.size = size

        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        self.health = health
        self.feed = False

        self.y_direction = False
        if self.movement[0] ==0:
            self.y_direction = True
        self.window = pygame.display.get_surface()

    ## Moves the enemy, then checks to see if the enemy has reached the next tile
    ## if the enemy has reached the next tile, requests new info
    def __move_enemy(self):

        ## changes position according to speed
        self.x_position += self.movement[0]
        self.y_position += self.movement[1]

        self.current_tile_position = (floor(self.x_position/self.tile_size), floor(self.y_position/self.tile_size))

        ## Checks to see if enemy is within 1 tick of the next tile
        if self.y_direction:
            if self.y_position % (self.tile_size//2) < abs(self.movement[1]):
                y_movement = self.y_position % self.movement[1]
                self.movement = (y_movement,0)
                self.feed = True

        else:
            if self.x_position % (self.tile_size//2) < abs(self.movement[0]):
                x_movement = self.x_position % self.movement[0]
                self.movement = (x_movement,0)
                self.feed = True




    ## this function will be called by the Enemy Wave class to see if an enemy needs new information.
    ## if it returns true, the enemy wave will feed it more info.
    def check_feed(self):
        if (self.feed):
            return True

        return False

    def update_enemy(self, speed):
        self.movement = speed
        self.y_direction = False
        if self.movement ==0:
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
        xPosition = self.x_position - (self.size[0]//2)
        yPosition = self.y_position - (self.size[1]//2)

        return (xPosition, yPosition)



