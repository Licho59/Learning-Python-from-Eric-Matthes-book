# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 23:02:16 2017

@author: Leszek
"""
#7.4 lista dodatkow
prompt = "\nProszę wskazać dodatek do pizzy: "
prompt += "\nJesli skompletowałes dodatki wpisz 'koniec'."
lista = []
while True:
    message = input(prompt)
    
    if message  == 'koniec':
        break
    else:
        print(message)
        lista.append(message.title())

print("\nPełna lista dodatkow to: " + str(lista) + ".")

#7.5 Bilety do kina
prompt = "\nPodaj swoj wiek w latach: "
message = input(prompt)
message = int(message)
if message < 3:
    print("\nWejscie do kina jest bezpłatne!")
elif message < 12:
    print("\nCena biletu wynosi 10 zł.")
else:
    print("\nCena biletu wynosi 15 zł.")
    
#7.6 Trzy wyjscia
prompt = "\nProszę wskazać dodatek do pizzy: "
prompt += "\nJesli skompletowałes dodatki wpisz 'koniec'."
lista = []
active = True
while active: 
    message = input(prompt)
    
    if message  == 'koniec':
        active = False
    else:
        print(message)
        lista.append(message.title())
print("\nPełna lista dodatkow do pizzy: " + str(lista) + ".")

#7.7 Nieskończonosc
prompt = "Wpisz nazwę miasta: "
message = input(prompt)
while True:
    print(message) #pętla w nieskończonosc
#aby tego uniknąć
prompt = "Wpisz nazwę miasta: "
while True:
    message = input(prompt)
    if message == 'wschowa':
        print("Koniec tej zabawy!")
        break
    else:
        print(message.title())