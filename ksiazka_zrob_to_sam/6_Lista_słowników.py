# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:31:46 2017

@author: Leszek
"""

#Lista słownikow
alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'żołty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}

aliens = [alien_0, alien_1, alien_2] #listę tworzą słowniki opisujące
#poszczegolnych obcych
for alien in aliens:
    print(alien)

#Utworzenie pustej listy przeznaczonej do przechowywania obcych.
aliens = []

#Utworzenie 30 zielonych obcych
for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien)
    
#Wyswietlenie pierwszych pięciu obcych
for alien in aliens[:5]:
    print(alien)
    
print("\nCałkowita liczba obcych: " + str(len(aliens)))

#Zmiana koloru obcego i jego szybkosci
for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żołty'
        alien['speed'] = 'middle'
        alien['points'] = 10

for alien in aliens[0:5]: #Wyswietlenie pierwszych pięciu obcych
    print(alien)
print("\nPowyżej wyswietlono dane pierwszych pięciu obcych.")

