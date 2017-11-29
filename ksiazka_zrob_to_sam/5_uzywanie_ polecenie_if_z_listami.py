# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:31:28 2017

@author: Leszek
"""

#Połączenie poleceń if z listami
requested_toppings = ['pieczarki', 'boczek', 'podwojny ser']
for requested_topping in requested_toppings:
    print("Dodaję " + requested_topping + ".")
print("\nTwoja pizza jest gotowa.")

requested_toppings = ['pieczarki', 'boczek', 'podwojny ser']
for requested_topping in requested_toppings:
    if requested_topping == 'boczek':
        print("Przepraszamy, ale obecnie nie mamy boczku.")
    else:
        print("Dodaję " + requested_topping + ".")
print("\nTwoja pizza jest gotowa.")

#Sprawdzanie czy lista nie jest pusta
requested_toppings = []
if requested_toppings: #sprawdza czy lista ma elementy-True, jesli nie- False
    for requested_topping in requested_toppings:
        print("Dodaję " + requested_topping + ".")
    print("\nTwoja pizza jest gotowa.")
else:
    print("\nCzy jestes pewien że chcesz pizzę bez dodatkow?")
    
#Użycie wielu list
available_toppings = ['pieczarki', 'oliwki', 'boczek', 'pepperoni', 'ananas',
                      'podwojny ser'] #możliwe użycie krotki ()
requested_toppings = ['pieczarki', 'frytki', 'podwojny ser']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Dodaję " + requested_topping + ".")
    else:
        print("Przepraszamy, ale obecnie niem mamy dodatku " + requested_topping + ".")
print("\nTwoja pizza jest gotowa!")
        