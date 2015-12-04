#BaseEnemy.py
# 
# File Contributors
#     David Mirabile
#     Nathan Veillon
#     Joshua Rosen
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
        self.speed = speed
        self.movement = (0,0)
        self.size = size

        self.image = pygame.image.load(image_location)
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()

        self.health = health
        self.feed = True

        self.y_direction = False
        if self.movement[0] ==0:
            self.y_direction = True
        self.window = pygame.display.get_surface()

        self.health_total = health
        self.health_bar_total = self.size[0]
        self.health_bar = self.size[0]

    ## Moves the enemy, then checks to see if the enemy has reached the next tile
    ## if the enemy has reached the next tile, requests new info
    def __move_enemy(self):

        ## changes position according to speed
        self.x_position += self.movement[0]
        self.y_position += self.movement[1]

        self.current_tile_position = (floor(self.x_position/self.tile_size), floor(self.y_position/self.tile_size))

        current_tile_middle_x_position = (self.current_tile_position[0]*self.tile_size)+(self.tile_size//2)
        current_tile_middle_y_position = (self.current_tile_position[1]*self.tile_size)+(self.tile_size//2)

        current_tile_middle_position = (current_tile_middle_x_position,current_tile_middle_y_position)

        ## Checks to see if enemy is within 1 tick of the next tile
        if self.y_direction:
            if abs(self.y_position - current_tile_middle_y_position) < abs(self.movement[1]):
                self.x_position = current_tile_middle_position[0]
                self.y_position = current_tile_middle_position[1]
                self.feed = True

        else:
            if abs(self.x_position - current_tile_middle_x_position) < abs(self.movement[0]):
                self.x_position = current_tile_middle_position[0]
                self.y_position = current_tile_middle_position[1]
                self.feed = True

        self.position = (self.x_position,self.y_position)
        self.rect.x = self.x_position
        self.rect.y = self.y_position


    ## this function will be called by the Enemy Wave class to see if an enemy needs new information.
    ## if it returns true, the enemy wave will feed it more info.
    def check_feed(self):
        if (self.feed):
            return True

        return False

    def update_enemy(self, speed):
        self.movement = speed
        self.feed = False
        self.y_direction = False
        if self.movement[0] ==0:
            self.y_direction = True
    
    def get_tile_position(self):
        return self.current_tile_position

    ## Damages the enemy.
    def damage_enemy(self, damage):
        self.health -= damage

        #Adjusts health bar proportionally based on actual health value/damage taken
        prop_dmg = damage / self.health_total
        health_bar_dmg = self.health_bar_total * prop_dmg
        self.health_bar -= health_bar_dmg
    
    ## displays the enemy.
    def display_enemy(self):
        self.__move_enemy()

        #Health bar
        GREEN = (0, 255, 0)
        YELLOW = (255, 255, 0)
        RED = (255, 0, 0)

        cur_color = GREEN
        if (self.health_bar <= self.health_bar_total // 2):
            cur_color = YELLOW
        if (self.health_bar <= self.health_bar_total // 4):
            cur_color = RED
        pygame.draw.rect(self.window, cur_color, Rect((self.__find_blit_position()[0], self.__find_blit_position()[1] - 12),
                                                       (self.health_bar,   5)))


        self.window.blit(self.image, self.__find_blit_position())

    ## determines where to blit the enemy to the screen
    def __find_blit_position(self):
        xPosition = self.x_position - (self.size[0]//2)
        yPosition = self.y_position - (self.size[1]//2)

        return (xPosition, yPosition)
