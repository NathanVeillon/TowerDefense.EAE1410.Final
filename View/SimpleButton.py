# SimpleButton.py
#
# File Contributors
#     Joshua Rosen
#
# Purpose:
# Simple button class for the LevelMenu

import pygame
from pygame.locals import *

class SimpleButton:

    def __init__(self, dimension, image_location, surf, position):
        self.surf = surf
        self.pos = position
        self.dimension = dimension

        self.active = True #Deactivate button after round starts?

        self.image = pygame.image.load(image_location).convert_alpha()
        self.image = pygame.transform.scale(self.image,self.dimension)

    #Returns true if the user clicked within the button bounds
    def clicked(self, MOUSEXY):
        P1 = self.pos
        P2 = (P1[0] + self.dimension[0], P1[1] + self.dimension[1])
        within_bounds = (self.active and P1[0] <= MOUSEXY[0] <= P2[0] and P1[1] <= MOUSEXY[1] <= P2[1])
        return within_bounds

    #Blits button onto surface
    def display_button(self, cost=0):
        self.surf.blit(self.image, self.pos)

        if (cost != 0):
            self.text = pygame.font.SysFont("Lucida Console", 96).render("Cost: $" + str(cost), True, (76, 50, 25), None)
            self.text = pygame.transform.scale(self.text, (100, 20))
            self.image.blit(self.text, (20, self.dimension[1] - 20))




