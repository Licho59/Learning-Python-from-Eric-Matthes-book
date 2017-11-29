# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:18:35 2017

@author: Leszek
"""

#Lista w słowniku
pizza = {
         'crust': 'grubym',
         'toppings': ['pieczarki', 'podwojny ser'],
        } #przechowywanie info o pizzy zamawianej przez klienta

#Podsumowanie zamowienia
print("Zamowiłes pizzę na " + pizza['crust'] + " ciescie" +
      " wraz z następującymi dodatkami:")
for topping in pizza['toppings']:
    print("\t" + topping)

#Ulubione języki programowania
favorite_languages = {
    'janek': ['python', 'ruby'],
    'sara': ['c'],
    'edward': ['ruby', 'go'],
    'paweł': ['python', 'haskel'],
    }
for name,languages in favorite_languages.items(): 
    if len(languages) == 1:
        print("\nUlubiony język programowania użytkownika " +
              name.title() +
               " to " + languages[0].title() + ".")
    else:
        print("\nUlubione języki programowania użytkownika " +
              name.title() + " to:")
        for language in languages:
            print("\t" + language.title())