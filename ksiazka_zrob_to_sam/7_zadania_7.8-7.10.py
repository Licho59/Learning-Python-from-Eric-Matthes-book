# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:13:36 2017

@author: Leszek
"""

#7.8 Bar
sandwich_orders = ['jarska', 'drobiowa', 'serowa', 'jajeczna', 'bigmac',
                   'z wędliną', 'rybna', 'pomidorowa']
finished_sandwiches = []

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()
    print("Kanapka " + prepared_sandwich + " przygotowana!")
    finished_sandwiches.append(prepared_sandwich)

print("----Przygotowano następujący zestaw kanapek:---- ")
for sandwich in finished_sandwiches:
    print("\t" + "Kanapka " + sandwich)
    
#7.9 Brak pastrami
sandwich_orders = ['jarska', 'drobiowa', 'serowa', 'jajeczna', 'bigmac',
                   'z wędliną', 'rybna', 'pomidorowa']

sandwich_orders.insert(0,'z pastrami')
sandwich_orders.insert(3, 'z pastrami')
sandwich_orders.append('z pastrami')
print(sandwich_orders)

print("\n---There are no more pastrami sandwiches available!---")
while 'z pastrami' in sandwich_orders:
    sandwich_orders.remove('z pastrami')
print("\nSandwiches still available:")
for sandwich in sandwich_orders:
    print("\t" + sandwich)
    
# 7.10 Wymarzone wakacje
holidays_poll = {}
polling_active = True
while polling_active:
    name = input("What's your name?: ")
    favorite_holidays = input("If you could go to only one place in\
    the world what would be your choice for holidays?: ")
    
    holidays_poll[name] = favorite_holidays
    if len(holidays_poll) == 4:
        break
for name, favorite_holidays in holidays_poll.items():
    print("\nFor " + name.title() + " the best place to go for holidays is "
          + favorite_holidays.title() + "!")