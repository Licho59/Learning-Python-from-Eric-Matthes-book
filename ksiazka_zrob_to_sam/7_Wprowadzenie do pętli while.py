# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:47:44 2017

@author: Leszek
"""

#Pętla while w działaniu
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 #difference between loops while and for: 
                        #while is running until it is False when
                        #loop for is running through given sequence of numbers
                            
#Wyjscie z pętli aby zakończyć działanie programu
prompt = "\nPowiedz mi cos o sobie, a wyswietlę to na ekranie:"
prompt += "\nNapisz koniec, aby zakończyć działanie programu. "
message = ""
while message != 'koniec':
    message = input(prompt)
    print(message) #program się nie skończy nawet po wpisaniu Koniec

prompt = "\nPowiedz mi cos o sobie, a wyswietlę to na ekranie:"
prompt += "\nNapisz koniec, aby zakończyć działanie programu. "
message = ""
while message != 'koniec':
    message = input(prompt)
    if message != 'koniec': #po użyciu 'koniec' program nie wykonuje
                            #polecenia print a tym samym nie ładuje input
        print(message)
        
# Użycie flagi
prompt = "\nPowiedz mi cos o sobie, a wyswietlę to na ekranie:"
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

active = True #flagą jest zmienna active
while active:
    message = input(prompt)
    
    if message == 'koniec':
        active = False # active jako flaga z wartoscią False
                        #przerywa pętlę while
    else:
        print(message)
        
#Użycie polecenia break do opuszczenia pętli
prompt = "\nPodaj nazwy miast, ktore chciałbys odwiedzić:"
prompt += "\n(Gdy zakończysz podawanie miast, napisz 'koniec'.) "

while True:
    city = input(prompt)
    
    if city == 'koniec':
        break    #przerywa działaie pętli while i tym samym input
    else:
        print("Chciałbym odwiedzić " + city.title() + "!")

#Użycie polecenia continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue  #continue wraca na początek pętli
    else:
        print("\n", current_number)
        
#Unikanie pętli działającej w nieskończonosc - klawisze ctrl + c
x = 1
while x < 5:
    print(x) #pętla nie zatrzymuje się (1,1,1,1,..)

x = 0
while x < 5:
    x += 1
    if x == 5:
        break
    else:
        print(x)
        
        