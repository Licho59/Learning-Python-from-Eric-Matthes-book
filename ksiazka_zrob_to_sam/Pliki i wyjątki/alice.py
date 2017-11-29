# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 14:31:11 2017

@author: Leszek
"""
# Obsługa wyjątku FileNotFoundError
filename = 'alice.txt'

with open(filename) as f_obj:
    f_obj.read()
    
# z użyciem try-except
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        f_obj.read()
except FileNotFoundError:
    msg = "Przepraszamy, ale plik " + filename + " nie istnieje."
    print(msg)
    
# Analiza tekstu
title = "Alicja w krainie czarow"
title.split() #najprostszy przykład w oparciu o tytuł książki

# analiza tekstu całej książki - liczba słow
filename = 'alice.txt'

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
    
# Praca z wieloma plikami

