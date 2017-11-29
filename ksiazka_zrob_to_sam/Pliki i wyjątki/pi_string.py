# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:28:05 2017

@author: Leszek
"""

# Praca z zawartoscią pliku
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line.rstrip() #funkcja strip zlikwiduje wszystkie białe znaki
                              # i wtedy zamiast len=36 będzie len=32
print(pi_string)
print(len(pi_string))
    
# Ogromne pliki, czyli na przykład milion cyfr
file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52] + "...") # można wstawić dowolną liczbę miejsc po przecin.
print(len(pi_string))

# Czy data moich urodzin znajduje się w liczbie pi?
file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_string = ''

for line in lines:
    pi_string += line.strip()
    
birthday = input("Podaj datę urodzenia (w formacie ddmmrr): ")
if birthday in pi_string:
    print("Twoja data urodzenia znajduje się wsrod miliona pierwszych\
        cyfr liczby pi.")
else:
    print("Twoja data urodzenia nie znajduje się wsrod miliona pierwszych\
        cyfr liczby pi.")        









