# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 17:59:59 2017

@author: Leszek
"""

# 8.16 Polecenia importu
import making_shirts

from making_shirts import make_shirt

from making_shirts import make_shirt as ms

import making_shirts as mgs

from making_shirts import *

making_shirts.make_shirt('45', 'leszek tlałka')
making_shirts.make_shirt(size = '39', text = 'jakub tlalka')

