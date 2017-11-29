# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:49:31 2017

@author: Leszek
"""
# Głowny kod gry.

import pygame  #moduł zawiera funckcjonalnosć niezbędną dla przygotowania gry

from pygame.sprite import Group

from my_settings import Settings #klasa przechowujaca wszystkie ustawienia gry

from my_ship import Ship #klasa zarządzająca zachowaniem statku

import my_game_functions as gf  #moduł z kodem reagującym na sygnały klawiat/myszy

def run_game():
    # Inicjalizacja gry i utworzenie obiektu ekranu.
   
    pygame.init()   #inicjuje bibliotekę i tworzy okno gry
    ai_settings = Settings() #obiekt klasy Settings
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Kolejna inwazja obcych")
   
    #Utworzenie statku kosmicznego.
    ship = Ship(ai_settings, screen)
    
    # Utworzenie grupy przeznaczonej do przechowywania pociskow.
    bullets = Group()
    
    #Rozpoczęcie pętli głownej gry - pętli zdarzeń oraz uaktualnienie ekranu.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) #poszczeg. zdarze-
        ship.update()                           #-nia wywołane myszą/klawiaturą
        gf. update_bullets(ai_settings, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
            
run_game()