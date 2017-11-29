# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 12:22:44 2017

@author: Leszek
"""

#6.7 Osoby
znajomy_0 = {
           'first_name': 'darek',
           'last_name': 'rybarczyk',
           'age': '48',
           'city': 'belchatow',
           }
znajomy_1 = {
             'first_name': 'janek',
             'last_name': 'skorodecki',
             'age': '60',
             'city': 'cisza',
             }
znajomy_2 = {
             'first_name': 'urszula',
             'last_name': 'sujecka',
             'age': '47',
             'city': 'belchatow',
             }
people = [znajomy_0, znajomy_1, znajomy_2]

print("\nDane moich znajomych:")
for znajomy in people:
    f = znajomy['first_name'].title()
    l = znajomy['last_name'].title()
    full_name = f + " " + l  
    age = znajomy['age']
    city = znajomy['city']
    print("\n\tImię i nazwisko: " + full_name.title())
    print("\tWiek: " + age)
    print("\tMiasto: " + city.title())
    
#6.8 Zwierzęta
elephant = {
             'animal': 'słoń',
             'age': '12',
             'weight': '2300',
             'owner': 'janek skorodecki',
            }
horse = {
         'animal': 'koń',
         'age': '7',
         'weight': '450',
         'owner': 'michalina wisłocka',
         }
parrot = {
          'animal': 'papuga',
          'age': '33',
          'weight': '2,5',
          'owner': 'maja krasowska',
          }
pets = [elephant, horse, parrot]

print("\nDane zwierząt:")
for pet in pets:
    print("\n\tGatunek zwierzęcia: " + pet['animal'])
    print("\tWiek: " + pet['age'] + " lat")
    print("\tWaga: " + pet['weight'] + " kg")
    print("\tWłasciciel: " + pet['owner'].title())

#6.9 Ulubione miejsca
favorite_places = {
                   'krysia': ['madryt', 'londyn', 'czeladź'],
                   'leszek': ['rzym', 'walencja', 'melbourne'], 
                   'monika': ['krakow', 'florencja', 'lizbona'],
                   }
print("\nNasze ulubione miejsca:")
for name, places in favorite_places.items():
    print("\n\tThe best place for " + name.title() + ":")
    for place in places:
        print("\t" + place.title())