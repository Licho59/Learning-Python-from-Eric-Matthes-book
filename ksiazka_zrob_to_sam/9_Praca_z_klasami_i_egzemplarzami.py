# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 22:49:43 2017

@author: Leszek
"""

# Klasa Car
class Car():
    """Prosta proba zaprezentowania samochodu."""
    
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow opisujących samochod."""
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
my_new_car = Car('audi', 'a4', 2016)

print("\n" + my_new_car.get_descriptive_name())

# Przypisanie atrybutowi wartosci domyslnej
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
        
my_new_car = Car('audi', 'a4', 2016)

print("\n" + my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Bezposrednia modyfikacja wartosci atrybutu
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
    
my_new_car = Car('audi', 'a4', 2016)
print("\n" + my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modyfikacja wartosci atrybutu za pomocą metody
class Car():
    """Prosta proba zaprezentowania samochodu."""   
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutow opisujących samochod."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 20
        
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
        
            
my_new_car = Car('audi', 'a4', 2016)
print("\n" + my_new_car.get_descriptive_name())

my_new_car.update_odometer(15)
my_new_car.read_odometer()

# Inkrementacja wartosci atrybutu za pomocą metody
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
        
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
      