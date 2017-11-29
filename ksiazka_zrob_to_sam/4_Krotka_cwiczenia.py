# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:07:25 2017

@author: Leszek
"""

dimmensions = (200,50)  #krotka - list z okraglymi
# nawiasami jest niezmienialna
print(dimmensions[0])
print(dimmensions[1])
dimmensions[0] = 250 #komunikat błędu-krotki nie można modyfikować
for dimmension in dimmensions:
    print(dimmension)

#Nadpisanie krotki
dimmensions = (200,50)
print("Wymiary początkowe:")
for dimmension in dimmensions:
    print(dimmension)

dimmensions = (400,100) #w zmiennej dimmensions umieszczono nową krotkę
print("\nWymiary po modyfikacji:")
for dimmension in dimmensions:
    print(dimmension)
    
# 4.13 Bufet
bufet = ('jajecznica', 'spaghetti', 'rizotto', 'bigos', 'mielony')
for danie in bufet:
    print(danie.title())
bufet[3] = 'schabowy' #brak możliwosci modyfikacji krotki

bufet = ('jajecznica', 'pomidorowa', 'rizotto', 'bigos', 'ziemniaki')
for danie in bufet:
    print(danie.title())