# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:14:07 2017

@author: Leszek
"""
#funkcja input

message = input("Powiedz mi cos o sobie, a wyswietlę to na ekranie: ")
print(message)

name = input("Podaj mi swoje imię: ")
print("Witaj, " + name.title() + "!")

#Użycie zmiennej dla długiego komunikatu
prompt = "Jeżeli powiesz nam, kim jestes,\
spersonalizujemy wyswietlany komunikat."
prompt += "\nJak masz na imię? "
name = input(prompt)
print("\nWitaj, " + name.title() + "!")

#funkcja int() do akceptowania danych liczbowych
age = input("How old are you? ")
print(int(age))

height = input("How tall are you(in centimeters)? ")
height = int(height)

if height >= 90:
    print("\nYou are enough tall to ride this train.")
else:
    print("\nYou'll be able to ride it when you grow up!")
    
# Operator modulo - jaka reszta z dzielenia
number = input("Put the number to check its parity: ")
number = int(number)

if number%2 == 0:
    print("\nThe given number is an even number.")
else:
    print("\nThe given number is an odd number.")
