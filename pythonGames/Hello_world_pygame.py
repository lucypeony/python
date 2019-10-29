import pygame, sys
from pygame.locals import *

#set up pygame
pygame.init()

#set up the windows
windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello World!')

#set up the colors
BLACK =(0,0,0)
WHITE = (255,255,255)
RED =(255,0,0)
GREEN =(0,255,0)
BLUE=(0,0,255)

#set up the fonts
basicFont = pygame.font.SysFont(None, 48)

#set up the text
text=basicFont.render('Hello World!',True, WHITE,BLUE)
