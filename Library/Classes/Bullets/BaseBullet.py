# BaseBullet.py
#
# File Contributors
#     Joshua Rosen
#
# Purpose:
# BaseBullet class, used for the bullets that the towers shoot.
#   If, in the future, we decide to have multiple towers with multiple types
#   of bullets, this class could be inherited.

import pygame
from pygame.locals import *
from math import *

class BaseBullet(pygame.sprite.Sprite):

    def __init__(self, pos, size, speed, vector, damage, image_location='Library/Assets/Bullets/BaseBullet.png'):
        #Calls the super constructor
        pygame.sprite.Sprite.__init__(self)

        self.size = size
        self.position = pos
        self.speed = speed
        self.vector = vector #should be a Vector object
        self.damage = damage

        self.window = pygame.display.get_surface() #Main window

        self.image = pygame.image.load(image_location).convert()
        self.image = pygame.transform.scale(self.image,self.size)

        self.rect = self.image.get_rect() #Needs a rect attribute for collision detection

    #Moves the bullet and blits bullet onto the main window
    def display_bullet(self):
        self.move_bullet()
        self.window.blit(self.image, (self.position[0] - self.size[0] // 2, self.position[1] - self.size[1] // 2))

    #Changes the bullet's position according to its speed and vector
    def move_bullet(self):
        newPosX = self.position[0] + (self.vector.vX * self.speed)
        newPosY = self.position[1] + (self.vector.vY * self.speed)
        self.position = (newPosX, newPosY)

        self.rect.x = self.position[0] - self.size[0] // 2
        self.rect.y = self.position[1] - self.size[1] // 2