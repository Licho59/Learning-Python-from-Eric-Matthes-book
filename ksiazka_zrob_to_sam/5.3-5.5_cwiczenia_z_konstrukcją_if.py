# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:27:12 2017

@author: Leszek
"""
#Konstrukcja if - zadania
#Zadanie 5.3 Kolory obcych cz.1
alien_color = 'zielony'
if alien_color == 'zielony':
    print("Zarobiłes 5 punktow")

alien_color = 'czerwony'
if alien_color != 'zielony':
    print("Zarobiłes 5 punktow")

alien_color = 'niebieski'
if alien_color == 'zielony':
    print("Zarobiłes 5 punktow") #warunek niezaliczony - bez realizacji

#Zadanie 5.4 Kolory obcych cz.2
alien_color = 'biały'
if alien_color == 'zielony':
    print("Zarobiłes 5 pkt za zestrzelenie 'zielonego'.")
if alien_color != 'zielony':
    print("Zarobiłes 10 pkt za zestrzelenie tego obcego.")
#wersja II
alien_color = 'biały'
if alien_color == 'zielony':
    print("Zarobiłes 5 pkt za zestrzelenie 'zielonego'.")
else:
    print("Zarobiłes 10 pkt za zestrzelenie tego obcego.")
#Zadanie 5.5 Kolory obcych cz.3
alien_color = 'zielony'
if alien_color == 'zielony':
    punkty = 5
elif alien_color == 'żołty':
    punkty = 10
elif alien_color == 'czerwony':
    punkty = 15
print("\nZarobiłes " + str(punkty) + " punktow za zestrzelenie tego obcego.")

alien_color = 'żołty'
if alien_color == 'zielony':
    punkty = 5
elif alien_color == 'żołty':
    punkty = 10
elif alien_color == 'czerwony':
    punkty = 15
print("\nZarobiłes " + str(punkty) + " punktow za zestrzelenie tego obcego.")

alien_color = 'czerwony'
if alien_color == 'zielony':
    punkty = 5
elif alien_color == 'żołty':
    punkty = 10
elif alien_color == 'czerwony':
    punkty = 15
print("\nZarobiłes " + str(punkty) + " punktow za zestrzelenie tego obcego.")