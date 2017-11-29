# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:01:29 2017

@author: Leszek
"""

class Restaurant():
    """Prosty opis restauracji oraz menu."""
    
    def __init__(self, name, cuisine):
        """Inicjalizacja atrybutow restaurant_name i cuisine_type."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
        """Wyswietla nazwę restauracji oraz rodzaj menu."""
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
        
    def open_restaurant(self, opening, closing):
        """Wyswietla info o godzinach pracy restauracji."""
        print("The restaurant " + self.restaurant_name.title() +
              " is open from " + opening + " to " +
              closing + ".")
    
    def set_number_served(self,clients):
        """Definiuje liczbę obsłużonych klientow."""
        self.number_served = clients
               
    def increment_number_served(self, clients_per_day):
        """Inkrementacja liczby obsłużonych klientow."""
        self.number_served += clients_per_day