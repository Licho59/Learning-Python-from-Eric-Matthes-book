# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:48:53 2017

@author: Leszek
"""

def make_pizza(size, *toppings):
    """Podsumowanie informacji o przygotowywanej pizzy."""
    print("\nPrzygotowuję pizzę o wielkosci "
          + str(size) + " cm, z następującymi dodatkami:")
    for topping in toppings:
        print("-" + topping)