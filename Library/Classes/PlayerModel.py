#DisplayLevel.py
#
# File Contributors
#     Joshua Rosen
#
# Purpose:
# Holds onto player instance variables

class PlayerModel():

    def __init__(self, starting_money, starting_lives):
        self.wallet = starting_money
        self.lives = starting_lives

