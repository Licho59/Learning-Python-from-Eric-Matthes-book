# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:25:50 2017

@author: Leszek
"""

# Przekazywanie dowolnej liczby argumentow
def make_pizza(*toppings): #argument z gwiazdką oznacza pustą krotkę
    """Wyswietlenie listy dodatkow wybranych przez klienta"""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('pieczarki', 'zielona papryka', 'podwojny ser')

#wersja z iteracją
def make_pizza(*toppings):
    """Podsumowanie informacji o przygotowywanej pizzy."""
    print("\nPrzygotowuję pizzę z następującymi dodatkami:")
    for topping in toppings:
        print("-" + topping)

make_pizza('pepperoni')
make_pizza('pieczarki', 'zielona papryka', 'podwojny ser')

# Argumenty pozycyjne i przekazywanie dowolnej liczby argumentow
def make_pizza(size, *toppings):
    """Podsumowanie informacji o przygotowywanej pizzy."""
    print("\nPrzygotowuję pizzę o wielkosci "
          + str(size) + " cm, z następującymi dodatkami:")
    for topping in toppings:
        print("-" + topping)

make_pizza(40, 'pepperoni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwojny ser')

# Używanie dowolnej liczby argumentow w postaci słow kluczowych
def build_profile(first, last, **user_info): 
            # ** - oznacza utworzenie pustego słownika
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location = 'princetown',
                             field = 'fizyka')
print(user_profile)