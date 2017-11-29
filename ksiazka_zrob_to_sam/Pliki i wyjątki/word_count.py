# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:23:50 2017

@author: Leszek
"""
# funkcja do liczenia słow w pliku

def count_words(filename):
    """Obliczenie przybliżonej liczby słow w danym pliku."""
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Przepraszamy, ale plik " + filename + " nie istnieje."
        print(msg)
    else:
        # Obliczenie przybliżonej liczby słow w pliku.
        words = contents.split()
        num_words = len(words)
        print("Plik " + filename + " zawiera " + str(num_words) +
              " słow.")
    
filename = 'alice.txt'
count_words(filename)

# Praca z wieloma plikami
def count_words(filename):
    """Obliczenie przybliżonej liczby słow w danym pliku."""
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Przepraszamy, ale plik " + filename + " nie istnieje."
        print(msg)
    else:
        # Obliczenie przybliżonej liczby słow w pliku.
        words = contents.split()
        num_words = len(words)
        print("Plik " + filename + " zawiera " + str(num_words) +
              " słow.")
        
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt',
              'little_women.txt']
for filename in filenames:
    count_words(filename)
    
# Ciche niepowodzenie - jeżeli nie jest konieczne zgłaszanie przechwyconego
# wyjątku.
def count_words(filename):
    """Obliczenie przybliżonej liczby słow w danym pliku."""
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Obliczenie przybliżonej liczby słow w pliku.
        words = contents.split()
        num_words = len(words)
        print("Plik " + filename + " zawiera " + str(num_words) +
              " słow.")
        
filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt',
              'little_women.txt']
for filename in filenames:
    count_words(filename)