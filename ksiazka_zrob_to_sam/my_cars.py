# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:48:13 2017

@author: Leszek
"""
# Import obu modułow dla tworzenia samochodow obu klas
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())