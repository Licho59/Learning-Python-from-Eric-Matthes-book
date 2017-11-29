# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 22:50:31 2017

@author: Leszek
"""
# Wczytywanie całego pliku

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) #metoda rstrip kasuje pusty wiersz
         #zwrocony przez metodę read na koncu pliku tekstowego
         
# Scieżka dostępu do pliku
#Umieszczenie plikow tekstowych w oddzielnym podkatalogu niż pliki
#programu wymaga podania w programie tzw.względnej scieżki dostępu do pliku
# tekstowego np. 
with open('pliki_tekstowe\pi_digits.txt') as file_object: 

# lub bezwzględnej scieżki dostępu w przypadku dowolnej lokalizacji pliku
# z uwagi na długosć scieżki warto przechowywać ją w zmiennej np:
file_path = 'C\Users\nazwa_użytkownika\inne\pliki_tekstowe\nazwa_pliku.txt'
with open(file_path) as file_object:

# Odczytywanie wiersz po wierszu

file_name = 'pi_digits.txt'
with open(file_name) as file_object:
     for line in file_object:
        print(line.rstrip())
        
# Utworzenie listy wierszy na podstawie zawartosci pliku

file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
type(lines)

     