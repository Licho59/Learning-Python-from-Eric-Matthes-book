# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 23:19:08 2017

@author: Leszek
"""

#8.3 T-shirt
def make_shirt(size, text):
    """Wyswietla info dotyczące rozmiaru oraz tekstu na koszulce"""
    print("\nRozmiar zamowionej koszulki to " + size +
          ", na plecach należy wydrukować napis:" + text.title()) 

make_shirt('45', 'leszek tlałka')
make_shirt(text = 'jakub tlalka', size = '39')
     
# 8.4 Duże koszulki
def make_shirt(size, text='uwielbiam pythona'):
    """Wyswietla info dotyczące rozmiaru oraz tekstu na koszulce"""
    print("\nRozmiar zamowionej koszulki to " + size +
          ", na plecach należy wydrukować napis: " + text.title())

make_shirt(size='XXL')
make_shirt(size='Medium')
make_shirt('any possible', 'freedom')

# 8.5 Miasta
def describe_city(city, country='polska'):
    """Wyswietla info na temat miasta i kraju, w ktorym ono leży"""
    print("\n" + city.title() + " znajduje się w kraju o nazwie " +
           country.title())

describe_city('warsaw')
describe_city('poznań')
describe_city('berlin', country='niemcy')