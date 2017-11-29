# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:10:32 2017

@author: Leszek
"""
# Najczęsciej występujące słowa
filenames = ['murder_in_gunroom.txt', 'new_life.txt',
             'pilgrimage_to_italy.txt']

for filename in filenames:
    
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        pass
    else:
        num_words = contents.count('the')
        print("\nThe book " + filename + " consists of " +
              str(num_words) + " 'the'.")     