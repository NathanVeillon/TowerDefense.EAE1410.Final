# BaseTower.py
#
# File Contributors
#     Joshua Rosen
#
# Purpose:
# BaseTower class to be inherited by other tower types

import time
import pygame
from pygame.locals import *
from math import sqrt

class BaseTower():

    #tower_size should be equal to tile_size
    def __init__(self, tower_size, position, attack_radius, enemy_wave_list, image_location='Library/Assets/Towers/BaseTower.png'):
        self.window = pygame.display.get_surface()
        self.position = position
        self.dimension = (tower_size, tower_size)
        self.center_position = (self.position[0] + self.dimension[0] // 2, self.position[1] + self.dimension[1] // 2)

        self.image = pygame.image.load(image_location).convert()
        self.image = pygame.transform.scale(self.image,self.dimension)

        self.radius = attack_radius

        self.total_enemy_wave = enemy_wave_list
        self.enemy_to_attack = self.find_first_enemy()

        self.type = 'BaseTower'

        self.placed = False #False if the player is still in the process of placing the tower, True otherwise
        self.tile_surface = None #The surface of the tile that the tower has been placed upon, needed for display_tower
                                 #  method to blit the tower upon the tile

    #Call this when the next enemy wave
    def get_new_wave(self, new_wave):
        self.total_enemy_wave = new_wave

    #Check to see if passed enemy is within the radius of the tower
    def enemy_within_range(self, enemy):
        e_pos = enemy.position
        t_pos = self.center_position
        distance = sqrt((e_pos[0] - t_pos[0])**2 + (e_pos[1] - t_pos[1])**2)
        return (distance < self.radius)

    #Find the first enemy to attack
    def find_first_enemy(self):
        for enemy in self.total_enemy_wave:
            if self.enemy_within_range(enemy):
                return enemy

        return None

    #Draws a line to attack enemy
    def attack_enemy(self):
        if (time.clock() % 3 == 0): #Time delay for attacking

            if (self.enemy_to_attack == None):
                return None

            attack_position = self.enemy_to_attack.position
            pygame.draw.line(pygame.display.get_surface(), (0, 0, 0), (self.center_position[0], self.center_position[1]), attack_position, 2)

    #Blits tower onto main window (if being placed) or onto tile surface (if already placed)
    def display_tower(self):
        if (self.placed == False):
            self.image.set_alpha(128) #Make unplaced tower transparent
            pos = self.find_mouse_pos()
            self.window.blit(self.image, pos)
        else:
            self.image.set_alpha(255) #Make placed tower opaque
            tile_size = (self.tile_surface.get_width(), self.tile_surface.get_height())

            #Blit the tower onto the CENTER of the tile_surface
            self.tile_surface.blit(self.image, ((tile_size[0] - self.dimension[0]) // 2, (tile_size[1] - self.dimension[1])//2))

    #Returns the mouse position as the center of the tower being placed
    def find_mouse_pos(self):
        mouse_pos = list(pygame.mouse.get_pos())
        mouse_pos[0] -= self.dimension[0] // 2
        mouse_pos[1] -= self.dimension[1] // 2
        return mouse_pos