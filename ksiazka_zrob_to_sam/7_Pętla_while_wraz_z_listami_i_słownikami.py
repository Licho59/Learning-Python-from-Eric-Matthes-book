# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:49:45 2017

@author: Leszek
"""
#Przenoszenie elementow z jednej listy na drugą
unconfirmed_users = ['alicja', 'bartek', 'katarzyna', 'viola']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() #funkcja pop po usunięciu ostatniej
                #pozycji pozwala użyć ponownie usuniętego elementu 
    print("Weryfikacja użytkownika: " + current_user.title())
    confirmed_users.append(current_user)
    
print("\nZweryfikowano wymienionych poniżej użytkownikow:")
for confirmed_user in confirmed_users:
    print("\t", confirmed_user.title())
    
#Usuwanie z listy wszystkich egzemplarzy okreslonej wartosci
pets = ['kot', 'pies', 'koń', 'kot', 'kura', 'kot', 'kogut', 'kot']
print(pets)

while 'kot' in pets:
    pets.remove('kot')
print(pets)

#Umieszczenie w słowniku danych wejsciowych przez użytkownika
responses = {}
polling_active = True

while polling_active:
    name = input("What's your name?: ")
    response = input("\nWhat peak would you like to climb up one day?: ")

    responses[name] = response

    repeat = input("If does anyone want to participate in\
                   the poll?(yes/no): ")
    if repeat == 'no':
        polling_active = False

print("\n----Poll results----")
for name, response in responses.items():
    print("\n" + name.title() + " would like to climb up for "
          + response.title() + ".")
  