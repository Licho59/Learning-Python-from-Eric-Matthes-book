# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:50:50 2017

@author: Leszek
"""

# 9.14 Kostki
from random import randint

class Die():
    """Modelowanie kostki do gry."""
    
    def __init__(self, sides=6):
        """Inicjalizacja atrybutu kosci do gry."""
        self.sides = sides
        
    def roll_die(self):
        """Zwraca losowo wybraną liczbę w przedziale od 1 do 'liczba scian'."""
        return randint(1, self.sides)
        
d6 = Die() # tworzy 6 scianową kostkę
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)

print("\n10 rolls of 6-sided die:")    
print(results)

d10 = Die(10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)

print("\n10 rolls of 10-sided die:")    
print(results)


d20 = Die(20)
results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)

print("\n10 rolls of 20-sided die:")    
print(results)

