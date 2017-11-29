# -*- coding: utf-8 -*-
"""
Created on Mon May  8 21:09:09 2017

@author: Leszek
"""

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
