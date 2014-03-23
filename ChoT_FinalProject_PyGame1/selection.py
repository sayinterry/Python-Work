import pygame
import globs
from globs import *

pygame.mixer.init()

class Selection:
    def __init__(self):
        self.back = pygame.transform.scale(GFX["bg-gradiant"], SCREENSIZE)
        self.logo = pygame.transform.scale(GFX["LOGO"], (100, 30))
        self.chooseText = GFX["selectionTEXT"]
        self.selection_area = GFX["selectionBox"]
        self.zeke_thumb = GFX_ZEKE["thumbnail"]
        self.p1_selector = GFX["selection_p1"]
        self.p1_col = 1
        self.p1_row = 1
        self.p1_selection = "ZEKE"
        self.p1_done = False
        self.p1_selected = False
        self.p1_selection_move = False
        self.p2_selector = GFX["selection_p2"]
        self.p2_col = 2
        self.p2_row = 1
        self.p2_selection = None
        self.p2_done = False
        self.p2_selected = False
        self.p2_selection_move = True
        self.done = False
        self.mode = None

    def selection_event(self,event):
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if self.p1_selected == False and self.p1_selection_move == False:
                if event.key == pygame.K_w:
                    if self.p1_row > 1:
                        SFX["select"].set_volume(1)
                        SFX["select"].play()
                        self.p1_row -= 1
                        self.p1_selection = self.get_character(self.p1_col, self.p1_row)
                elif event.key == pygame.K_s:
                    if self.p1_row < 4:
                        SFX["select"].set_volume(1)
                        SFX["select"].play()
                        self.p1_row += 1
                        self.p1_selection = self.get_character(self.p1_col, self.p1_row)
                elif event.key == pygame.K_a:
                    if self.p1_col > 1:
                        SFX["select"].set_volume(1)
                        SFX["select"].play()
                        self.p1_col -= 1
                        self.p1_selection = self.get_character(self.p1_col, self.p1_row)
                elif event.key == pygame.K_d:
                    if self.p1_col < 2:
                        SFX["select"].set_volume(1)
                        SFX["select"].play()
                        self.p1_col += 1
                        self.p1_selection = self.get_character(self.p1_col, self.p1_row)
                elif event.key == pygame.K_g:
                    if self.p1_selection != None:
                        SFX["button_pressed"].set_volume(1)
                        SFX["button_pressed"].play()
                        self.p1_selected = True
                        self.character_selected(self.p1_selection, "player1")
                if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                    self.p1_selection_move = True
            if self.mode == "HUMAN":
                if self.p2_selected == False and self.p2_selection_move == False:
                    if event.key == pygame.K_UP:
                        if self.p2_row > 1:
                            SFX["select"].set_volume(1)
                            SFX["select"].play()
                            self.p2_row -= 1
                            self.p2_selection = self.get_character(self.p2_col, self.p2_row)
                    elif event.key == pygame.K_DOWN:
                        if self.p2_row < 4:
                            SFX["select"].set_volume(1)
                            SFX["select"].play()
                            self.p2_row += 1
                            self.p2_selection = self.get_character(self.p2_col, self.p2_row)
                    elif event.key == pygame.K_LEFT:
                        if self.p2_col > 1:
                            SFX["select"].set_volume(1)
                            SFX["select"].play()
                            self.p2_col -= 1
                            self.p2_selection = self.get_character(self.p2_col, self.p2_row)
                    elif event.key == pygame.K_RIGHT:
                        if self.p2_col < 2:
                            SFX["select"].set_volume(1)
                            SFX["select"].play()
                            self.p2_col += 1
                            self.p2_selection = self.get_character(self.p2_col, self.p2_row)
                    elif event.key == pygame.K_KP1:
                        if self.p2_selection != None:
                            SFX["button_pressed"].set_volume(1)
                            SFX["button_pressed"].play()
                            self.p2_selected = True
                            self.character_selected(self.p2_selection, "player2")
                if event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                    self.p2_selection_move = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                self.p1_selection_move = False
            elif event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                self.p2_selection_move = False

    def update(self,Surf):
        Surf.blit(self.back, (0,0))
        Surf.blit(self.logo, (890,560))
        Surf.blit(self.selection_area, (375, 100))
        Surf.blit(self.zeke_thumb, self.getSelection(1,1))
        Surf.blit(self.chooseText, (155, 15))
        if self.mode == "HUMAN":
            Surf.blit(self.p2_selector, self.getSelection(self.p2_col,self.p2_row))
        Surf.blit(self.p1_selector, self.getSelection(self.p1_col,self.p1_row))

    def get_character(self, c, r):
        if c == 1:
            if r == 1:
                return "ZEKE"
            elif r == 2:
                pass
            elif r == 3:
                pass
            elif r == 4:
                pass
        elif c == 2:
            if r == 1:
                pass
            elif r == 2:
                pass
            elif r == 3:
                pass
            elif r == 4:
                pass

    def getSelection(self, c, r):
        x = 273+117*c
        y = -2+117*r
        return (x,y)

    def character_selected(self, name, player):
        if name == "ZEKE":
            some_selection = True
        if some_selection == True:
            if player == "player1":
                self.p1_done = True
            elif player == "player2":
                self.p2_done = True
