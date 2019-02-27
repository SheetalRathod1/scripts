# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 11:19:14 2019

@author: SRathod2
"""

# Functions or Definitions or Modules 
#2 Types of functions

# 1. Builtin functions dir(__builtins__)
'''
print()
len()       : length of the object
input()     : capture data from keyboard
id()      : unique identity of any object
type()      : cross check type of object
isinstance() :
range(start,stop,step)
help()
dir()    
    
    
    
    
conversion functions
    list()
    tuple()
    set()
    dict()
    int()
    float()
    oct()
    str()
    
    
# UserDefined Functions
Function block starts with keyword defc
'''


def add(first,second):
    total = first + second
    return total

#Call to a Function

gettotal = add(10,20)
print(gettotal)


# Passing Arguments...................

'''
##Fixed Arguments............

def add(first,second):
    total = first + second
    return total

#Call to a Function

gettotal = add(10,20)
print(gettotal)




###Default aRGUMENTS..............

def add(first,second,third):
    total = first + second + third
    return total

#Call to a Function

gettotal = add(10,20,30)
print(gettotal)


gettotal = add()
print(gettotal)


gettotal = add(10)
print(gettotal)


gettotal = add(10,20)
print(gettotal)


gettotal = add(10,20,30)
print(gettotal)


if arguments are not passed it takes the default value as 0
eg: range()


###Keyword Arguments .........................

def add(first,second):
    total = first + second
    return total

## Calling function

gettotal = add(first = 10,second = 20)
print(gettotal)


gettotal = add(second = 20, first = 10)
print(gettotal)




###Variable Length Argument......................

 here * is used to display in the form of tuple 
 donot use * if you want to display in the form of list
 
 
def display(*val):
    print(val)
    for item in val:
        print(item)
        
# Calling Function

display(10,20,["java",20,"python"],40,50,60)



        
        
        

'''




    
    
    
    
    
     