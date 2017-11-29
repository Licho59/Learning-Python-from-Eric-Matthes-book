# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 21:05:09 2017

@author: Leszek
"""
#Wartosć zwrotna
def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane imię i nazwisko"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') #wywołanie funkcji
#zwracającej wartosć wymaga dostarczenia zmiennej w celu przechowania wartosci
print("\n\t", musician)

#Definiowanie argumentu jako opcjonalnego
def get_formatted_name(first_name, middle_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko"""
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()
    
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician) #kod funkcji nie jest opcjonalny

# Z argumentem opcjonalnym
def get_formatted_name(first_name, last_name, middle_name=''):
    """Zwraca elegancko sformatowane pełne imię i nazwisko"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
        return full_name.title()
    else:
        full_name = first_name + ' ' + last_name
        return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Zwrot słownika
def build_person(first_name, last_name):
    """Zwraca słownik informacji o danej osobie"""
    person = {'first': first_name, 'last': last_name}
    return person
    
musician = build_person('jimi', 'hendrix')
print(musician)

#dodatkowe wartosci dodane do słownika
def build_person(first_name, last_name, age=''): #dodano pusty argum. opcjona.
    """Zwraca słownik informacji o danej osobie"""
    person = {'first': first_name, 'last': last_name,}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', '27')
print(musician)

#Używanie funkcji wraz pętlą while
def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nProszę podać imię i nazwisko:")
    print("(wpisz 'q', aby zakończyć pracę w dowolnym momencie)")
    
    f_name = input("Imię: ")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nWitaj, " + formatted_name + "!")
 