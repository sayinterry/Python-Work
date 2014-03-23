import pygame
import math

from globs import *

class Handler():
    def __init__(self):
        self.p1 = None
        self.p2 = None

    def check(self, aggressor, victim):
        self.p1 = aggressor
        self.p2 = victim
        if self.p1.getCharacter() == "ZEKE":
            if self.p1.getAttack_type() == "LOW1":
                if self.p1.getStateFrame() == 25:
                    if math.fabs(((self.p1.getX()) - self.p2.getX())) <= 183 and math.fabs(((self.p1.getX()) - self.p2.getX())) >= 90:
                        if self.p2.getY() < 430:
                            self.p2.hit_by(self.p1.getAttack_type(), self.p1.getCharacter())
            elif self.p1.getAttack_type() == "HIGH1":
                if self.p1.getStateFrame() == 30:
                    if math.fabs(((self.p1.getX()) - self.p2.getX())) <= 135 and math.fabs(((self.p1.getX()) - self.p2.getX())) >= 100:
                        if self.p2.getY() < 450:
                            self.p2.hit_by(self.p1.getAttack_type(), self.p1.getCharacter())
