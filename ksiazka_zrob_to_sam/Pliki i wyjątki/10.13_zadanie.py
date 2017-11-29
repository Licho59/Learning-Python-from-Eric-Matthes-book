# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:25:42 2017

@author: Leszek
"""
# 10.13 Weryfikacja użytkownika
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
        correct = input("Are you " + username + "?(y/n) ")
        if correct == 'y':
            print("Witamy ponownie, " + username.title() + "!")
        else:
            username = get_new_username()
            print("Twoje imię zostało zapisane i będzie używane poźniej, " +
              username.title() + "!")
    else:
        username = get_new_username()
        print("Twoje imię zostało zapisane i będzie używane poźniej, " +
              username.title() + "!")
    
greet_user()
