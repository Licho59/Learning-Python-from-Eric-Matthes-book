# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 22:14:03 2017

@author: Leszek
"""

# 10.3 Gosć
guest_name = input("Wprowadź swoje imię:")
filename = 'user_name.txt' 
              # funkcja open tworzy plik *txt jesli go wczesniej nie utworzono
with open(filename, 'w') as file_object: 
    file_object.write(guest_name.title())
    
# 10.4 Księga gosci - moja odpowiedź
filename = 'guest_book.txt'

prompt = "\nWprowadź swoje imię: "
prompt += "\nNapisz 'koniec' aby zakończyć działanie programu."
guest_name = ""
while guest_name != 'koniec':
    guest_name = input(prompt)
    if guest_name != 'koniec':
        print("Thank you very much " + guest_name.title( ) +
              " for visiting our website!")
    with open(filename, 'a') as file_object:
        file_object.write("New guest: " + guest_name.title() +".\n")
        
# Księga gosci - poprawnie wg książki
filename = 'guest_book_11.txt'

print("Enter 'quit' when you are finished.")

while True:
    name = input("What's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name.title() + "\n")
        print("Hi " + name.title() + ", you've been added to the guestbook.")
    