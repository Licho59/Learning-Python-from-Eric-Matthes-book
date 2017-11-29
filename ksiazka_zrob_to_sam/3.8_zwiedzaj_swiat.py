# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:48:04 2017

@author: Leszek
"""

miejsca = ['argentyna', 'szkocja', 'mediolan', 'alaska', 'sydney']
print(miejsca)
print(sorted(miejsca)) #tymczasowa kolejnosc alfabetyczna
print(miejsca) #potwierdzenie że lista nie zmieniona
print(sorted(miejsca, reverse=True)) #tymcz kolejn alfabet odwrotna
print(miejsca) #potwierdzenie że lista nie zmieniona
miejsca.reverse() #trwałe odwrocenie kolejnosci
print(miejsca)
miejsca.reverse() #powtorzenie komendy wraca do pierwotnej listy
print(miejsca)
miejsca.sort() #trwała zmiana kolejn. na alfab
print(miejsca) 
miejsca.sort(reverse=True) #param odwr kolejn alfab
print(miejsca)