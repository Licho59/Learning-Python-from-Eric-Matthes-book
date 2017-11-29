# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:33:40 2017

@author: Leszek
"""

# Testowanie funkcji
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

unittest.main() # polecenie wykonania testow zdefiniowanych w pliku

  #po modyfikacji kodu w 'name_function.py' (dodane 'middle')
  # test wyrzuca komunikat 'FAILED (errors=1) - test jest ok ale w funkcji
    #  get_formatted_name należy znaleźć i poprawić błąd                                     