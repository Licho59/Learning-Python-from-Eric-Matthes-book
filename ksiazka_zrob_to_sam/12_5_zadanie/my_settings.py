# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 20:55:29 2017

@author: Leszek
"""
# Przygotowanie modułu dla usatwień gry
class Settings():
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry."""
    
    def __init__(self):
        """Inicjalizacja ustawień gry."""
        #Ustawienia ekranu
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (50, 200, 150)
        
        # Ustawienia dotyczące statku
        self.ship_speed_factor = 1.5
        
        # Ustawienia dotyczące pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        