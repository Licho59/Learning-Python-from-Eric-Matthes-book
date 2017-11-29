# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:44:14 2017

@author: Leszek
"""

# 9.4 Liczba obsłużonych
class Restaurant():
    """Prosty opis restauracji oraz menu."""
    
    def __init__(self, name, cuisine):
        """Inicjalizacja atrybutow restaurant_name i cuisine_type."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
        
    def describe_restaurant(self):
        """Wyswietla nazwę restauracji oraz rodzaj menu."""
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
        
    def open_restaurant(self, opening, closing):
        """Wyswietla info o godzinach pracy restauracji."""
        print("The restaurant " + self.restaurant_name.title() +
              " is open from " + opening + " to " +
              closing + ".")
    
    def set_number_served(self,clients):
        """Definiuje liczbę obsłużonych klientow."""
        self.number_served = clients
               
    def increment_number_served(self, clients_per_day):
        """Inkrementacja liczby obsłużonych klientow."""
        self.number_served += clients_per_day
        
restaurant = Restaurant('ratuszowa', 'kuchnia regionalna')
restaurant.set_number_served(123)
restaurant.increment_number_served(27)
print("Liczba obsłużonych klientow: " + str(restaurant.number_served))

# 9.5 Proby logowania
class Users():
    """Prosty opis profilu użytkownika."""
    
    def __init__(self, first, last, age, sex, location):
        """Inicjalizacja atrybutow first_name i last_name."""
        self.first_name = first
        self.last_name = last
        self.user_age = age
        self.user_sex = sex
        self.user_location = location
        self.login_attempts = 12
        
    def describe_user(self):
        """Podsumowuje informacje zebrane o użytkowniku."""
        print("\nProfil użytkownika:")
        print("\tImię: " + self.first_name.title())
        print("\tNazwisko: " + self.last_name.title())
        print("\tWiek: " + self.user_age)
        print("\tPłeć: " + self.user_sex.title())
        print("\tMiejsce zamieszkania: " + self.user_location.title())

    def greet_user(self):
        """Wyswietla spersonalizowane powitanie użytkownika."""
        print("\n" + self.first_name.title() + ", Witamy na naszym portalu!")
        
    def increment_login_attempts(self):
        """Inkrementuje wartosci login_attempts."""
        self.login_attempts += 1
        
        
    def reset_login_attempts(self):
        """Zerowanie wartosci login_attempts."""
        self.login_attempts = 0
                   
user_1 = Users('leszek', 'tlalka', '58', 'man', 'bełchatow')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

user_1.reset_login_attempts()
print("Liczba logowań: " + str(user_1.login_attempts))

