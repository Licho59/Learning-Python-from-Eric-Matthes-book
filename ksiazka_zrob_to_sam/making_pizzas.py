# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:49:16 2017

@author: Leszek
"""
# Nadawanie stylu funkcjom:
    # - dla wartosci parametrow domyslnych oraz słow kluczowych
        # bez spacji po obu stronach znaku =
    # - w każdej funkcji zwięzły komentarz wyjasniający jej przeznaczenie
    # - dla długiej listy parametrow powdwojne wcięcia w nowym wierszu
    # - polecenia import powinny znajdować się na początku pliku

# Import całego modułu
import pizza

pizza.make_pizza(40, 'pepperoni')
pizza.make_pizza(30, 'pieczarki', 'zielona papryka', 'podwojny ser')

# Import okreslonych funkcji z modułu
from pizza import make_pizza

pizza.make_pizza(24, 'grzyby', 'ser')
# ponieważ w poleceniu import jest wskazana funkcja nie ma potrzeby
#wywoływać nazwy modułu
make_pizza(33, 'pomidory', 'kiełbasa')

# Użycie słowa kluczowego "as" w celu zdefiniowania aliasu funkcji
from pizza import make_pizza as mp

mp(30, 'pepperoni')
mp(45, 'pomidor', 'cebula', 'szynka') 

#podobnie można zdefiniować alias modułu np.
import pizza as p

p.make_pizza(33, 'ogorek')

# Import wszystkich funkcji modułu za pomocą "*"
from pizza import *

make_pizza(40,'szynka')
