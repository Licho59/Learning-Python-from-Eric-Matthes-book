# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:08:00 2017

@author: Leszek
"""

# 8.12 Kanapki
def make_sandwich(*toppings):
    """Podsumowanie zawartosci zamawianej przez klienta kanapki."""
    print("\nZamowiono kanapkę, ktora zawiera:")
    for topping in toppings:
        print("- " + topping)
        
make_sandwich('żołty ser')
make_sandwich('pomidor', 'szynka', 'majonez')
make_sandwich('sałata', 'biały ser', 'ogorek', 'ketchup')

# 8.13 Profil użytkownika
def build_profile(first, last, **user_info): 
            # ** - oznacza utworzenie pustego słownika
    """Budowa słownika zawierającego wszelkie informacje o użytkowniku."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('leszek', 'tlalka',
                             profession = 'manager',
                             location = 'belchatow',
                             field = 'research&development',
                             company = 'pge giek')
print(user_profile)

# 8.14 Samochody
def make_car_info(make, model, **car_info):
    """Budowa słownika zawierającego dane samochodu."""
    profile = {}
    profile['car_make'] = make
    profile['car_model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile
    
car_profile = make_car_info('honda', 'crv',
                            color='grey metalic',
                            age='10 years',
                            tow_package=True)
print(car_profile)