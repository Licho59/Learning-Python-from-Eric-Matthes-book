# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:34:59 2017

@author: Leszek
"""

# 10.2 Poznajemy C
file_name = 'learning_python.txt'
   
with open(file_name) as file_object:
    for line in file_object:
        language = line.replace('Pythonie', 'C')
        print(language.rstrip())
    print("--------------")

# rozwiazanie wg książki
with open(file_name) as f:
    lines = f.readlines()
        
for line in lines:
# zastąpienie "Pythonie" przez "C"
    line = line.strip()
    print(line.replace('Pythonie', 'C'))
    