# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 18:39:08 2017

@author: Leszek
"""

#5.8 Witaj, administratorze
users = ['licho', 'kajko','admin', 'mamba', 'kokosz', 'balbina']
for user in users:
    if user == 'admin':
        print("Witaj, admin! Czy chcesz przejrzeć raport?")
    else:
        print("Witaj, " + user.title() + 
              "! \nDziękujemy, że ponownie się zalogowałes.")

#5.9 Brak użytkownikow
users = ['licho', 'kajko','admin', 'mamba', 'kokosz', 'balbina']
del users[:] 
if users: #if sprawdza czy lista nie jest pusta (True wykonuje blok) 
    for user in users:
        if user == 'admin':
            print("Witaj, admin! Czy chcesz przejrzeć raport?")
        else:
            print("Witaj, " + user.title() + 
              "! \nDziękujemy, że ponownie się zalogowałes.")
else:
    print("Musimy znaleźć jakichs użytkownikow.")

# Sprawdzanie nazw użytkownikow
users = ['licho', 'kajko','admin', 'Mamba', 'kokosz', 'balbina']
current_users = []
for user in users:
    current_users.append(user.lower())
new_users = ['mamba','majka', 'tomek', 'licho']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Wybierz inną nazwę użytkownika.")
    else:
        print("Twoja nazwa użytkownika jest poprawna.")
        
#Ten kod źle działa
users = ['licho', 'kajko','admin', 'Mamba', 'kokosz', 'balbina']
current_users = users[:]
new_users = ['majka','mamba','licho', 'tomek']
for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            print("Wybierz inną nazwę użytkownika.")
            break
    print("Twoja nazwa użytkownika jest poprawna.")
    
#Ten kod działa dobrze - z pomocą Kuby
    users = ['licho', 'kajko','admin', 'Mamba', 'kokosz', 'balbina']
current_users = users[:]
new_users = ['majka','mamba','licho', 'tomek']
for new_user in new_users:
    repeated = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            repeated = True
            break
    if repeated:
        print("Wybierz inną nazwę użytkownika.")
            
    else:
        print("Twoja nazwa użytkownika jest poprawna.")

#Sprawdzanie nazw użytkownikow - od Kuby - z nieznaną jeszcze formą kodu
users = ['licho', 'kajko','admin', 'Mamba', 'kokosz', 'balbina']
current_users = users[:]
new_users = ['mamba','majka', 'tomek', 'licho']
for new_user in new_users:
    if new_user.lower() in [u.lower() for u in current_users]:
        print("Wybierz inną nazwę użytkownika.")
    else:
        print("Twoja nazwa użytkownika jest poprawna.")       

    
    #Liczby porządkowe
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")

#korekta kodu Sprawdzanie nazw użytkownikow
users = ['licho', 'kajko','admin', 'Mamba', 'kokosz', 'balbina']
current_users = users[:]
new_users = ['mamba','majka', 'tomek', 'licho']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Wybierz inną nazwę użytkownika.")
    else:
        print("Twoja nazwa użytkownika jest poprawna.")
    
