# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:34:02 2017

@author: Leszek
"""
import pygame

class Player():
    '''Klasa wyswietlająca postać gracza.'''
    
    def __init__(self, screen):
        '''Inicjalizacja postaci gracza oraz jego położenia na ekranie'''
        self.screen = screen
        
        # wczytanie obrazu postaci gracza i pobranie jego prostokąta
        self.image = pygame.image.load('images/player.bmp')
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # umieszczenie gracza na srodku ekranu
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
    def blitme(self):
        '''Wyswietlenie gracza w jego aktualnym położeniu.'''
        self.screen.blit(self.image, self.rect)
        
