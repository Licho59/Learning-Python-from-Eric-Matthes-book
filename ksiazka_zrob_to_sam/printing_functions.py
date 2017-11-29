# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:39:13 2017

@author: Leszek
"""

def print_models(unprinted_designs, completed_models):
    """
    Symulujemy wydruk poszczegolnych projektow dopoki pozostał jakikolwiek
    na liscie. Każdy wydrukowany model zostaje przeniesiony na
    listę completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # Symulacja wydruku 3D na podstawie modelu.
        print("Wydruk modelu: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Wyswietla wszystkie modele ktore zostały wydrukowane"""
    print("\nWydrukowane zostały następujące modele:")
    for completed_model in completed_models:
        print(completed_model.title())