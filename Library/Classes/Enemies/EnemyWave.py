#EnemyWave.py
# 
# File Contributors
#     Nathan Veillon
#     David Mirabile
#

import time
from .BaseEnemy import *

class EnemyWave:
    def __init__(self, tile_map, raw_text_wave=None):
        if(raw_text_wave):
            text_wave = raw_text_wave
        else:
            text_wave = {}

        self.tile_map = tile_map
        self.queued_enemies = self.import_enemies(text_wave)
        self.enemies_to_display = []

        self.timer = 0

    def __iter__(self):
        return self.enemies_to_display.__iter__()

    def change_text_wave(self, raw_new_text):
        if(raw_new_text):
            new_text_wave = raw_new_text
        else:
            new_text_wave = {}

        self.queued_enemies += self.import_enemies(new_text_wave)

    def import_enemies(self,text_wave):
        list_of_enemies = []
        for enemy_type,enemy_quantity in text_wave.items():
            for x in range(enemy_quantity):
                try:
                    list_of_enemies.append(eval(enemy_type)(self.tile_map))
                except:
                    list_of_enemies.append(BaseEnemy(self.tile_map))

        return list_of_enemies

    def spawn_enemy(self):
        if len(self.queued_enemies) > 0:
            self.timer += 1
            if self.timer > 100:
                self.timer = 0
                enemy = self.queued_enemies.pop()
                self.enemies_to_display.append(enemy)

    def display_enemies(self):
        for enemy in self.enemies_to_display:
            if(enemy.current_health <= 0):
                self.enemies_to_display.remove(enemy)
            else:
                enemy.move_enemy()
                enemy.display_enemy()

