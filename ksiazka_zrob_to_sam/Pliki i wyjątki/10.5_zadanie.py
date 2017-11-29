# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:24:34 2017

@author: Leszek
"""
# 10.5 Ankieta dotycząca programowania 

filename = 'survey.txt'

print("Enter 'quit' when you are finished.")

while True:
    answer = input("Why do you like programming? ")
    if answer == 'quit':
        break
    else:
        with open(filename, 'a') as f_object:
            f_object.write(answer + "\n")
            
# Wersja odpowiedzi wg książki
filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)
    
    continue_poll = input("\nWould you like to let someone yet\
                          respond? (y/n) ")
    if continue_poll != 'y':
        break
    else:
        with open(filename, 'a') as f_object:
            for response in responses:
                f_object.write(response + "\n")