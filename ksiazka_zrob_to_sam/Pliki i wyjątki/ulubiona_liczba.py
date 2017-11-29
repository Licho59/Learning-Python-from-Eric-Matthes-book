# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:27:13 2017

@author: Leszek
"""
# Ulubiona liczba - wczytanie danych do pliku
import json

filename = 'favorite_number.json'

num = input("What's your favorite number? ")
with open(filename, 'w') as f_obj:
    json.dump(num, f_obj)
    
# Kod wg książki
import json
                    # bez wiersza dedykowanego - filename = "xxx.json'
number = input("What's your favorite number? ")
with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks, I'll remember that.")
    