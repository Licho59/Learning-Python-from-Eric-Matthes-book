# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:54:03 2017

@author: Leszek
"""
# 9.6 Budka z lodami
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
        
class IceCreamStand(Restaurant):
    """Przedstawia cechy charakterystyczne budki z lodami."""
    
    def __init__(self, name, cuisine, flavors):
        """Inicjalizacja atrybutow klasy nadrzędnej."""
        super().__init__(name, cuisine)
        self.flavors = flavors
        
    def list_of_flavors(self):
        """Wyswietla listę dostępnych smakow lodow."""
        print("Dostępne smaki lodow to:")
        for icecream in self.flavors:
            print(icecream.title())
                           
my_icecream = IceCreamStand('zielona budka', 'lody', ['malinowe', 'smietankowe', 'bakaliowe',
                           'czekoladowe', 'mieszane'])
my_icecream.list_of_flavors()


                           
        
