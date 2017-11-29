# -*- coding: utf-8-*-
"""
Spyder Editor

This is a temporary script file.
"""
# Zapisywanie danych do pustego pliku
filename = 'programming.txt'

with open(filename, 'w') as file_object: # 'r'/'w'/'a'-tryby odczyt/zapis/dołąc
    file_object.write("Uwielbiam programować.") # 'r+' łącznie odczyt i zapis
# metoda write zapisuje tekst (Uwielbiam programować) w pliku 'programming'
#jednoczenie usuwając pierwotną zawartosć

# Zapisywanie wielu wierszy - unikać polskiej czcionki (?)
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("Uwielbiam filmować.\n") #polskie czcionki pisze maczkami
    file_object.write("Uwielbiam z nią tworzyć nowe gry.\n")
    print("Spiewać też lubię!")
    
# Dołączanie do pliku
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love finding elements in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")