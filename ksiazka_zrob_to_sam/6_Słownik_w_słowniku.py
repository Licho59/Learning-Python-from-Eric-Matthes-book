# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 11:53:57 2017

@author: Leszek
"""

#Słownik w słowniku

users = {'aeinstein':
            {'first': 'albert',
             'last': 'enistein',
             'location': 'princetown',
             },
         'mcurie':
            {'first': 'marie',
             'last': 'skłodowska-curie',
             'location': 'paryż',
             },
        }
        
for username, user_info in users.items():
    print("\nNazwa użytkownika:" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\nImię i nazwisko: " + full_name.title())
    print("\tMiejscowosć: " + location.title())