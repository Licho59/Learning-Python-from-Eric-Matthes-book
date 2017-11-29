# -*- coding: utf-8 -*-
"""
Created on Sun May 14 21:52:48 2017

@author: Leszek
"""
from user import User

class Privileges():
    """Okresla uprawnienia administratora witryny."""
    
    def __init__(self,privileges):
        """Inicjalizacja atrybutu uprawnień."""
        self.privileges = privileges
        
    def show_privileges(self):
        """Wyswietla listę uprawnień administratora witryny."""
        print("Lista uprawnień administratora witryny:")
        print(self.privileges)    
        
class Admin(User):
    """Przedstawia uprawnienia dla administratora witryny."""
    
    def __init__(self, first, last, age, sex, location, privileges):
        """Inicjalizacja atrybutow klasy nadrzędnej."""
        super().__init__(first, last, age, sex, location)
        self.privileges = privileges