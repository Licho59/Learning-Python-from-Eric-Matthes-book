# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:11:06 2017

@author: Leszek
"""

# Testowanie funkcji -dodanie nowego testu
import unittest   #moduł z narzędziami do testowania kodu
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'name_function.py'.""" # utworzono klasę do zrobienia
 # serii testow jednostkowych - dziedziczy ona po klasie unittest.TestCase
     
    def test_first_last_name(self): #metoda sprawdzająca 1 aspekt funcji get_..
        #metoda zaczynająca się od 'test_' uruchamiana jest automatycznie 
        """Czy dane w postaci 'Janis Joplin' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #metoda asercji
         # (z mod inittest) sprawdza czy otrzymany wynik odpowiada oczekiwanemu
         # oznacza: "porownaj wartosć zmiennej f_n z ciągem 'Janis Joplin'
    
    def test_first_middle_last_name(self):
        """Czy dane w postacji 'Wolfgang Amadeus Mozart' są obsługiwane
            prawidłowo?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main() # polecenie wykonania testow zdefiniowanych w pliku