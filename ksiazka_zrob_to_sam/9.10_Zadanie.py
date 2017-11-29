# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:05:36 2017

@author: Leszek
"""

# 9.10 Zaimportowana klasa Restaurant

from restaurant import Restaurant

moja_knajpa = Restaurant('switezianka', 'polskie jadło')
moja_knajpa.describe_restaurant()
print("Liczba obsłużonych to " + str(moja_knajpa.number_served))

