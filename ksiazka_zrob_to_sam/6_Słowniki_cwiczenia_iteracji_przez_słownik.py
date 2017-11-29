# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 22:07:25 2017

@author: Leszek
"""

#Iteracja przez słownik- ćwiczenia - metoda items
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',}
for name, language in favorite_languages.items():
    print("\nUlubiony język programowania użytkownika " + name.title() +
          " to " + language.title() + ".")  #słowniki nie zwracają kolejnosci

#metoda keys zwraca listę wszystkich kluczy         
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',}
for name in favorite_languages.keys():
    print(name.title())
for name in favorite_languages:
    print(name.title())  #to samo wychodzi bez metody keys

#Wartosc klucza - słownik[key]
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',
                      }
print(favorite_languages['edward'].title()) #drukuje wartosc klucza dla edward                     
friends = ['sara', 'paweł']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Witaj, " + name.title() + "! Widzę, że Twoim ulubionym " +
              "jezykiem programowania jest " +favorite_languages[name].title()
              + "!")
    else:
        print("Spadaj " + name.title() + " na drzewo!")

#Iteracja przez uporządkowane klucze słownika
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',
                      }
for name in sorted(favorite_languages.keys()): #wydruk wg alfab. kolejn. imion
    print(name.title() + ", dziękujemy za udział w ankiecie.\nTwoj ulubiony" +
          " język programowania to " + favorite_languages[name] + ".\n")

#Iteracja przez wartosci kluczy
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',
                      }
print("\nW ankiecie wymienione zostały następujące języki programowania:")
for language in favorite_languages.values(): #wystąpią powtorzenia wartosci
    print(language.title())

#wyswietlenie unikatowych wartosci poprzez zbior - set
favorite_languages = {
                      'janek': 'python',
                      'sara': 'c',
                      'edward': 'ruby',
                      'paweł': 'python',
                      }
print("\nW ankiecie wymienione zostały następujące języki programowania:")
for language in set(favorite_languages.values()):
    print(language.title())                      