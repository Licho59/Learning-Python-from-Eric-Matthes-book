# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:12:33 2017

@author: Leszek
"""
# Testowanie funkcji - przygotowanie kodu zawierającego funkcję.
from name_function import get_formatted_name

print("Wpisz 'q', aby zakończyć działanie programu.")
while True:
    first = input("\nPodaj imię: ")
    if first == 'q':
        break
    last = input("\nPodaj nazwisko: ")
    if last == 'q':
        break
    
    formatted_name = get_formatted_name(first, last)
    print("\tElegancko sformatowane pełne imię i nazwisko: " +
          formatted_name + '.')