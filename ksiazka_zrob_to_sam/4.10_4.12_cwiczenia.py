# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:14:39 2017

@author: Leszek
"""
#Wycinki
my_foods = ['bigos', 'gołąbki', 'pizza', 'mielone']
print("Pierwsze trzy dania mojej listy to:")
for food in my_foods[:3]:
    print(food.title())

my_foods = ['bigos', 'gołąbki', 'pizza', 'mielone']
my_foods.append('rosoł')    
print("Trzy dania w srodku listy to:")
for food in my_foods[1:4]:
    print(food.title())

print("Ostatnie trzy dania mojej listy to:")
for food in my_foods[-3:]:
    print(food.title())
    
#Moja pizza, Twoja pizza
pizzas = ['pepperoni', 'hawajska', 'owoce morza', 'margerita']
friend_pizzas = pizzas[:]
pizzas.append('makaroniarska')
friend_pizzas.append('pospolita')
print("Moje ulubione rodzaje pizzy to:")
for pizza in pizzas:
    print(pizza.title())
print("Ulubione rodzaje pizzy mojego przyjaciela to:")
for pizza in friend_pizzas:
    print(pizza.title())
    

