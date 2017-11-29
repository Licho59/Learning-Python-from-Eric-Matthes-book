# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 21:22:29 2017

@author: Leszek
"""
import pygame  

class Ship():
    """Klasa odpowiedzialna za zarządzanie statkiem kosmicznym."""
    
    def __init__(self, ai_settings, screen): #parametry odnoszą sie do egzemplarza
                                                        # oraz ekranu
        """Inicjalizacja statku kosmicznego i jego położenie początkowe."""
        self.screen = screen
        self.ai_settings = ai_settings
             
        #Wczytywanie obrazu statku kosmicznego i pobranie jego prostokąta.
        self.image = pygame.image.load('my_ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Każdy nowy statek kosmiczny pojawia się po lewej stronie srodka ekranu.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery        
        self.center = float(self.rect.centery)
        
        # Opcje wskazujące na poruszanie się statku
        self.moving_down = False
        self.moving_up = False
        
    def update(self):
        '''Uaktualnienie położenia statku na podstawie opcji wskazujących
        na jego ruch.'''
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor
                
        # Uaktualnienie obiektu rect na podstawie wartosci self.center.
        self.rect.centery = self.center
        
    def blitme(self):
        """Wyswietlenie statku kosmicznego w jego aktualnym położeniu."""
        self.screen.blit(self.image, self.rect)