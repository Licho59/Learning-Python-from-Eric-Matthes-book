# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:29:04 2017

@author: Leszek
"""

# zadanie 12.4 - Klawisze

import pygame, sys
from pygame.locals import *

pygame.init()

bg_color = (100, 200, 100)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Klawisze')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(chr(event.key))
            
    screen.fill(bg_color)
    pygame.display.flip()
    