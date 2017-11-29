# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:53:47 2017

@author: Leszek
"""

#Przekazywanie argumentow -argumenty pozycyjne
def describe_pet(animal_type, pet_name):
    """Wyswietla informacje o zwierzeciu"""
    print("\nMoje zwierzę to " + animal_type + ".")
    print("Moj " + animal_type + " ma na imię " +
          pet_name.title() + ".")
    
describe_pet('chomik', 'harry') #wywołanie argumentow powinno
                # odpowiadać kolejnosci parametow funkcji

#Wiele wywołań funkcji
def describe_pet(animal_type, pet_name):
    """Wyswietla informacje o zwierzęciu"""
    print("\nMoje zwierzę to " + animal_type + ".")
    print("Moj " + animal_type + " ma na imię " +
          pet_name.title() + ".")
    
describe_pet('chomik', 'harry')
describe_pet('pies', 'willie') #w przypadku argumentow pozycyjnych
                            #kolejnosć ma znaczenie

#Argumenty w postaci słow kluczowych to para: nazwa-wartosć przekazywana
# do funkcji
def describe_pet(animal_type, pet_name):
    """Wyswietla informacje o zwierzęciu"""
    print("\nMoje zwierzę to " + animal_type + ".")
    print("Moj " + animal_type + " ma na imię " +
          pet_name.title() + ".")

describe_pet(animal_type='chomik', pet_name='harry')#nie ma ryzyka błędnej
                                                    #kolejnosci
                                                    
#Wartosci domyslne
def describe_pet(pet_name, animal_type='pies'):
    """Wyswietla informacje o zwierzęciu."""
    print("\nMoje zwierzę to " + animal_type + ".")
    print("Moj " + animal_type + " ma na imię " + pet_name.title()
        + ".")
describe_pet(pet_name='willie') #zmiana kolejnosci parametrow wynika
# z zastosowania parametru pozycyjnego, ktory jest lokowany na końcu
describe_pet('willie') #dla tego przykładu wystarczy podanie argumentu 

#Odpowiedniki wywołań funkcji
def describe_pet(pet_name, animal_type='pies'):
    print("\nNasz " + animal_type + " ma na imię " + pet_name.title() + ".")
    
#Pies o imieniu Willie - dowolne z poniższych wywołań działa tak samo
describe_pet('willie')
describe_pet(pet_name='willie')

#Chomik o imieniu Harry. - jak wyżej
describe_pet('harry', 'chomik')
describe_pet(pet_name='harry', animal_type='chomik')
describe_pet(animal_type='chomik', pet_name='harry')



                                                    

