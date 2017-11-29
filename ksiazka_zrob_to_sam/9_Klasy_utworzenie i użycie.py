# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:34:42 2017

@author: Leszek
"""

# Utworzenie i użycie klasy
class Dog():
    """Prosta proba modelowania psa."""
    
    def __init__(self, name, age):
        """Inicjalizacja atrybutow name i age."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia."""
        print(self.name.title() + " teraz siedzi.")
        
    def roll_over(self):
        """Symulacja, że pies kładzie się na plecach po otrzymaniu
        polecenia."""
        print(self.name.title() + " teraz położył się na plecy!")
        
# Utworzenie egzemplarza na podstawie klasy
class Dog():
   """Prosta proba modelowania psa."""
    
   def __init__(self, name, age):
        """Inicjalizacja atrybutow name i age."""
        self.name = name
        self.age = age
        
   def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia."""
        print(self.name.title() + " teraz siedzi.")
        
   def roll_over(self):
        """Symulacja, że pies kładzie się na plecach po otrzymaniu
        polecenia."""
        print(self.name.title() + " teraz położył się na plecy!")
    
my_dog = Dog('willie', 6)

print("Moj pies ma na imię " + my_dog.name.title() + ".")
print("Moj pies ma " + str(my_dog.age) + " lat.")

# Wywoływanie metod
class Dog():
   """Prosta proba modelowania psa."""
    
   def __init__(self, name, age):
        """Inicjalizacja atrybutow name i age."""
        self.name = name
        self.age = age
        
   def sit(self):
        """Symulacja, że pies siada po otrzymaniu polecenia."""
        print(self.name.title() + " teraz siedzi.")
        
   def roll_over(self):
        """Symulacja, że pies kładzie się na plecach po otrzymaniu
        polecenia."""
        print(self.name.title() + " teraz położył się na plecy!")
    
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()

# Utworzenie wielu egzemplarzy
# Klasa Dog została już zdefiniowana i wywołana w poprzednim
# przykładzie
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)

print("Moj pies ma na imię " + my_dog.name.title() + ".")
print("Moj pies ma " + str(my_dog.age) + " lat.")
my_dog.sit()

print("\nTwoj pies ma na imię " + your_dog.name.title() + ".")
print("Twoj pies ma " + str(your_dog.age) + " lat.")
your_dog.roll_over()