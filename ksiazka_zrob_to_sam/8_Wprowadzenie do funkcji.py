# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:24:43 2017

@author: Leszek
"""
#wprowadzenie do funkcji
def greet_user():
    """Wyswietla proste powitanie."""
    print("Witaj!")
    
greet_user #wywołanie funkcji realizuje kod tj. komunikat 'Witaj!'

#przekazywanie informacji do funkcji
def greet_user(username):
    """Wyswietla proste powitanie."""
    print("Witaj, " + username.title() + "!")

greet_user('leszek')

# 8.1 Komunikat
def display_messages():
    """Wyswietla dowolne komunikaty"""
    print("Ten rozdział jest dedykowany poznaniu funkcji.")
    
display_messages

# 8.2 Ulubiona książka
def favorite_book(title):
    """Wyswietla komunikat o książkach"""
    print("\nJedną z moich ulubionych książek jest " +
          title.title() + ".")
    
favorite_book('winnetou')