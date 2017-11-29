# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:11:32 2017

@author: Leszek
"""
#Testy warunkowe
car = 'subaru'
print("Czy car == 'subaru'? Przewiduję wartość True.")
print(car == 'subaru')

print("\nCzy car == 'audi'? Przewiduję wartość False.")
print(car == 'audi')

my_dish = 'bigos'
print("Czy my_dish == 'marchewka'? Przewiduję False.")
print(my_dish == 'marchewka')
print("\nCzy my_dish == 'bigos'? Przewiduję True.")
print(my_dish == 'bigos')

car = 'honda'
car == 'toyota'

favorite_place = 'london'
favorite_place == 'london'

street = 'jesionowa'
street == 'bukowa'
street = 'jarzebinowa'


street == 'jesionowa'

street != 'akacjowa'

#5.2. Więcej testow warunkowych
title = 'winnetou among appaches'
title =='Old Surehand among Appaches'
title !='Old Surehand among Appaches'
title = 'winnetou among appaches'
title == 'Winnetou among appaches'.lower() #True

#Testy liczbowe
age = 57
age == 56
age = 57
age <= 60 

height_1 = 180
height_2 = 170
height_2 > 169 and height_1 == 180
height_1 < 130 or height_2 >= 183 

#Sprawdzanie czy element znajduje się na liscie
dishes = ['rosol', 'bigos', 'flaki', 'ziemniaki']
if 'kotlet' not in dishes:
    print("To nieprawda że kotlet należy do 'dishes'")
if 'bigos' in dishes:
    print("Rzeczywiscie bigos należy do 'dishes'")