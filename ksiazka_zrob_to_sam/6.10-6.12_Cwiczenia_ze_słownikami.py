# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:57:46 2017

@author: Leszek
"""

#6.10 Ulubione liczby

ulubione_liczby = {
                   'krysia': '20',
                   'kuba': '28',
                   'leszek': '03',
                   'marzena': '20',
                   'basia': '23'
                   }
print("\n", ulubione_liczby)

ulubione_liczby['krysia'] = ['20', '05', '1959']
ulubione_liczby['kuba'] = ['28', '10', '1990']
ulubione_liczby['leszek'] = ['03', '02', '1959']
ulubione_liczby['marzena'] = ['20', '08', '1980']
ulubione_liczby['basia'] = ['23', '09', '1960']

for person in ulubione_liczby:
    print("\t" + person.title())
for person, liczby in ulubione_liczby.items():
        print("\nUlubione liczby użytkownika " +
          person.title() + " to:" + str(liczby))
for liczby in ulubione_liczby.values():
    print("\n", liczby)
    
#6.11 Miasta
cities = {
          'london': {'country': 'great_britain',
                     'population': '12 mln',
                     'fact': 'big ben'},
          'warsaw': {'country': 'poland',
                     'population': '1,5 mln',
                     'fact': 'powstanie warszawskie'},
          'rome': {'country': 'italy',
                   'population': '8 mln',
                   'fact': 'roman imperium'}
                   }
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print("\nMain information about " + city.title() +
          " are below:")
    print("\tThe country name: " + country.title())
    print("\tThe population of the city: " + population + " people")
    print("\tThe interesting fact or place in the city: " +
          fact.title())
    

    