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
