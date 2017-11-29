# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:22:59 2017

@author: Leszek
"""

#9.1 Restauracja
class Restaurant():
    """Prosty opis restauracji oraz menu."""
    
    def __init__(self, name, cuisine):
        """Inicjalizacja atrybutow restaurant_name i cuisine_type."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        
    def describe_restaurant(self):
        """Wyswietla nazwę restauracji oraz rodzaj menu."""
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
        
    def open_restaurant(self, opening_hour, closing_hour):
        """Wyswietla info o godzinach pracy restauracji."""
        self.opening = opening_hour
        self.closing = closing_hour
        print("The restaurant " + self.restaurant_name.title() +
              " is open from " + self.opening + " to " +
              self.closing + ".")

restaurant = Restaurant('ratuszowa', 'kuchnia regionalna')

restaurant.describe_restaurant()
restaurant.open_restaurant('8am','10pm')
print(restaurant.restaurant_name) 
        
# 9.2 Trzy restauracje
class Restaurant():
    """Prosty opis restauracji oraz menu."""
    
    def __init__(self, name, cuisine):
        """Inicjalizacja atrybutow restaurant_name i cuisine_type."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        
    def describe_restaurant(self):
        """Wyswietla nazwę restauracji oraz rodzaj menu."""
        print("\nNazwa restauracji oraz rodzaj menu:")
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
        
    def open_restaurant(self, opening_hour, closing_hour):
        """Wyswietla info o godzinach pracy restauracji."""
        
        print("The restaurant " + self.restaurant_name.title() +
              " is open from " + opening_hour + " to " +
              closing_hour + ".")

restaurant_1 = Restaurant('ratuszowa', 'kuchnia regionalna')
restaurant_2 = Restaurant('biała dama', 'kuchnia polska')
restaurant_3 = Restaurant('pod niebem toskanii', 'pizza food')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9.3 Użytkownicy
class Users():
    """Prosty opis profilu użytkownika."""
    
    def __init__(self, first, last, age, sex, location):
        """Inicjalizacja atrybutow first_name i last_name."""
        self.first_name = first
        self.last_name = last
        self.user_age = age
        self.user_sex = sex
        self.user_location = location
        
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
    
user_1 = Users('leszek', 'tlalka', '58', 'man', 'bełchatow')
user_2 = Users('kuba', 'tlalka', '27', 'man', 'warszawa')
user_3 = Users('marzena', 'tlalka krasowska', '37', 'woman', 'wrocław')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()        
        
       