# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:54:20 2017

@author: Leszek
"""
# Kod odpowiedzialny za zarządzanie zdarzeniami - 'game_functions.py'
import pygame, sys

from my_bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''Reakcja na nacisnięcie klawisza.'''
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def fire_bullet(ai_settings, screen, ship, bullets):
    '''Wystrzelenie pocisku, jeżeli nie przekroczono ustalonego limitu.'''
    # Utworzenie nowego pocisku i dodanie go do grupy pociskow.
    if  len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    '''Reakcja na zwolnienie klawisza.'''
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    
def check_events(ai_settings, screen, ship, bullets):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(ai_settings, screen, ship, bullets):
    """Uaktualnienie obrazow na ekranie i przejscie do nowego ekranu."""
    #Odswieżenie ekranu w trakcie każdej iteracji pętli.
    screen.fill(ai_settings.bg_color)
    # Ponowne wyswietlenie wszystkich pociskow pod warstwami statku kosmicznego
    # i obcych.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    
    #Wyswietlenie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()
    
def update_bullets(ai_settings, screen, bullets):
    '''Uaktualnienie położenia pociskow i usunięcie tych niewidocznych
    na ekranie.'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width:
            bullets.remove(bullet)
        