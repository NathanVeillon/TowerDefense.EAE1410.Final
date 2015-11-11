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

    def __init__(self, height, width, color, text_color, label, text_size, surf, position):
        self.surf = surf
        self.pos = position
        self.button_color  = color

        self.highlight_color = (color[0] + ((255 - color[0])//3),
                               color[1] + ((255 - color[1])//3),
                               color[2] + ((255 - color[2])//3))

        self.height = height
        self.width = width
        self.radius = self.height//2

        self.ACTIVE = True
        self.HILIGHTED = False

        button_font = pygame.font.SysFont("Sylfaen", text_size)
        self.text_surf = button_font.render(label, True, text_color, None)

        w, h = self.text_surf.get_size()

        self.XPOS = (self.width - w)//2
        self.YPOS = int((self.height - h)//2)

        self.BUTTONSURF = pygame.Surface((self.width, self.height), flags=SRCALPHA, depth=32)
        self.BUTTONSURF.fill((0, 0, 0, 0))

    def buttonBG(self, color):
        #Draws a square with rounded corners
        pygame.draw.circle(self.BUTTONSURF, color, (self.radius, self.radius), self.radius)
        pygame.draw.circle(self.BUTTONSURF, color, (self.width - self.radius, self.radius), self.radius)

        pygame.draw.rect(self.BUTTONSURF, color,  Rect((self.radius, 0), (self.width - 2 * self.radius, self.height)))

    def __buttonText(self):
        self.BUTTONSURF.blit(self.text_surf, (self.XPOS, self.YPOS))

    #Returns true if the user clicked within the button bounds
    def clicked(self, MOUSEXY):
        P1 = self.pos
        P2 = (P1[0] + self.width, P1[1] + self.height)
        within_bounds = (self.ACTIVE and P1[0] <= MOUSEXY[0] <= P2[0] and P1[1] <= MOUSEXY[1] <= P2[1])

        return within_bounds

    def Active(self):
        self.ACTIVE = True
        return True

    def InActive(self):
        self.ACTIVE = False
        return False

    #Blits button onto surface
    def display_button(self):

        if self.ACTIVE:
            if self.HILIGHTED:
                self.buttonBG(self.highlight_color)
                self.__buttonText()
                self.surf.blit(self.BUTTONSURF, self.pos)
            else:
                self.buttonBG(self.button_color)
                self.__buttonText()
                self.surf.blit(self.BUTTONSURF, self.pos)




