# main.py
#
# File Contributors
#     Nathan Veillon
#     Kathy Huang
# Purpose:
# Main File to run Game

#Royalty-free music taken from incompetech.com
            #http://incompetech.com/music/royalty-free/index.html?isrc=USUAN1400005

#Royalty-free music taken from bensound.com
            #http://www.bensound.com/royalty-free-music/track/epic
            
import sys
import pygame
from pygame.locals import *
from Library.Classes.Tiles.BaseTile import *
from Library.Classes.Display.DisplayWindow import *

a = DisplayWindow()
a.display_window()
# a.displayLevel('Level01')