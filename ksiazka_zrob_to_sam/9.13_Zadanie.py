# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:40:12 2017

@author: Leszek
"""
# Modyfikacja za pomocą OrderedDict

from collections import OrderedDict

glosariusz_2 = OrderedDict()

glosariusz_2 = {
              'zmienna':
                  'służy do przechowywania danych',
              'petla_for': 
                  'służy do iteracji przez całą listę',
              'lista': 
                  'kolekcja elementow ułożonych w kolejnosci',
              'zen_pythona': 
                  'zbior zasad dobrego programowania',
              'słownik': 
                  'pozwala połączyć powiązane ze sobą informacje',
              }
glosariusz_2['python'] = 'język programowania' #dodanie nowej pary klucz-wartos
glosariusz_2['else'] = 'polecenie warunkowe w konstrukcji if'
glosariusz_2['zagnieżdżenie'] = 'przechowanie zestawu słownikow np. na liscie'
glosariusz_2['Django'] = 'aplikacja sieciowa'
glosariusz_2['input'] = 'funkcja do pobrania danych wejsciowych'              

for element in glosariusz_2.keys():
    print(element.title())

for k,v in glosariusz_2.items():
    print("\nHasło: " + k.title())
    print("Znaczenie: " + v)