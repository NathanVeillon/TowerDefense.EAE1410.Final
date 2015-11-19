# Vector.py
#
# File Contributors
#     Joshua Rosen
#
# Purpose:
# Simplified vector class, used for bullet movement

from math import *

class Vector(object):
    def __init__(self, vXf = 0.0, vYf = 0.0):
        self.vX = vXf
        self.vY = vYf
        self.vector = [self.vX, self.vY]

    def __add__(self, rV):
        return Vector(self.vX + rV.vX, self.vY + rV.vY)

    def __sub__(self, rV):
        return Vector(self.vX - rV.vX, self.vY - rV.vY)

    def __mul__(self, rS):
        return Vector(self.vX * rS, self.vY * rS)

    def __truediv__(self, rS):
        return Vector(self.vX / rS, self.vY / rS)

    @staticmethod
    def fromPoints(P1, P2):
        return Vector(P2[0] - P1[0], P2[1] - P1[1])

    def normalize(self):
        mag = self.length()
        X = self.vX / mag
        Y = self.vY / mag
        return Vector(X, Y)

    def length(self):
        LV2 = sqrt((self.vector[0] * self.vector[0])+
                   (self.vector[1] * self.vector[1]))
        return LV2

    def rotate(self, theta):
        rad = radians(theta)
        X = round((self.vX * cos(rad)) - (self.vY * sin(rad)), 3)
        Y = round((self.vX * sin(rad)) + (self.vY * cos(rad)), 3)
        return Vector(X, Y)