# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:27:35 2019

@author: SRathod2
"""

#.......Libraries.........

'''
Builtin Libraries - builtin libraries are installed/copied with python setup
path: C:\Anaconda3\Lib


math
os
sys
time
datetime
logging
shutile

#Method 1
import math
print(math.ceil(4.9))
print(math.log(3))


#Method2 - Accessing methods with alias name
 import math as m
 print(m.ceil(4.9))
 print(m.tan(3))


#Method3 - importing only required methods. 
#  . is not required here

from math import ceil,log
print(ceil(4.9))
print(log(3))


#Method4 - Import all methods
from math import *
print(ceil(4.9))



import os
print(os.listdir())    #...lists the libraries in the current path


print(os.listdir("C:\\"))  #.....lists the libraries in C:

    
os.unlink("rangetest.py")

    
    
    
    



Third Party Libraries
Based on requirement(read/write excel, db connectivity, mail).. the developer has to install third party library

path: C:\Anaconda3\Lib\Site Packages