import pygame
import random
import math

from globs import *

class Fighter:
    def __init__(self):
        pygame.init()
        self.currentImage = None
        self.character = None
        self.done = False
        self.x = 0
        self.y = 0
        self.HP = 100
        self.CHARGE = 0
        self.y_offset = 0
        self.x_offset = 0
        self.player = None
        self.rect = None

        self.i = 0
        
        self.state = "STAND"
        self.stateFrame = 0
        self.facing = None
        self.attack = None
        self.attack_type = None
        self.moving = None
        self.animating = False
        self.blocking = True
        self.hit = False

    def create(self, player):
        if player == "player1":
            self.x = 45
            self.y = 377
            self.player = 1
            self.facing = "RIGHT"
        elif player == "player2":
            self.x = 870
            self.y = 377
            self.player = 2
            self.facing = "LEFT"
        self.currentImage = GFX_ZEKE["stand0"]

    def update(self, Surf):
        if not self.hit:
            if self.state != "ATTACK":
                self.updateAnimation()
            else:
                self.updateAttackAnimation()
            if self.state == "JUMP":
                self.jump()
        else:
            self.updateHitAnimation()
        Surf.blit(self.currentImage, (self.x+self.x_offset,self.y+self.y_offset))

    def fighter_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state != "CROUCH" and self.state != "ATTACK" and not self.hit:
                if self.player == 1:
                    if event.key == pygame.K_w:
                        self.state = "JUMP"
                    if event.key == pygame.K_s:
                        pass
                    if event.key == pygame.K_a:
                        pass
                    if event.key == pygame.K_d:
                        pass
                    if event.key == pygame.K_g:
                        pass
                    if event.key == pygame.K_h:
                        pass
                elif self.player == 2:
                    if event.key == pygame.K_UP:
                        self.state = "JUMP"
                    if event.key == pygame.K_DOWN:
                        pass
                    if event.key == pygame.K_LEFT:
                        pass
                    if event.key == pygame.K_RIGHT:
                        pass
                    if event.key == pygame.K_KP1:
                        pass
                    if event.key == pygame.K_KP2:
                        pass
        if event.type == pygame.KEYUP:
            if self.player == 1:
                if event.key == pygame.K_s and self.state != "JUMP" and self.state != "ATTACK" and not self.hit:
                    self.state = "STAND"
                    self.y_offset = 0
            elif self.player == 2:
                if event.key == pygame.K_DOWN and self.state != "JUMP" and self.state != "ATTACK" and not self.hit:
                    self.state = "STAND"
                    self.y_offset = 0

    def updateAnimation(self):
        if self.animating == True:
            if self.character == "ZEKE":
                if self.state == "STAND":
                    if self.stateFrame >= 0 and self.stateFrame < 12:
                        self.currentImage = GFX_ZEKE["stand0"]
                    elif self.stateFrame >= 12 and self.stateFrame < 24:
                        self.currentImage = GFX_ZEKE["stand1"]
                    elif self.stateFrame >= 24 and self.stateFrame < 36:
                        self.currentImage = GFX_ZEKE["stand2"]
                    elif self.stateFrame >= 36 and self.stateFrame < 48:
                        self.currentImage = GFX_ZEKE["stand3"]
                    elif self.stateFrame >= 48 and self.stateFrame < 60:
                        self.currentImage = GFX_ZEKE["stand4"]
                    else:
                        self.stateFrame = 0
                        self.updateAnimation()
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                elif self.state == "WALK":
                    if self.stateFrame >= 0 and self.stateFrame < 12:
                        self.currentImage = GFX_ZEKE["walk0"]
                    elif self.stateFrame >= 12 and self.stateFrame < 24:
                        self.currentImage = GFX_ZEKE["walk1"]
                    elif self.stateFrame >= 24 and self.stateFrame < 36:
                        self.currentImage = GFX_ZEKE["walk2"]
                    elif self.stateFrame >= 36 and self.stateFrame < 48:
                        self.currentImage = GFX_ZEKE["walk3"]
                    else:
                        self.stateFrame = 0
                        self.updateAnimation()
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                elif self.state == "JUMP":
                    self.currentImage = GFX_ZEKE["jump0"]
                elif self.state == "CROUCH":
                    self.currentImage = GFX_ZEKE["crouch0"]
            if self.facing == "RIGHT":
                self.currentImage = pygame.transform.flip(self.currentImage, True, False)
            self.stateFrame += 1

    def updateAttackAnimation(self):
        if self.animating == True:
            if self.character == "ZEKE":
                if self.attack_type == "LOW1":
                    if self.stateFrame >= 0 and self.stateFrame < 8:
                        self.currentImage = GFX_ZEKE["low0_0"]
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 8 and self.stateFrame < 15:
                        self.currentImage = GFX_ZEKE["low0_1"]
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 15 and self.stateFrame < 24:
                        self.currentImage = GFX_ZEKE["low0_2"]
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 24 and self.stateFrame < 33:
                        self.currentImage = GFX_ZEKE["low0_3"]
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    else:
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(GFX_ZEKE["stand0"], True, False)
                        else:
                            self.currentImage = GFX_ZEKE["stand0"]
                        self.stateFrame = 0
                        self.state = "STAND"
                        self.attack_type = None
                        self.x_offset = 0
                        if self.facing == "RIGHT":
                            self.x += 12
                        else:
                            self.x -= 12
                elif self.attack_type == "HIGH1":
                    if self.stateFrame >= 0 and self.stateFrame < 8:
                        self.currentImage = GFX_ZEKE["high0_0"]
                        if self.facing == "LEFT":
                            self.x_offset = -132
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 8 and self.stateFrame < 16:
                        self.currentImage = GFX_ZEKE["high0_1"]
                        if self.facing == "LEFT":
                            self.x_offset = -114
                            self.x -= 2
                        if self.facing == "RIGHT":
                            self.x += 2
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 16 and self.stateFrame < 21:
                        self.currentImage = GFX_ZEKE["high0_2"]
                        self.y_offset = -49
                        if self.facing == "LEFT":
                            self.x_offset = -128
                            self.x -= 4
                        if self.facing == "RIGHT":
                            self.x += 4
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 21 and self.stateFrame < 29:
                        self.currentImage = GFX_ZEKE["high0_3"]
                        if self.facing == "LEFT":
                            self.x_offset = -127
                            self.x -= 3
                        self.y_offset = -34
                        if self.facing == "RIGHT":
                            self.x += 3
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    elif self.stateFrame >= 29 and self.stateFrame < 38:
                        self.currentImage = GFX_ZEKE["high0_4"]
                        self.y_offset = 0
                        if self.facing == "LEFT":
                            self.x_offset = -132
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                    else:
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(GFX_ZEKE["stand0"], True, False)
                        else:
                            self.currentImage = GFX_ZEKE["stand0"]
                        self.stateFrame = 0
                        self.state = "STAND"
                        self.attack_type = None
                        self.x_offset = 0
            self.stateFrame += 1

    def updateHitAnimation(self):
        if self.character == "ZEKE":
            if not self.blocking:
                if self.attack_type == "GROUND":
                    if self.stateFrame <= 40:
                        self.currentImage = GFX_ZEKE["hit0_ground"]
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                            self.currentImage = pygame.transform.rotate(self.currentImage, self.stateFrame)
                            if self.x > 100:
                                self.x -= random.randint(0,3)
                        else:
                            self.currentImage = pygame.transform.rotate(self.currentImage, (0-self.stateFrame))
                            if self.x < 850:
                                self.x += random.randint(0,3)
                    else:
                        self.hit = False
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(GFX_ZEKE["stand0"], True, False)
                        else:
                            self.currentImage = GFX_ZEKE["stand0"]
                        self.stateFrame = 0
                        self.state = "STAND"
                        self.attack_type = None
                elif self.attack_type == "COUNTER":
                    if self.stateFrame <= 40 or self.y+self.y_offset < 408:
                        self.currentImage = GFX_ZEKE["hit0_counter"]
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(self.currentImage, True, False)
                            if self.stateFrame <= 36:
                                self.currentImage = pygame.transform.rotate(self.currentImage, int(2.5*self.stateFrame))
                            else:
                                self.currentImage = pygame.transform.rotate(self.currentImage, 90)
                            if self.x+self.x_offset > 100:
                                self.x_offset -= random.randint(1,3)
                        else:
                            if self.stateFrame <= 36:
                                self.currentImage = pygame.transform.rotate(self.currentImage, int((0-2.5*self.stateFrame)))
                            else:
                                self.currentImage = pygame.transform.rotate(self.currentImage, -90)
                            if self.x+self.x_offset < 850:
                                self.x_offset += random.randint(1,3)
                        if self.y+self.y_offset <= 408:
                            self.y_offset = 0.2*(self.i-5)**2
                            self.i += 1
                    else:
                        self.hit = False
                        self.y = 377
                        self.y_offset = 0
                        self.i = 0
                        self.x = self.x+self.x_offset
                        self.x_offset = 0
                        if self.facing == "RIGHT":
                            self.currentImage = pygame.transform.flip(GFX_ZEKE["stand0"], True, False)
                        else:
                            self.currentImage = GFX_ZEKE["stand0"]
                        self.stateFrame = 0
                        self.state = "STAND"
                        self.attack_type = None
            self.stateFrame += 1
                        
            

    def setFighter(self, character):
        self.character = character
        self.animating = True

    def animateJump(self):
        self.y = 377-((-0.032)*(((self.i)-50)**2)+80)
        if self.moving == "RIGHT":
            self.x += 1
        elif self.moving == "LEFT":
            self.x -= 1
        self.i += 2

    def jump(self):
        if self.state != "ATTACK" and not self.hit:
            if self.i == 102:
                self.i = 0
                self.state = "STAND"
                self.y = 377
            else:
                self.animateJump()

    def low_attack(self):
        if self.state != "JUMP" and self.state != "CROUCH" and self.attack_type == None:
            self.state = "ATTACK"
            self.attack_type = "LOW1"
            self.stateFrame = 0
            if self.facing == "LEFT":
                self.x_offset = -157

    def high_attack(self):
        if self.state != "JUMP" and self.state != "CROUCH" and self.attack_type == None:
            self.state = "ATTACK"
            self.attack_type = "HIGH1"
            self.stateFrame = 0
            self.x_offset = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getY_offset(self):
        return self.y_offset

    def getX_offset(self):
        return self.x_offset

    def getStateFrame(self):
        return self.stateFrame

    def getHP(self):
        return self.HP

    def getState(self):
        return self.state

    def getCharacter(self):
        return self.character

    def getAttack_type(self):
        return self.attack_type

    def getFacing(self):
        return self.facing

    def getBlocking(self):
        return self.blocking

    def getHit(self):
        return self.hit

    def setState(self, status):
        self.state = status

    def setMoving(self, status):
        self.moving = status

    def setBlock(self, boolean):
        self.blocking = boolean

    def setFacing(self, status):
        self.facing = status

    def toggleBlock(self):
        if self.blocking == True:
            self.blocking = False
        else:
            self.blocking = True

    def changeX(self, value):
        self.x += value

    def setY_offset(self, value):
        self.y_offset = value

    def setX_offset(self, value):
        self.x_offset = value

    def hit_by(self, atk_type, character):
        if self.state == "ATTACK" or self.getY() < 377:
            self.i = 0
            self.attack_type = "COUNTER"
        else:
            self.attack_type = "GROUND"
        if character == "ZEKE":
            if atk_type == "LOW1":
                self.drainHP(8)
            elif atk_type == "HIGH1":
                self.drainHP(12)
        self.hit = True
        self.stateFrame = 0

    def drainHP(self, amount):
        if self.attack_type == "COUNTER":
            self.HP -= 2*amount
        else:
            self.HP -= amount
