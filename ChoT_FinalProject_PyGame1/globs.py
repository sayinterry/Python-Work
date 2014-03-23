import os
import pygame
import button

FPS = 64.0              #Global frames per second (desired)
SCREENSIZE = (1000,600) #Global screen size
SURFACE = pygame.display.set_mode(SCREENSIZE)
pygame.init()

#Fonts
basicFont = pygame.font.Font(os.path.join('graphics','ArialNb.TTF'),48)
fixedsys  = pygame.font.Font(os.path.join('graphics','Fixedsys500c.ttf'),60)

def getgraphics(directory):
    """Returns a dictionary of all the image files in a directory.
    Dictionary keys are image names minus their file extensions."""
    dirlist = os.listdir(directory)
    graphic = {}
    for graf in dirlist:
        if graf[-3:] in ("png","jpg"):
            graphic[graf[:-4]] = pygame.image.load(os.path.join(directory,graf)).convert_alpha()
    return graphic

def getsounds(directory):
    dirlist = os.listdir(directory)
    sound = {}
    for sds in dirlist:
        if sds[-3:] in ("ogg"):
            sound[sds[:-4]] = pygame.mixer.Sound(os.path.join(directory, sds))
    return sound

SFX = getsounds("Audio")

GFX  = getgraphics("graphics")
GFX_CYNTHIA = getgraphics(os.path.join("graphics", "Cynthia"))
GFX_ZEKE = getgraphics(os.path.join("graphics", "Zeke"))
