
import pygame, random, math, time, sys, os
from pygame.locals import * 

import imgs

w = 640 
h = 480


WALL_HEIGHT = 3

window = pygame.display.set_mode((w + WALL_HEIGHT*2 + 378,h + WALL_HEIGHT*2)) 
screen = pygame.display.get_surface() 
background = pygame.Surface(screen.get_size()).convert()


def init():
    background.fill((255, 255, 255))

    pygame.display.set_caption("nxtemu")
    #background.blit(pygame.image.load("./icons/brick.jpg").convert(), (640, 0))
    background.blit(imgs.brick.convert(), (640, 0))

    pygame.draw.rect(background, pygame.Color("gray"), ((0, 0), (646, 486)))
    pygame.draw.rect(background, pygame.Color("white"), ((3, 3), (640, 480)))



