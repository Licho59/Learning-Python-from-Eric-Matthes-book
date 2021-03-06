# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:45:56 2017

@author: Leszek
"""

# 9.7 Admin.
class Users():
    """Prosty opis profilu użytkownika."""
    
    def __init__(self, first, last, age, sex, location):
        """Inicjalizacja atrybutow first_name i last_name."""
        self.first_name = first
        self.last_name = last
        self.user_age = age
        self.user_sex = sex
        self.user_location = location
        self.login_attempts = 0
        
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
        
class Admin(Users):
    """Przedstawia uprawnienia dla administratora witryny."""
    
    def __init__(self, first, last, age, sex, location, privileges):
        """Inicjalizacja atrybutow klasy nadrzędnej."""
        super().__init__(first, last, age, sex, location)
        self.privileges = privileges

    def show_privileges(self):
        """Wyswietla listę uprawnień administratora witryny."""
        print("Lista uprawnień administratora witryny:")
        print(self.privileges)
        
my_admin = Admin('michał', 'urbaniak', 54, 'man', 'warszawa',
                 ['może dodać post', 'może usunąć post',
                 'może zbanować użytkownika', 'może wiele więcej'])
my_admin.show_privileges()