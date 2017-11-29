# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:03:20 2017

@author: Leszek
"""

# Latanie rakietą
import pygame, sys
from pygame.locals import *
from rocket import Rocket
import rocket_game_functions as gf

pygame.init()

bg_color = (100, 000, 200)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Rakieta w kosmosie')
rocket = Rocket(screen)

while True:
    gf.check_events(rocket) #poszczegolne zdarzenia wywołane myszą/klawiaturą
    rocket.update()
   # gf.update_screen(screen, rocket)
     
    screen.fill(bg_color)
    rocket.blitme()
    pygame.display.flip()
    
