# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:51:49 2017

@author: Leszek
"""
#invitations for my favorite guests because of bigger table
guests = ['president obama', 'julia roberts', 'elon musk', 'amy adams', 'clint eastwood']
absent_guest = guests.pop(0).title()
print(absent_guest + " can not participate in the dinner.")
guests.append('darek rybarczyk')
print("There will be 3 additional guests because bigger table is available")
guests.insert(0, 'tom hanks')
guests.insert(2, 'krysia tlałka')
guests.append('marek grechuta')
for guest in guests:
    invitation = "\n\t\tDear " + guest.title() + ",\n\n please accept the invitation for dinner at my residence."
    print(invitation)
#bigger table will not be delevered
print("I can invite only 2 persons for the dinner in my residence.")
print(guests)
guest_not_invited_1 = guests.pop(0).title()
print("\tDear " + guest_not_invited_1 + "\nI have to apologize for canceling the invitation for dinner.")
guest_not_invited_2 = guests.pop(0).title()
print("\tDear " + guest_not_invited_2 + "\nI have to apologize for canceling the invitation for dinner.")
guest_not_invited_3 = guests.pop(1).title()
print("\tDear " + guest_not_invited_3 + "\nI have to apologize for canceling the invitation for dinner.")
guest_not_invited_4 = guests.pop(1).title()
print("\tDear " + guest_not_invited_4 + "\nI have to apologize for canceling the invitation for dinner.")
print(guests)
guest_not_invited_5 = guests.pop(1).title()
print("\tDear " + guest_not_invited_5 + "\nI have to apologize for canceling the invitation for dinner.")
guest_not_invited_6 = guests.pop().title()
print("\tDear " + guest_not_invited_6 + "\nI have to apologize for canceling the invitation for dinner.")
for guest in guests:
    print("\n\tDear " + guest.title() + "\nI am really happy to have you at today's dinner.")
del guests[:]
print(guests)