# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:23:06 2017

@author: Leszek
"""

#8.6 Nazwy miast
def city_country(city, country):
    """Zwraca ciąg tekstowy z nazwami miasta i kraju w ktorym ono leży"""
    cc_name = city + ", " + country
    return cc_name.title()
    
info = city_country('warsaw', 'poland')
print(info)

info = city_country('berlin', 'niemcy')
print(info)

info = city_country('rzym', 'włochy')
print(info)

#8.7 Album
def make_album(artist, album_title, song_number=''):
    """Zwraca słownik z nazwą artysty i tytułem albumu"""
    music = {'name': artist, 'album': album_title}
    if song_number:
        music['song_number'] = song_number
    return music
        
musician = make_album('the beatles', 'yellow submarine') #wywołanie funkcji
#zwracającej wartosć wymaga zmiennej do przechowania tej wartosći
print(musician)
musician = make_album('czerwone gitary', 'najlepsze hity', '12')
print(musician)
musician = make_album('stare dobre małżeństwo', 'niebieska tancbuda')
print(musician)

#8.8 Albumy użytkownikow - z użyciem pętli while
def make_album(artist, album_title, song_number=''):
    """Zwraca słownik z nazwą artysty i tytułem albumu"""
    music = {'name': artist, 'album': album_title}
    if song_number:
        music['song_number'] = song_number
    return music

while True:
    print("\nWprowadź nazwisko artysty i tytuł albumu: ")
    print("(jesli chcesz skończyć nacisnij 'q')")
    
    artist = input("Artysta: ")
    if artist == 'q':
        break
    title = input("Tytuł albumu: ")
    if title == 'q':
        break

    album_info = make_album(artist.title(), title.title())
    print("\n", album_info)
