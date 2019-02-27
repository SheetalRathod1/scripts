# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:30:09 2019

@author: SRathod2
"""

# Built-in Functions

# 1. Input 

name = input("Enter the name: ")
print ("You entered :", name)


First = input("Enter 1st value:")
Second = input("Enter 2nd value:")
 Total = First + Second
 Print("Sum of two numbers :", total)
 
 
 
 # + operator performs concatenation and addition as well 
 # Hence to add 2 numbers ensure the input is type casted (converted to int) to capture a numeric value 
 
 # Type cast to capture the numbers 
 First = int(input("Enter 1st value:"))
Second = int(input("Enter 2nd value:"))
 Total = First + Second
 Print("Sum of two numbers :", total)
 
 
 
 # 2. Range
 
 # Syntax: range(start,stop,step)
print(list(range(1,10)))
print(tuple(range(3,9)))
 
print(list(range(2,10,2))) 

print(list(range(1,100,2))) 







