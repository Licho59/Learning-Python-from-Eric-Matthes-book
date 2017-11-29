# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:01:23 2017

@author: Leszek
"""

# 8.9 Magicy
def show_magicians(magician_names):
    """Wyswietla imiona magikow zamieszczone na liscie"""
    for magician in magician_names:
        print("\n", magician.title())

magicians = ['crazy jackie', 'mirrafiori', 'great mag']            
show_magicians(magicians)

#8.10 Doskonali magicy
def show_magicians(magician_names):
    """Wyswietla imiona magikow zamieszczone na liscie"""
    for magician in magician_names:
        print("\n", magician.title())

def make_great(magician_names):
    """Modyfikuje listę imion magików przez dodanie doskonały"""
    for x in range(len(magician_names)):
        magician_names[x] = 'doskonały'.title() + ' ' + magician_names[x].title()
                
magicians = ['crazy jackie', 'mirrafiori', 'great mag']            
make_great(magicians)
show_magicians(magicians)
print("\n", magicians)

#8.11 Niezmienieni magicy
def show_magicians(magician_names):
    """Wyswietla imiona magikow zamieszczone na liscie"""
    for magician in magician_names:
        print("\n", magician.title())

def make_great(magician_names):
    """Modyfikuje listę imion magików przez dodanie doskonały"""
    great_magicians = []
    for x in range(len(magician_names)):
        magician_names[x] = 'doskonały'.title() + ' ' + magician_names[x].title()
        great_magicians.append(magician_names[x])
    return great_magicians
        
magicians = ['crazy jackie', 'mirrafiori', 'great mag']            
new_list = make_great(magicians[:])
print(new_list)
show_magicians(magicians)
print("\n", magicians)