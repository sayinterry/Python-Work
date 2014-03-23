import pygame
import button
import asdfa
from globs import *

class Mainmenu:
    def __init__(self):
        self.back = pygame.transform.scale(GFX["bg"], SCREENSIZE)
        self.button1 = button.Button()
        self.button1.create_button("b1up", "b1hover", "b1down", "vsCPU", [375,250])
        self.button2 = button.Button()
        self.button2.create_button("b2up", "b2hover", "b2down", "vsHUMAN", [375,350])
        self.done = False
        self.mode = None

    def mainmenu_event(self,event):
        """Press any key to continue."""
        """if event.type == pygame.KEYDOWN:
            self.done = True"""
        self.button1.button_event(event)
        self.button2.button_event(event)
        if self.button1.done or self.button2.done:
            if self.button1.mode != None:
                self.mode = self.button1.mode
            else :
                self.mode = self.button2.mode
            self.done = True

    def update(self,Surf):
        Surf.blit(self.back, (0,0))
        self.button1.button_draw(Surf)
        self.button2.button_draw(Surf)
