# -*- coding: utf-8 -*-
"""
Created on Sun May 14 21:31:38 2017

@author: Leszek
"""

# 9.11 Zaimportowana klasa Admin
import upa

przywileje = upa.Privileges(['zakłada konto', 'usuwa z forum', 'może wszystko'])
forum_admin = upa.Admin('jakub', 'tlalka', 26, 'man', 'warszawa', przywileje)
forum_admin.privileges.show_privileges()
