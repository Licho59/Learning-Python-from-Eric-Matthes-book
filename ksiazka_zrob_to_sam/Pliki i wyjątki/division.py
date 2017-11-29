# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:44:47 2017

@author: Leszek
"""
# Używanie bloku try-except
try:
    print(5/0)
except:
    print("Nie można dzielić przez zero!")
    
# Używanie wyjątkow w celu uniknięcia awarii programu
print("\nWprowadź dwie liczby, ktore zostaną podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu.")

while True:
    first_number = input("Pierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("Druga liczba: ")
    if second_number == 'q':
        break
    
    answer = int(first_number)/int(second_number)
    print(answer)
    
# Blok else
print("\nWprowadź dwie liczby, ktore zostaną podzielone.")
print("Wpisz 'q', aby zakończyć działanie programu.")

while True:
    first_number = input("Pierwsza liczba: ")
    if first_number == 'q':
        break
    second_number = input("Druga liczba: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("Nie można dzielić przez zero!")
    else:
        print(answer)