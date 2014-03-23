import os

import pygame
from pygame.locals import *

from globs import *
import mainmenu
import button
import selection
import battle
import fighter
 
class Control:
    def __init__(self):
        self._running = True
        self.state = "MAINMENU"
        pygame.mixer.music.load(os.path.join('Audio', 'bg.ogg'))
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        
        self.myclock = pygame.time.Clock()
        pygame.key.set_repeat(1, 30)

        self.Mainmenu = mainmenu.Mainmenu()
        self.Selection = selection.Selection()
        self.Battlescreen = battle.Battlescreen()

    def control_events(self) :
        for event in pygame.event.get():
            self.on_event(event)
            if self.state == "MAINMENU":
                self.Mainmenu.mainmenu_event(event)
            elif self.state == "SELECTION":
                self.Selection.selection_event(event)
            elif self.state == "BATTLESCREEN":
                self.Battlescreen.battlescreen_event(event)
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    def quit_game(self):
        pygame.quit()
 
    def on_execute(self):
        while(self._running):
            self.control_events()
            if self.state == "MAINMENU":
                self.Mainmenu.update(SURFACE)
                if self.Mainmenu.done:
                    self.Selection.mode = self.Mainmenu.mode
                    self.state = "SELECTION"
            elif self.state == "SELECTION":
                self.Selection.update(SURFACE)
                if self.Selection.mode == "CPU" and self.Selection.p1_done or self.Selection.p1_done and self.Selection.p2_done:
                    self.Selection.done = True
                    pygame.mixer.music.stop()
                if self.Selection.done:
                    self.state = "LOADING"
            elif self.state == "LOADING":
                pygame.mixer.music.load(os.path.join('Audio', 'battle_theme.ogg'))
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play(-1)
                self.Battlescreen.getPlayer1().setFighter(self.Selection.p1_selection)
                if self.Selection.mode == "HUMAN":
                    self.Battlescreen.getPlayer2().setFighter(self.Selection.p2_selection)
                self.Battlescreen.mode = self.Selection.mode
                self.state = "BATTLESCREEN"
            elif self.state == "BATTLESCREEN":
                self.Battlescreen.update(SURFACE)
                if self.Battlescreen.done:
                    self.state = "GAMEOVER"
                    self.winner = self.Battlescreen.winner
            elif self.state == "GAMEOVER":
                pygame.font.init()
                thefont = pygame.font.Font(os.path.join("graphics", "ArialNb.TTF"), 40)
                word = thefont.render("The winner is " + self.winner + "!!!", 1, (0,0,255))
                SURFACE.blit(word, (350, 300))
            self.myclock.tick(FPS)
            pygame.display.update()
        self.quit_game()
 
if __name__ == "__main__" :
    Starter = Control()
    Starter.on_execute()
