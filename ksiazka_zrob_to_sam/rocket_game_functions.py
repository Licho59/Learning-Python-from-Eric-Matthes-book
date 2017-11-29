# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:54:20 2017

@author: Leszek
"""
# Kod odpowiedzialny za zarządzanie zdarzeniami - 'game_functions.py'
import sys

import pygame

def check_keydown_events(event, rocket):
    '''Reakcja na nacisnięcie klawisza.'''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    if event.key == pygame.K_DOWN:
        rocket.moving_down = True
        
def check_keyup_events(event, rocket):
    '''Reakcja na zwolnienie klawisza.'''
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False
    
def check_events(rocket):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)
            
'''def update_screen(ai_settings, screen, ship):
    """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu."""
    #Odswieżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #Wyswietlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()'''