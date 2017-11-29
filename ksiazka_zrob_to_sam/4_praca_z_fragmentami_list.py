# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 19:22:52 2017

@author: Leszek
"""

#Praca z fragmentami list
szesciany = [number**3 for number in range(1,11)]
print(szesciany[2:5])

players = ['karol', 'martyna', 'michał', 'florian', 'ela']
print(players[:3]) #parametr 3 nie jest uwzględniany
print(players[3:])
print(players[-4]) #wywietla 4-ty element od końca
print(players[-4:-1]) #wyswietla od -4 do przedostatniego elem

print("Oto trzech pierwszych graczy naszej drużyny:")
for player in players[:3]:
    print(player.title())

#Kopiowanie listy
my_foods = ['bigos', 'gołąbki', 'pizza', 'mielone']
friend_foods = my_foods[:] #pobranie wycinka daje kopię listy
print("Moje ulubione potrawy to:")
print(my_foods)
print("\nUlubione potrawy mojego przyjaciela to:")
print(friend_foods)

my_foods = ['bigos', 'gołąbki', 'pizza', 'mielone']
friend_foods = my_foods[:]
my_foods.append('grochowa')
friend_foods.append('lody')
print("Moje ulubione potrawy to:")
print(my_foods)
print("\nUlubione potrawy mojego przyjaciela to:")
print(friend_foods)

    

      
      