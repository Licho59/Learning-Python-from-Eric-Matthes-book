# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:06:56 2017

@author: Leszek
"""

# Używanie json.dump() i json.load()
import json # import modułu przechowującego dane

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json' # plik przechowujący dane
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj) # funkcja zapisująca dane w pliku
    
# Użycie json.load w celu wczytania danych do pamięci
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

# Zapisywanie i odczytywanie danych wygenerowanych przez użytkownika
import json

username = input("Jak masz na imię?: ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("Twoje imię zostało zapisane i będzie używane poźniej, " +
           username.title() + "!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Witamy ponownie, " + username.title() + "!")
    
# Uzupełniona wersja kodu jw. o blok try_except
import json

    # wczytanie imienia z pliku o ile wczesniej zostało w nim zapisane
    # w przeciwnym razie pytamy użytkownika o imię i zapisujemy je w pliku.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Jak masz na imię?: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("Twoje imię zostało zapisane i będzie używane poźniej, " +
           username.title() + "!")
else:
    print("Witamy ponownie, " + username.title() + "!")
    