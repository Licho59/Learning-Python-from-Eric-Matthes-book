# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:24:04 2017

@author: Leszek
"""
# 10.8 Koty i psy
fname_1 = 'koty.txt'
koty = ['white', 'black', 'reddish-brown']

fname_2 = 'psy.txt'
psy = ['burek', 'azorek', 'reksio']

try:
    with open(fname_1) as f_object:
        contents = f_object.write(koty)
except FileNotFoundError:
    print("Sorry but the list is not available.")
else:
    print(contents)
try:
    with open(fname_2) as f_object:
        contents = f_object.write(psy)
except FileNotFoundError:
    print("Sorry but the list is not available.")
else:
    print(contents)
    
# Rozwiązanie wg książki - cats_and_dogs.py
filename = 'cats.txt'
with open(filename, 'w') as f:
    f.write("henry\nclarence\nmildred")

filename = 'dogs.txt'
with open(filename, 'w') as f:
    f.write("willie\nannahootz\nsummit")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f_object:
            contest = f_object.read()
            print(contest)
    except FileNotFoundError:
        print("Sorry, I can't find that file.")
