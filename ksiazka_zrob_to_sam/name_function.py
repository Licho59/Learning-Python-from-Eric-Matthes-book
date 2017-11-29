# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:08:42 2017

@author: Leszek
"""

"""def get_formatted_name(first, middle, last):
   # Generuje elegancko sformatowane imię i nazwisko.
    full_name = first + ' ' + middle + ' ' + last #modyfikacja kodu (middle)
                                        # skutkuje wywołaniem błędu w tescie
    return full_name.title()

# niezbędna poprawa testu poprzez okreslenie parametru 'middle' jako opcjonaln
# tj. (first, last, middle='') oraz dodatkowo funkcję 'if'"""

# Poprawiona funkcja
def get_formatted_name(first, last, middle=''):
    """Generuje elegancko sformatowane pełne imię i nazwisko."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()