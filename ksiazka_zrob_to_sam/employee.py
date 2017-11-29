# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 15:23:41 2017

@author: Leszek
"""

# 11.3 Pracownik - przygotowanie klasy Employee
class Employee():
    """ A class to represent an employee."""
    
    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.first = f_name.title()
        self.last = l_name.title()
        self.salary = salary
        
    def give_raise(self, amount=5000):
        """Give the employee a rise."""
        self.salary += amount
        