# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:34:02 2017

@author: Leszek
"""
import pygame

class Rocket():
    '''Klasa wyswietlająca obraz rakiety.'''
    
    def __init__(self, screen):
        '''Inicjalizacja obrazu rakiety oraz jej położenia na ekranie'''
        self.screen = screen
        
        # wczytanie obrazu postaci gracza i pobranie jego prostokąta
        self.image = pygame.image.load('images/rocket.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # umieszczenie rakiety na srodku ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
        # Opcje wskazujące na poruszanie się rakiety
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    
    def update(self):
        '''Uaktualnienie położenia rakiety na podstawie opcji wskazujących
        na jej ruch.'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        
        
    def blitme(self):
        '''Wyswietlenie rakiety w jej aktualnym położeniu.'''
        self.screen.blit(self.image, self.rect)
        
