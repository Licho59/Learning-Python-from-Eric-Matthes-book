# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:53:18 2017

@author: Leszek
"""
#cwiczenia z pętlą for
magicians = ['alicja', 'dawid', 'karolina']
for magician in magicians:
    print(magician.title() + "," + "to była doskonała sztuczka.")
    print("Nie mogę się doczekać Twojej kolejnej sztuczki, " + magician.title() + ".\n")
print("Dziękuję wszystkim. To był naprawdę wspaniały występ!")

pizzas = ['pepperoni', 'hawajska', 'owoce morza', 'margerita']
for pizza in pizzas:
    print("Bardzo lubię pizzę o nazwie " + pizza + ".")
print("\nWszystkie pizze są dobre.")

#tworzenie list liczbowych  - funkcja range()
for value in range(2,8): #range nie obejmuje ostatniego elementu
    print(value)

numbers = list(range(2,8)) #konwersja zbioru liczb na listę
numbers.reverse()
print(numbers)

#lista kwadratow pierwszych 10 liczb
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# wersja kodu jw. zoptymalizowana
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
#wersja kodu optymalna tzw. lista składana
squares = [value**2 for value in range(1,11)]
print(squares)

#proste dane statystyczne
numbers = [2,13,-1,42,1,56,-34,98]
print(min(numbers)) #najmniejsza z listy
print(max(numbers)) #największa z listy
print(sum(numbers)) #suma liczb z listy