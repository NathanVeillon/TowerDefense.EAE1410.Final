#BaseEnemy.py
# 
# File Contributors
#       David Mirabile
# 
# Purpose:
# Generates an individual enemy.

import pygame, math
from random import randint


class newEnemy:

    def __init__(self, pos, surf, speed, health):
        self.POS = pos
        self.SURF = surf
        self.SPEED = speed
        self.HEALTH = health


    
    def damage_enemy(self, damage):
        self.HEALTH -= damage

    def disp_enemy(self):
        pass