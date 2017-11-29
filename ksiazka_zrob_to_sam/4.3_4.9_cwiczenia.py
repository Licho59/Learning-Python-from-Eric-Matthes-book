# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 17:52:17 2017

@author: Leszek
"""

#odliczanie do dwudziestu
for number in range(1,21):
    print(number)
    
#Milion... lub trochę mniejsza wartosc
numbers = list(range(1,10**4+1))
for number in numbers:
    print(number)

#Sumowanie do miliona
numbers = list(range(1,10**6+1))
print(min(numbers))
print(max(numbers))
print(sum(numbers)) #Wow - 1 sek na zsumowanie!

#Liczby nieparzyste
nieparzyste = list(range(1,21,2))
for number in nieparzyste:
    print(number)

#Trzy
trzecia_potega = []
for value in range(3,31):
    cube = value**3
    trzecia_potega.append(cube)
print(trzecia_potega)
#lub
trzecia_potega = [cube**3 for cube in range(3,31)]
print(trzecia_potega)

#Szescian
szesciany = []
for n in range(1,10):
    cube = n**3
    szesciany.append(cube)
print(szesciany)

szesciany = []
for n in range(1,10):
    szesciany.append(n**3)
print(szesciany)

#Szescian za pomocą listy składanej
szesciany = [number**3 for number in range(1,11)]
print(szesciany)


