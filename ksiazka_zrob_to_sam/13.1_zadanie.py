# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 14:11:09 2017

@author: Leszek
"""

# Gwiazdy
import sys
import pygame
from pygame.sprite import *
   
pygame.init()
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Sky full of stars')
bg_color = (50, 50, 250)


my_star = pygame.image.load('images/star.bmp')
rect = my_star.get_rect()
screen_rect = screen.get_rect()
# umieszczenie pojedynczego obiektu gwiazdy w okolicach gornego rogu ekranu 
rect.x = rect.width
rect.y = rect.height
# ustalenie liczby gwiazd w rzędzie i liczby kolumn
my_star_width = rect.width
available_space_x = screen_size[0] - 2 * my_star_width
number_stars_x = int(available_space_x / (2 * my_star_width)) 
stars = []
for n in range(number_stars_x):
    rect.x = 2* rect.x * n
    stars.pygame.draw.rect(screen, rect.x, rect.y, rect.width, rect.height)                               
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)
    screen.blit(my_star, rect) # wyswietlenie gwiazdy na ekranie
    pygame.display.flip() #wyswietlenie ostatnio odswieżonego ekranu