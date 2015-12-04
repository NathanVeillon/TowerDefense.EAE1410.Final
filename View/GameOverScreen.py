#GameOverScreen.py
#
# File Contributors
#     Joshua Rosen

import pygame
from pygame.locals import *

class GameOverScreen():

    def __init__(self, black_image_location='Library/Assets/GameOver.png'):
        self.window = pygame.display.get_surface()

        self.cur_alpha = 0
        self.black_image = pygame.image.load(black_image_location).convert()
        self.black_image = pygame.transform.scale(self.black_image,(self.window.get_width(), self.window.get_height()))
        self.black_image.set_alpha(self.cur_alpha)

        self.game_over_font = pygame.font.SysFont("Cambria", 240)
        self.cur_red = 0

        self.timer = 0

    def display_self(self):
        self.timer += 1

        if (self.cur_alpha != 255):
            self.cur_alpha += 1
        self.black_image.set_alpha(self.cur_alpha)
        self.window.blit(self.black_image, (0,0))

        if (self.cur_red != 255):
            self.cur_red += 1
        self.game_over_surf = self.game_over_font.render("GAME OVER", True, (self.cur_red, 0, 0), None)
        self.game_over_surf = pygame.transform.scale(self.game_over_surf, (600, 400))
        self.window.blit(self.game_over_surf, (50, 75))