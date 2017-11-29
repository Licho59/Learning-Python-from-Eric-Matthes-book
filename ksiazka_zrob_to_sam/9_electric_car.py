# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 19:43:19 2017

@author: Leszek
"""
#Dziedziczenie - klasa nadrzędna i potomna
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
        
class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu elektrycznego."""
    
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow klasy nadrzędnej."""
        super().__init__(make, model, year)
        self.battery_size = 70
        
    def describe_battery(self):
        """Wyswietlenie informacji o wielkosci akumulatora."""
        print("Ten samochod ma akumulator o pojemnosci " +
               str(self.battery_size) + " kWh.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Definiowanie atrybutow i metod dla klasy potomnej - jw.
# Nadpisywanie metod klasy nadrzędnej - po to aby zablokować w klasie
# potomnej nieprzydatną metodę z klasy nadrzędnej, np.
def ElectricCar(Car):
    --cięcie--
    
    def fill_gas_tank():
        """Samochod o napędzie elektrycznym nie ma zbiornika paliwa."""
        print("Ten samochod nie wymaga tankowania paliwa!")     