# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:18:15 2017

@author: Leszek
"""
#Polecenie if-else
age = 17 # przebieg pętli w zależnosci od wartosci zmiennej
if age >= 18:
    print("Możesz wziąć udział w głosowaniu.")
    print("\nCzy zarejestrowałes się już aby głosować?")

else:
    print("Jestes za młody aby wziąć udział w głosowaniu.")
    print("Możesz się zarejestrować po ukończeniu 18 lat.")

#Łańcuch if-elif-else - służy do sprawdzania jednego konkretnego warunku
age = 14
if age < 4:
    print("Cena biletu wstępu wynosi 0 zł.")
elif age < 18: #polecenie elif  jest wykonywane jesli if jest False
    print("Cena biletu wstępu wynosi 5 zł.")
else: #polecenie else jest wykonywane  obligatoryjnie gdy nie spełniony jest
# żaden z powyższych warunkow, nawet jesli są nieprawidłowe dane
    print("Cena biletu wstępu wynosi 10 zł.")

#drobna optymalizacja - w razie potrzeby tylko korekta w wydruku
age = 70
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age > 65:
    price = 5
else: # można bez else - elif age > 65 jest tak samo dobre
    price = 10
print("Cena biletu wstępu wynosi " + str(price) + " zł.")

#Sprawdzanie wielu warunkow - niezależne od siebie warunki
requested_toppings = ['pieczarki', 'podwojny ser']
if 'pieczarki' in requested_toppings:
    print("\tDodaję pieczarki.")
if 'pepperoni' in requested_toppings:
    print("\tDodaję pepperoni.")
if 'podwojny ser' in requested_toppings:
    print("\tDodaję podwojny ser.")
print("\n\tTwoja pizza jest już gotowa!")

