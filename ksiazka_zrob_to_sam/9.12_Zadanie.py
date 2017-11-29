# -*- coding: utf-8 -*-
"""
Created on Sun May 14 21:53:55 2017

@author: Leszek
"""
# 9.12 Wiele modułow
from admin import Admin, Privileges

uprawnienia = Privileges(['dostęp do danych', 'kasowanie', 'inne'])
new_admin = Admin('leszek', 'tlalka', 58, 'man', 'bełchatow', uprawnienia)
new_admin.privileges.show_privileges()
