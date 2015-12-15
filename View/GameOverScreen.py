#GameOverScreen.py
#
# File Contributors
#     Joshua Rosen
#     Kathy Huang
import pygame
from pygame.locals import *
from Library.Classes.Animation import pyganim

class GameOverScreen():

    def __init__(self):
        self.window = pygame.display.get_surface()

        self.cur_alpha = 0
        self.image_location='Library/Assets/GameOver/GameOver'
        image_locations = [('%s_%s.png' % (self.image_location, str(num).rjust(3, '0')), 0.1) for num in range(30)]

        self.gameoverAnim = pyganim.PygAnimation(image_locations)
        self.gameoverAnim.play()

        #Royalty-Free sound effect from Adobe
        #http://offers.adobe.com/en/na/audition/offers/audition_dlc.html
        gameOverSound = pygame.mixer.Sound('Library\Assets\Music\Explosion Building Demolition Debris 01.wav')
        gameOverSound.set_volume(1.0)
        gameOverSound.play()

        self.cur_red = 0

        self.timer = 0

    def display_self(self):
        self.timer += 1

        if (self.cur_alpha != 255):
            self.cur_alpha += 5
        self.gameoverAnim.set_alpha(self.cur_alpha)
        self.gameoverAnim.blit(self.window, (0,0))
