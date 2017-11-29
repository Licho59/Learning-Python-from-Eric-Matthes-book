# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:38:10 2017

@author: Leszek
"""
# Ulubiona liczba - odczytanie i wyswietlenie danych
import json

filename = 'favorite_number.json'

with open(filename) as f_obj:
    num = json.load(f_obj)
print("Znam Twoją ulubioną liczb, to " + str(num))

# Kod wg książki
import json

with open('favorite_number.json') as f:
    number = json.load(f)

print("I know your favorite number! It's " + str(number))