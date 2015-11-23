#BaseEnemy.py
# 
# File Contributors
#     Nathan Veillon
#
# 
import math
import pygame
from pygame.locals import *
from Library.Classes.Tiles.Path import *

class BaseEnemy(pygame.sprite.Sprite):

    def __init__(self,dimensions,speed,health,image_location='Library/Assets/Enemies/BaseEnemy.png'):
        pygame.sprite.Sprite.__init__(self)

        self.window = pygame.display.get_surface()

        self.dimensions = dimensions
        self.speed = speed
        self.total_health = health
        self.current_health = health
        self.position = (50,50)
        self.blit_position = self.find_blit_position()

        self.image = pygame.Surface(dimensions, flags=SRCALPHA, depth=32)

        self.enemy_surface = pygame.image.load(image_location).convert_alpha()
        self.enemy_surface = pygame.transform.scale(self.enemy_surface, dimensions)

        self.rect = self.image.get_rect()

        self.tile_map = None
        self.current_tile = None
        self.past_center = False

    def find_blit_position(self):
        return (self.position[0]-(self.dimensions[0]//2), self.position[1]-(self.dimensions[1]//2))

    def set_enemy_tile_map(self,tile_map):
        self.tile_map = tile_map
        tile_size = self.tile_map.tile_size
        start_position = self.tile_map.start_position
        self.position = ((start_position[0]*tile_size)+(tile_size//2),(start_position[1]*tile_size)+(tile_size//2))

    def find_current_tile(self):
        tile_size = self.tile_map.tile_size
        current_tile_x = self.position[0]//tile_size
        current_tile_y = self.position[1]//tile_size
        current_tile = self.tile_map.tile_map[current_tile_x][current_tile_y]

        return current_tile

    def move_enemy(self):
        current_tile = self.find_current_tile()
        tile_size = self.tile_map.tile_size

        if(self.current_tile != current_tile):
            self.past_center = False

        if(self.position == current_tile.middle_position):
            self.past_center = True

        self.current_tile = current_tile
        if(isinstance(self.current_tile, Path)):
            current_tile_direction = self.current_tile.current_direction

            if(self.past_center):
                self.move_based_on_direction(current_tile_direction)
            else:
                self.go_to_center_of_tile()
        else:
            start_position = self.tile_map.start_position
            self.position = ((start_position[0]*tile_size)+(tile_size//2),(start_position[1]*tile_size)+(tile_size//2))

    def move_based_on_direction(self,direction):
        x,y = self.position
        if(direction == 'U'):
            y -= self.speed
        elif(direction == 'L'):
            x -= self.speed
        elif(direction == 'D'):
            y += self.speed
        elif(direction == 'R'):
            x += self.speed

        self.position = (x,y)

    def go_to_center_of_tile(self):
        tile_center_position = self.current_tile.middle_position
        x_position_difference = tile_center_position[0]-self.position[0]
        y_position_difference = tile_center_position[1]-self.position[1]


        norm = (x_position_difference**2)+(y_position_difference**2)
        distance = math.sqrt(norm)

        if(distance < self.speed):
            self.position = tile_center_position
        else:
            x_normalized = (x_position_difference/distance)
            y_normalized = (y_position_difference/distance)
            x = self.position[0]+int(x_normalized*self.speed)
            y = self.position[1]+int(y_normalized*self.speed)
            self.position = (x,y)

    def damage_enemy(self,damage):
        self.current_health -= damage

    def display_enemy(self):
        self.blit_position = self.find_blit_position()
        self.window.blit(self.enemy_surface,self.blit_position)




