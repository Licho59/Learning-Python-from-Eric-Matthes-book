# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:28:18 2017

@author: Leszek
"""
# Utworzenie testu dla funkcji city_functions.py
import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Testy dla programu 'city_functions.py'."""
    
    def test_city_country(self):
        """Czy dane w postaci 'Santiago, Chile' są obsługiwane prawidłowo?"""
        santiago_chile = city_country('santiago', 'chile')
        self.assertEqual(santiago_chile, 'Santiago, Chile')
        
unittest.main()
        
    
