# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 23:29:33 2017

@author: Leszek
"""
# Program wykorzystujący klasę AnonymousSurvey
from survey import AnonymousSurvey

 # Zdefiniowanie pytania i utworzenie ankiety
question = "Jaki jest Twoj ojczysty język?"
my_survey = AnonymousSurvey(question)

# Wyswietlenie pytania i przechowywanie odpowiedzi na nie
my_survey.show_question()
print("Wpisz 'q', aby zakończyć działanie programu.\n")
while True:
    response = input("Język: ")
    if response == 'q':
        break
    my_survey.store_response(response)
    
# Wyswietlenie wynikow ankiety
print("\nDziękujemy każdemu respondentowi za udział w ankiecie!")
my_survey.show_results()
