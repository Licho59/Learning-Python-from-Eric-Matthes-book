# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:58:36 2017

@author: Leszek
"""

# Glosariusz 2 -cwiczenie 6.4
glosariusz_2 = {
              'zmienna':
                  'służy do przechowywania danych',
              'pętla_for': 
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

for element in sorted(glosariusz_2.keys()):
    print(element.title())
for k,v in sorted(glosariusz_2.items()):
    print("\nHasło: " + k.title())
    print("Znaczenie: " + v)  

#6.5 Rzeki
rivers = {'amazonka': 'brazylia', 'colorado': 'stany zjednoczone',
          'wisła': 'polska',
          }
for river,country in rivers.items():
    print(river.title() + " przepływa przez " + country.title() + ".\n")

for river in rivers.keys(): #w celu wyswietlenia kluczy
    print(river.title())

print("\nKraje wymienione w słowniku to: ")
for country in rivers.values():
    print(country.title())

#6.6 Ankieta
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',
                      }
list_of_polled = ['jakub', 'tomek', 'janek', 'edward', 'maja']
for person in list_of_polled:
    if person in favorite_languages:
        print("\nThank you " + person.title() +
              " for your participation in the poll.")
    else:
        print("\nWe encourage you " + person.title() +
              " to take participation in the poll.")
            