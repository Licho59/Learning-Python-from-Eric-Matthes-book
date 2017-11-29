# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:59:33 2017

@author: Leszek
"""

# 5.6 Etapy życia - zadanie
age = 65
if age < 2:
    print("Jestes niemowlęciem.")
if age >= 2 and age < 4:
    print("Jestes dzieckiem, ktore uczy się chodzić.")
if age >= 4 and age < 13:
    print("Jestes dzieckiem.")
if age >= 13 and age < 20:
    print("Jestes nastolatkiem.")
if age >=20 and age < 65:
    print("Jestes dorosły.")
else:
    print("Jestes seniorem.")

#5.7 Ulubione owoce
favorite_fruits = ['jabłka', 'granaty', 'winogrona', 'daktyle']
if 'jabłka' in favorite_fruits:
    print("Naprawdę lubisz banany.")
if 'granaty' in favorite_fruits:
    print("Naprawdę lubisz banany.")
if 'banany' not in favorite_fruits:
    print("Uzupełnij listę ulubionych owocow.")

    