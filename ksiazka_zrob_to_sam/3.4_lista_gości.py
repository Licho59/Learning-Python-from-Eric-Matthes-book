# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:51:49 2017

@author: Leszek
"""
#invitations for my favorite guests after some changes
guests = ['president obama', 'julia roberts', 'elon musk', 'amy adams', 'clint eastwood']
for guest in guests:
    invitation = "\n\t\tDear " + guest.title() + ",\n\n please accept the invitation for dinner at my residence."
    print(invitation) 