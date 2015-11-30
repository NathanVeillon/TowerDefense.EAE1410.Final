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
from Library.Classes.Bullets.BaseBullet import *
from Library.Classes.Bullets.Vector import *
from math import *

class BaseTower():
    cost = 50 #Static instance variable

    def __init__(self, tower_size, position, attack_radius, enemy_wave_list, tile_map_size, image_location='Library/Assets/Towers/BaseTower.png'):
        self.window = pygame.display.get_surface()
        self.position = position #When the tower is placed, this position is set to the corresponding tile's position
        self.dimension = (tower_size, tower_size) #tower_size should be equal to tile_size
        self.center_position = (self.position[0] + self.dimension[0] // 2, self.position[1] + self.dimension[1] // 2)

        self.image = pygame.image.load(image_location).convert()
        self.image = pygame.transform.scale(self.image,self.dimension)

        self.attack_radius = attack_radius
        self.bullet_damage = 10
        self.bullet_speed = 5

        self.enemy_wave = enemy_wave_list
        self.enemy_to_attack = None

        self.type = 'BaseTower'

        self.tile_map_size = tile_map_size - 5 #The size of the tile_map, for removing bullets if they leave it

        self.placed = False #False if the player is still in the process of placing the tower, True otherwise
        self.tile_surface = None #The surface of the tile that the tower has been placed upon, needed for display_tower
                                 #  method to blit the tower upon the tile

        self.bullet_list = pygame.sprite.Group() #List of bullets that this tower generates

        self.timer = 0 #Time delay for attacking

    #Set the enemy_wave to the next wave in the list
    def get_new_wave(self, new_wave):
        self.enemy_wave = new_wave

    #Check to see if passed enemy is within the radius of the tower
    def enemy_within_range(self, enemy):
        #e_pos = enemy.position
        e_pos = enemy.position #Enemy is currently just a point

        t_pos = self.center_position
        distance = sqrt((e_pos[0] - t_pos[0])**2 + (e_pos[1] - t_pos[1])**2)
        return (distance < self.attack_radius)

    #Find the first enemy to attack
    def find_first_enemy(self):
        for enemy in self.enemy_wave:
            if self.enemy_within_range(enemy):
                return enemy

        return None

    #Fires a bullet to attack enemy
    def attack_enemy(self):
        self.enemy_to_attack = self.find_first_enemy()

        self.timer += 1 #Needs a time delay for attacking
        if (self.timer == 75):
            self.timer = 0

            if (self.enemy_to_attack == None):
                return None

            attack_position = self.enemy_to_attack.position
            attack_position = tuple(attack_position)
            # attack_position = self.enemy_to_attack #Enemy is currently just a point

            attack_vector = Vector.fromPoints(self.center_position, attack_position)
            attack_vector = attack_vector.normalize()

            self.bullet_list.add(BaseBullet(self.center_position, (5,5), self.bullet_speed, attack_vector, self.bullet_damage))

    #Blits tower onto main window (if being placed) or onto tile surface (if already placed)
    def display_tower(self):
        if (self.placed == False):
            self.image.set_alpha(128) #Make unplaced tower transparent
            self.center_position = self.find_centered_mouse_pos()
            self.window.blit(self.image, self.center_position)
        else:
            self.image.set_alpha(255) #Make placed tower opaque

            tile_size = (self.tile_surface.get_width(), self.tile_surface.get_height())

            #Assigns the center_position to the center of the tile (thus the center of the tower, visually)
            self.center_position = (self.position[0] + tile_size[0] // 2, self.position[1] + tile_size[1] // 2)

            #Blit the tower onto the CENTER of the tile_surface, coordinates are relative to the tile
            self.tile_surface.blit(self.image, ((tile_size[0] - self.dimension[0]) // 2, (tile_size[1] - self.dimension[1])//2))

            self.draw_bullets()


    #Returns the mouse position as the center of the tower being placed
    def find_centered_mouse_pos(self):
        mouse_pos = list(pygame.mouse.get_pos())
        mouse_pos[0] -= self.dimension[0] // 2
        mouse_pos[1] -= self.dimension[1] // 2
        return mouse_pos

    def draw_bullets(self):
        for bullet in self.bullet_list:
            if (bullet.position[0] < 0 or bullet.position[1] < 0
                or bullet.position[1] > self.tile_map_size or bullet.position[0] > self.tile_map_size):
                self.bullet_list.remove(bullet) #If bullet goes offscreen, remove bullet
            else:
                bullet.display_bullet()