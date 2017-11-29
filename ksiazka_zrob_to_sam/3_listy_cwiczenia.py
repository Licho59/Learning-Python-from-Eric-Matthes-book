# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:09:31 2017

@author: Leszek
"""
#ćwiczenia z listami
bicycles = ['trekingowy', 'gorski', 'miejski', 'szosowy']
message = "Moim pierwszym rowerem był rower " + bicycles[1].title() + "."
print(message)
#cwiczenie 3.2
imiona = ['marzena', 'jakub', 'krystyna', 'piotr', 'barbara', 'halina']
message = "Zagraj ze mną w karty "+ imiona[3].title()
print(message)
# cwiczenie 3.3
cars = ['toyota', 'ford', 'audi', 'mercedes',
        'nissan', 'fiat', 'citroen', 'mitsubishi',
        'mazda', 'hyundai', 'renault',
        'volkswagen', 'nissan', 'volvo', 'skoda']
print("My favorite car is "+cars[6].title()+".")
print("My first car is "+cars[-1].title()+".")
print("The most expensive car is "+cars[3].title()+".")

#ćwiczenie z motocycles: dodawanie i usuwanie z listy
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati') #dodawanie do listy
print(motorcycles)

del motorcycles[2] #trwałe usuwanie z listy
print(motorcycles)
last_motorcycle = motorcycles.pop() #metoda pop pozwala użyć element usunięty
print(motorcycles)
print(last_motorcycle)
print("Moj pierwszy motocykl to " + motorcycles.pop(0).title() + ".")
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('ducati')
motorcycles.append('suzuki')
motorcycles.insert(2,'jawa')
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

#metoda remove pozwala użyć usunięty z listy element
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nMotocykl " + too_expensive.title() + " jest zbyt drogi dla mnie.")

#organizacja listy - metoda sort, funkcja sorted, metoda reverse
cars = ['skoda','toyota','mazda','honda', 'fiat', 'bmw', 'audi', 'nissan']
cars.sort() # kolejnosc alfabetyczna
print(cars)
cars.sort(reverse=True) #odwrotna kolejnosc
print(cars)
print(len(cars))

cars = ['skoda','toyota','mazda','honda', 'fiat', 'bmw', 'audi', 'nissan']
print("Oto lista początkowa:")
print(cars)

print("\nOto lista posortowana:")
print(sorted(cars)) #funkcja sorted sortuje tymczasowo
# ale nie zmienia pierwotnej kolejnosci na liscie

print("\nOto ponownie lista początkowa")
print(cars)
print(sorted(cars, reverse=True)) #tymcz. sortowanie z par odwr kolej 
print(cars)

cars.reverse() # metoda reverse trwale odwraca chronologiczny porzadek listy
print(cars)
len(cars) #funkcja ktora podaje długosc listy
