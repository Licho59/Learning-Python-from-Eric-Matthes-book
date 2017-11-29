# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:39:19 2017

@author: Leszek
"""
# 10.6 Dodawanie - kod rozbudowany w stosunku do zadanego
print("Podaj dwie liczby w celu ich dodania.") 
print("Wprowadź 'q' aby zakończyć działanie programu.") 

while True: 
    first_number = input("Wprowadź pierwszą liczbę: ") 
    second_number = input("Wprowadź drugą liczbę: ") 
    
    if first_number == 'q' or second_number == 'q': 
        print("Wyjście z programu!") 
        break 
    try: 
        suma = float(first_number) + float(second_number)
    except ValueError: 
        print("Jedna z wprowadzonych wielkości nie jest liczbą.") 
        print("Spróbuj jeszcze raz.") 
        continue 
    else: 
        print("Wynik dodawania: " + str(suma))
        
# Prawidłowe rozwiązanie wg książki – Addition
 try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me a number: ")
    y = int(y)

except ValueError:
    print("Sorry, I really needed a number")
    
else:
    sum = x + y
    print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")