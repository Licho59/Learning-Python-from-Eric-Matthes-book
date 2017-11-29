# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:13:00 2017

@author: Leszek
"""

# Ciche koty i psy

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as f_object:
            contest = f_object.read()
            
    except FileNotFoundError:
        pass
    else:
        print("\nReading file: " + filename)
        print(contest)