# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:57:30 2017

@author: Leszek
"""
# 8.15 Wydruk modeli

import printing_functions as pf

unprinted_designs = ['camera', 'apple_mobile', 'red bicycle']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
