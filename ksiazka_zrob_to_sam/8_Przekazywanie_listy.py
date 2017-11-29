# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:57:30 2017

@author: Leszek
"""
#Przekazywanie listy
def greet_users(names):
    """Wyswietla proste powitanie każdemu użytkownikowi z listy"""
    for name in names:
        msg = "Witaj, " + name.title() + "!"
        print("\n" + msg)
        
usernames = ['tomek', 'maja', 'krysia', 'leszek']
greet_users(usernames)

#Modyfikowanie listy w funkcji
#przykład 1 - bez użycia funkcji

#Rozpoczynamy od pewnych projektow, ktore mają być wydrukowane.
unprinted_designs = ['phone case', 'robot pendant', 'żelazko']
completed_designs = []

#Symulujemy wydruk poszczegolnych projektow, dopoki pozostał jakikolw.na liscie
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #Symulacja wydruku 3D na podstawie modelu.
    print("Wydruk modelu: " + current_design)
    completed_designs.append(current_design)
    
#Wyswietlanie wszystkich wydrukowanych modeli
print("\nWydrukowane zostały następujące modele:")
for completed_model in completed_designs:
    print("\n", completed_model.title())    

#przykład 2 - z użyciem dwoch funkcji
def print_models(unprinted_designs, completed_models):
    """
    Symulujemy wydruk poszczegolnych projektow dopoki pozostał jakikolwiek
    na liscie. Każdy wydrukowany model zostaje przeniesiony na
    listę completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Symulacja wydruku 3D na podstawie modelu.
        print("Wydruk modelu: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Wyswietla wszystkie modele ktore zostały wydrukowane"""
    print("\nWydrukowane zostały następujące modele:")
    for completed_model in completed_models:
        print(completed_model.title())

#Częsć głowna programu wykorzystująca obie wyżej napisane funkcje        
# z ktorych każda ma oddzielne pojedyncze zadanie
unprinted_designs = ['camera', 'apple_mobile', 'red bicycle']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Uniemożliwienie modyfikowania listy przez funkcję
# w tym celu należy do funkcji przekazać kopię listy, pierwotna się nie zmieni

print_models(unprinted_designs[:], completed_models) #funkcja jednak pracuje
# efektywniej z pierwotną listą a nie kopią, dlatego korzystanie z kopii tylko
# w uzasadnionych przypadkach.
