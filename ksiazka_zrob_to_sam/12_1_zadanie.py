# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:03:20 2017

@author: Leszek
"""

# Niebieskie okno
import pygame, sys
from pygame.locals import *
from player import Player

pygame.init()

bg_color = (100, 000, 200)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Niebieskie okno')
player = Player(screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(bg_color)
    player.blitme()
    pygame.display.flip()