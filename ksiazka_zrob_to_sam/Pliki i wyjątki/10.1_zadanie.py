# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:20:11 2017

@author: Leszek
"""
# 10.1 Poznajemy Pythona
file_name = 'learning_python.txt'

print("\n---Reading in the entire file:")
with open(file_name) as file_object:
    contents = file_object.read()
    print(contents)
    
print("\n---Looping over the lines:")
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
        
print("\n---Storing the lines in a list:")
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())

    
  