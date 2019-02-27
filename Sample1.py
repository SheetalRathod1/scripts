# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 11:05:06 2019

@author: SRathod2
"""

# for string manipulation/Slicing
# syntax : var[start:stop:step]

var = "unix shell scripting"
print(var)
print(var[0])  
print(var[5])
print(var[0:5])
print(var[0:6:2])
print(var[::4])
print(var[0:12:3])

#Fetch 
print(var[3:8])


#Fetch characters in reverse order 
# [-1] means fetch last character
print(var[-1])

#Fetch the entire string
print(var[::])


#Fetch first 5 characters
print(var[:6])

#Reverse the string
print(var[::-1])





# String Concatenation 
# Use + operator as a concatenantion operator

first = "python"
second = "programming"

final = first + " " + second
print(final)



# List (Array in C)

#In C : int val[3] = {10,20,30}
#In python : val = [10,20,30]

# List is set of elemenrs 
# elements can be set of numbers or set of strings or combination
# list elements are defined in []

alist = [10,20,30]
blist = ["unix","python","c"]
clsit = [10,20,"unix",4000,"python"]

print(alist[0])     # 10
print(alist[0:3])   # 10 20 30
print(alist[-1])   # 40

alist[0] = 1000
print("updtaed list: ",alist)



# List concatenation

alist = [10,20]
blst = [30,40]
final = alist + blist 

print(final)



alist = [[10,20],[30,40],[50,60]]


# Tuple
# Tuple is set of elemenrs 
# elements can be set of numbers or set of strings or combination
# Tuple elements are defined in ()
# Tuple is read only, elements inside the tuple cannot be modified

atup = (10,20,30)
btup = ("perl","java","hadoop","spark")
print(atup)
print(btup[0:4])
atup[0] = 10000

print("updated Tuple :",atup)     # will throw an error "object does not support item assignment"


# Dictionary 
# contains elememts in form of keys and values
# Keys are always unique
# dictionary elements are defined in {}

#Syntax : Dictname = {key:value , key:value , key:value}
# example:  Book = {"chap1":10 , "chap2":20 , "chap3":30}
#           Data = {10:20,30:40,50:60}



Book = {"chap1":10 , "chap2":20 , "chap3":30 ,"chap1":1000}
print(Book["chap1"])

# Add more key values to existing dictionary

Book["chap4"] = 40

print("updated dictionary : ", Book)

Book["chap5"] = 50

print("updated dictionary : ", Book)

 

# set

#Set is group of elements
# Set elements are defined in {}
#Indexing is not permitted for set

aset = {10,20,30,40,10,20}
print(aset)   # prints 10,20,30,40   - Prints only unique values


# converting list to set 
alist = [10,20,30,40,10,20]
print(set(alist))      # will display only unique values in form of Set 


# Dispay output in tuple format

print(tuple(alist))


























