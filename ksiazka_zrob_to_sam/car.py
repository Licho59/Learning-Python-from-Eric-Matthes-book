# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:05:49 2017

@author: Leszek
"""
"""Klasa, ktora będzie używana do zaprezentowania samochodu."""

class Car():
    """Prosta proba zaprezentowania samochodu."""   
    
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow opisujących samochod."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """Wyswietla informację o przebiegu samochodu."""
        print("Ten samochod ma przejechane " + str(self.odometer_reading) +
              " km.")
        
    def update_odometer(self, mileage):
        """Przypisanie podanej wartosci licznikowi przebiegu.
        Zmiana zostanie odrzucona w przypadku proby cofnięcia licznika.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofnąć licznika przebiegu!") 
    
    def increment_odometer(self, kilometers):
        """Inkrementacja wartosci licznika przebiegu samochodu o
        podaną wartosć."""
        self.odometer_reading += kilometers
        
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
        