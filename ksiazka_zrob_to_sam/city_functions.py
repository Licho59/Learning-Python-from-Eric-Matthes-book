# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 21:16:20 2017

@author: Leszek
"""
# 11.1 - 11.2  Utworzenie funkcji z nazwami miasta i państwa + populacja
# funkcję zmodyfikowano poprzez dodanie parametru 'population

"""A collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Return a string representing a city_country pair."""
    
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' - population ' + str(population)
    return output_string
    