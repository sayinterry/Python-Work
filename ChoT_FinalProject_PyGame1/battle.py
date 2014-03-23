import pygame

import fighter
import handler
import healthbar
from globs import *

class Battlescreen:
    def __init__(self):
        self.floor = GFX["map1_floor"]
        self.back = pygame.transform.scale(GFX["bg-gradiant"], SCREENSIZE)
        self.logo = pygame.transform.scale(GFX["LOGO"], (100,30))
        self.done = False
        self.winner = None
        self.mode = None
        self.damage_handler = handler.Handler()
        self.player1 = fighter.Fighter()
        self.player2 = fighter.Fighter()
        self.player1.create("player1")
        self.player2.create("player2")
        self.hbar1 = healthbar.Health(1)
        self.hbar2 = healthbar.Health(2)
        self.winner = None

    def update(self, Surf):
        self.update_player()
        if self.player1.state == "ATTACK":
            self.damage_handler.check(self.player1, self.player2)
        elif self.player2.state == "ATTACK":
            self.damage_handler.check(self.player2, self.player1)
        self.hbar1.updateHP(self.player1.getHP())
        self.hbar2.updateHP(self.player2.getHP())
        if self.done == False:
            if self.player1.getHP() <= 0:
                self.done = True
                self.winner = "Player 2"
            elif self.player2.getHP() <= 0:
                self.done = True
                self.winner = "Player 1"
        Surf.blit(self.back, (0,0))
        Surf.blit(self.floor, (0,420))
        Surf.blit(self.logo, (890, 560))
        self.hbar1.update(Surf)
        self.hbar2.update(Surf)
        self.player1.update(Surf)
        if self.mode == "HUMAN":
            self.player2.update(Surf)

    def update_player(self):
        if self.player1.getState() != "ATTACK" and self.player1.getHit() == False:
            if self.player1.getX() > self.player2.getX():
                self.player1.setFacing("LEFT")
            elif self.player1.getX() < self.player2.getX():
                self.player1.setFacing("RIGHT")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s] and self.player1.getState() != "JUMP":
                self.player1.setState("CROUCH")
                self.player1.setY_offset(36)
            if keys[pygame.K_a] and self.player1.getState() != "CROUCH":
                if self.player1.getFacing() == "RIGHT":
                    #self.player1.setBlock(True)
                    if self.player1.getState() != "JUMP":
                        if self.player1.getX() > 100:
                            self.player1.changeX(-2)
                elif self.player1.getFacing() == "LEFT":
                    self.player1.setBlock(False)
                    if self.player1.getState() != "JUMP":
                        if self.player1.getX() > 100 and (self.player1.getX() - self.player2.getX()) > 100:
                            self.player1.changeX(-3)
                if self.player1.getState() != "JUMP":
                    self.player1.setState("WALK")
                    self.player1.setMoving("LEFT")
            if keys[pygame.K_d] and self.player1.getState() != "CROUCH":
                if self.player1.getFacing() == "LEFT":
                    #self.player1.setBlock(True)
                    if self.player1.getState() != "JUMP":
                        if self.player1.getX() < 850:
                            self.player1.changeX(2)
                elif self.player1.getFacing() == "RIGHT":
                    self.player1.setBlock(False)
                    if self.player1.getState() != "JUMP":
                        if self.player1.getX() < 850  and (self.player2.getX() - self.player1.getX()) > 100:
                            self.player1.changeX(3)
                if self.player1.getState() != "JUMP":
                    self.player1.setState("WALK")
                    self.player1.setMoving("RIGHT")
            if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d] and self.player1.getState() != "JUMP":
                self.player1.setState("STAND")
                self.player1.setMoving(None)
                self.player1.setX_offset(0)
        if self.player2.getState() != "ATTACK" and self.player2.getHit() == False:
            if self.player2.getX() > self.player1.getX():
                self.player2.setFacing("LEFT")
            elif self.player2.getX() < self.player1.getX():
                self.player2.setFacing("RIGHT")
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN] and self.player2.getState() != "JUMP":
                self.player2.setState("CROUCH")
                self.player2.setY_offset(36)
            if keys[pygame.K_LEFT] and self.player2.getState() != "CROUCH":
                if self.player2.getFacing() == "RIGHT":
                    #self.player2.setBlock(True)
                    if self.player2.getState() != "JUMP":
                        if self.player2.getX() > 100:
                            self.player2.changeX(-2)
                elif self.player2.getFacing() == "LEFT":
                    self.player2.setBlock(False)
                    if self.player2.getState() != "JUMP":
                        if self.player2.getX() > 100  and (self.player2.getX() - self.player1.getX()) > 100:
                            self.player2.changeX(-3)
                if self.player2.getState() != "JUMP":
                    self.player2.setState("WALK")
                    self.player2.setMoving("LEFT")
            if keys[pygame.K_RIGHT] and self.player2.getState() != "CROUCH":
                if self.player2.getFacing() == "LEFT":
                    #self.player2.setBlock(True)
                    if self.player2.getState() != "JUMP":
                        if self.player2.getX() < 850:
                            self.player2.changeX(2)
                elif self.player2.getFacing() == "RIGHT":
                    self.player2.setBlock(False)
                    if self.player2.getState() != "JUMP":
                        if self.player2.getX() < 850  and (self.player1.getX() - self.player2.getX()) > 100:
                            self.player2.changeX(3)
                if self.player2.getState() != "JUMP":
                    self.player2.setState("WALK")
                    self.player2.setMoving("RIGHT")
            if not keys[pygame.K_UP] and not keys[pygame.K_LEFT] and not keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT] and self.player2.getState() != "JUMP":
                self.player2.setState("STAND")
                self.player2.setMoving(None)
                self.player2.setX_offset(0)

    def battlescreen_event(self, event):
        self.player1.fighter_event(event)
        if self.mode == "HUMAN":
            self.player2.fighter_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player1.jump()
            elif event.key == pygame.K_a:
                pass
            elif event.key == pygame.K_s:
                pass
            elif event.key == pygame.K_d:
                pass
            elif event.key == pygame.K_g:
                self.player1.low_attack()
            elif event.key == pygame.K_h:
                self.player1.high_attack()
            if event.key == pygame.K_UP:
                self.player2.jump()
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_KP1:
                self.player2.low_attack()
            elif event.key == pygame.K_KP2:
                self.player2.high_attack()

    def getPlayer1(self):
        return self.player1

    def getPlayer2(self):
        return self.player2
