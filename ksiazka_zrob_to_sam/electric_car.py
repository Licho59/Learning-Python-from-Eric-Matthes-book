# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:40:33 2017

@author: Leszek
"""
"""Zestaw klas przeznaczonych do zaprezentowania
samochodu elektrycznego."""

from car import Car

class Battery():
    """Prosta proba modelowania akumulatora samochodu elektrycznego."""
    
    def __init__(self, battery_size=70):
        """Inicjalizacja atrybutow akumulatora."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Wyswietlenie informacji o wielkosci akumulatora."""
        print("Ten samochod ma akumulator o pojemnosci "
              + str(self.battery_size) + " kWh.")
        
    def get_range(self):
        """Wyswietla informacje o zasięgu samochodu na podstawie
        pojemnosci akumulatora."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "Zasięg tego samochodu wynosi około " + str(range)
        message += " km po pełnym naładowaniu akumulatora."
        print(message)
        
class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
    
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow klasy nadrzędnej.
        Następnie inicjalizacja atrybutow charakterystycznyc dla
        samochodu elektrycznego."""
        super().__init__(make, model, year)
        self.battery = Battery()
