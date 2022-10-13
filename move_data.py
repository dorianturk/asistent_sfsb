# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 14:53:10 2022

@author: zsk
"""
import os
"""
#premjestanje datoteke u old
"""

source = "D:/asistent_sfsb/mehanika2/"
destination = "D:/asistent_sfsb/data_old/"
files = os.listdir(source)
 
for f in files:
    os.replace(source + f, destination + f)