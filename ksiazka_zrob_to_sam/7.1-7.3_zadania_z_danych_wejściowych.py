# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:13:31 2017

@author: Leszek
"""

# 7.1 Wypożyczenie samochodu
car_type = input("What type of car\
 would you like to rent? ")
print("\nWait a moment, I need to check if " +
       car_type + " is available.")

# 7.2 Stolik w restauracji
reservation_place = input("How many people\
 would you like to reserve the table for? ")
number = int(reservation_place)

if number >= 8:
    print("\nYou will need to wait for a bigger table!")
else:
    print("\nYour table is ready!\nCome in, please!")

# 7.3 Wielokrotnosć dziesięciu
number = input("Give me any number, please! ")
number = int(number)
if number%10 == 0:
    print("\nThe given number is multiple of 10!")
else:
    print("\n The given number is not multiple of 10.")    