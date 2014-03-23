import pygame
import globs

class Button:
    def __init__(self):
        self.state = "plain"
        self.title = None
        self.x = 0
        self.y = 0
        self.done = False
        self.mode = None

    def create_button(self, _image, _image_hover, _image_down, _title, coord):
        self.image = globs.GFX[_image]
        self.image_hover = globs.GFX[_image_hover]
        self.image_down = globs.GFX[_image_down]
        self.title = _title
        self.x = coord[0]
        self.y = coord[1]
        self.width = 250
        self.height = 100
        
    def button_draw(self, Surf):
        if self.state == "plain":
            Surf.blit(self.image, (self.x,self.y))
        elif self.state == "hover":
            Surf.blit(self.image_hover, (self.x,self.y))
        elif self.state == "down":
            Surf.blit(self.image_down, (self.x,self.y))

    def button_event(self,event):
        mpos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if mpos[0] > self.x and mpos[1] > self.y and mpos[0] < self.x+self.width and mpos[1] < self.y+self.height:
                if self.state != "hover" :
                    self.state = "hover"
                    globs.SFX["menu_scroll"].set_volume(0.4)
                    globs.SFX["menu_scroll"].play()
            else:
                self.state = "plain"
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self.state == "hover":
            self.state = "down"
            globs.SFX["button_pressed"].set_volume(0.7)
            globs.SFX["button_pressed"].play()
        elif event.type == pygame.MOUSEBUTTONUP:
            if mpos[0] > self.x and mpos[1] > self.y and mpos[0] < self.x+self.width and mpos[1] < self.y+self.height:
                if self.title == "vsHUMAN":
                    self.mode = "HUMAN"
                elif self.title == "vsCPU":
                    self.mode = "CPU"
                self.done = True
