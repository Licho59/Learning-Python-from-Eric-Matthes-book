# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:46:08 2017

@author: Leszek
"""
# Refaktoryzacja - podział kodu na serię funkcji
# Kod zawierający tylk jedną funkcję - bez refaktoryzacji
import json

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What's your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("Twoje imię zostało zapisane i będzie używane poźniej, " +
                  username + "!")
    else:
        print("Witamy ponownie, " + username.title() + "!")

greet_user()

# Podział kodu na kilka funkcji - refaktoryzacja
import json

def get_stored_username():
    """Pobranie imienia z pliku, o ile taki istnieje."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        None
    else:
        return username
    
def get_new_username():
    """Poproszenie użytkownika, aby podał swoje imię, a następnie
        zapisanie tego imienia w pliku."""
    username = input("Jak masz na imię? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Przywitanie użytkownika z użyciem jego imienia."""
    username = get_stored_username()
    if username:
        print("Witamy ponownie, " + username.title() + "!")
    else:
        username = get_new_username()
        print("Twoje imię zostało zapisane i będzie używane poźniej, " +
              username.title() + "!")
    
greet_user()
        


