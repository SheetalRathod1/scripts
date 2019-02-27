# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:19:43 2019

@author: SRathod2
"""

#Statement in Python

#1. Conditional Statements in Python

name = "Python"

If name.isupper():
    print("This is upper")
    
elif name.islower():
    print("This is lower")
    
else:
    print("None is this")


#2. Control statements
   # For Loop
   # While Loop
   
for val in range(1,10):
    print(val)
    
    print("-------------------")    
for val in range(2,10,2):
    print(val)

    print("-------------------")        
for val in range(1,10,2):
    print(val)
    
    print("-------------------")    
for val in range(100,1,-1):
    print(val)
    
    

#for loop with string
name = "python"
for char in name:
    print(char)
