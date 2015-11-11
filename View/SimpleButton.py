# simpleButtonClass003.py

import pygame
from pygame.locals import *

class SimpleButton:

    # class that creates button objects

    def __init__(self, height, width, color, textColor, label, textSize, surf, position):

        # define some values

        self.SURF = surf
        self.POS = position
        self.BUTCOLOR  = color
        self.HIGHLIGHTCOLOR = (color[0] + ((255 - color[0])//3),
                               color[1] + ((255 - color[1])//3),
                               color[2] + ((255 - color[2])//3))

        self.TEXTCOLOR = textColor
        self.TEXTSIZE = textSize

        self.HEIGHT   = height
        self.WIDTH  = width
        self.RADIUS   = self.HEIGHT//2
        #THEIGHT  = int(self.HEIGHT * .72)

        self.ACTIVE = True
        self.HILIGHTED = False

        self.BUTFONT = pygame.font.SysFont("Sylfaen", self.TEXTSIZE)
        # Render a Text Surface
        self.TEXTSURF = self.BUTFONT.render(label, True, textColor, None)

        w, h   = self.TEXTSURF.get_size()

        self.XPOS   = (self.WIDTH - w)//2
        self.YPOS   = int((self.HEIGHT - h)//2)

        self.BUTTONSURF = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.BUTTONSURF.fill((0, 0, 0, 0))

    def buttonBG(self, color):

        # create square with rounded corners

        pygame.draw.circle(self.BUTTONSURF, color, (self.RADIUS, self.RADIUS),
                           self.RADIUS)
        pygame.draw.circle(self.BUTTONSURF, color,
                           (self.WIDTH - self.RADIUS, self.RADIUS), self.RADIUS)

        pygame.draw.rect(self.BUTTONSURF, color,  Rect((self.RADIUS, 0), (self.WIDTH - 2 * self.RADIUS, self.HEIGHT)))

    def buttonText(self):

        # Draw Text
        self.BUTTONSURF.blit(self.TEXTSURF, (self.XPOS, self.YPOS))

    def clicked(self, MOUSEXY):
        yesORno = False
        P1 = self.POS
        P2 = (P1[0] + self.WIDTH, P1[1] + self.HEIGHT)
        yesORno = (self.ACTIVE and P1[0] <= MOUSEXY[0] <= P2[0] and
                   P1[1] <= MOUSEXY[1] <= P2[1])

        return yesORno

    def Active(self):
        self.ACTIVE = True
        return True

    def InActive(self):
        self.ACTIVE = False
        return False


    def displayBut(self):

        if self.ACTIVE:
            if self.HILIGHTED:
                self.buttonBG(self.HIGHLIGHTCOLOR)
                self.buttonText()
                self.SURF.blit(self.BUTTONSURF, self.POS)
            else:
                self.buttonBG(self.BUTCOLOR)
                self.buttonText()
                self.SURF.blit(self.BUTTONSURF, self.POS)




