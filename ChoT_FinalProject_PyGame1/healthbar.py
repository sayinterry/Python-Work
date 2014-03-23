import pygame

from globs import *

red = (255,0,0)

class Health:
    def __init__(self, player):
        if player == 1:
            self.image = GFX["healthbar"]
            self.x = 50
            self.y = 30
            self.barC1 = ((self.x+63),(self.y+15))
            self.player = 1
        elif player == 2:
            self.image = pygame.transform.flip(GFX["healthbar"],True,False)
            self.x = 610
            self.y = 30
            self.barC1 = (self.x,(self.y+15))
            self.player = 2
        self.barWidth = 277
        self.barHeight = 75
        self.HP = 100

    def update(self, Surf):
        pygame.draw.rect(Surf, red, [self.barC1, (self.barWidth, self.barHeight)], 0)
        Surf.blit(self.image, (self.x, self.y))

    def updateHP(self, health):
        if self.player == 2:
            self.barC1 = ((self.x+(277*((100-health)*0.01))), (self.y+15))
        self.barWidth = 277*(health*0.01)
