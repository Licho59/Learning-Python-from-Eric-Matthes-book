# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:38:28 2017

@author: Leszek
"""
# 10.7 Kalkulator dodawania
print("Adding numbers.")
print("Put a 'q' to finish.")

while True:
    x = input("Give me a number: ")
    if x == 'q':
        print("Thank you for using our calculator!")
        break
    try:
        x = int(x)
        y = input("Give me a number: ")
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number")
    
    else:
        sum = x + y
        print("The sum of " + str(x) + " and " + str(y) + " is " +
              str(sum) + ".")
        
# Rozwiązanie wg książki
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x =input("Give me a number: ")
        if x == 'q':
            break
        x = int(x)
    
        y = input("Give me another number: ")
        if y == 'q':
            break
        y = int(y)
    except ValueError:
        print("Sorry, I really needed a number.")
        
    else:
        sum = x + y
        print("\nThe sum of " + str(x) + " and " + str(y) + " is " +
              str(sum) + ".")
        