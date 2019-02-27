# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:45:26 2019

@author: SRathod2
"""

############ String Methods###########
# Everything in Python is Object 
#Every object contains set of methods


name = "python"

# Upper and lower case oncversion
print(name.capitalize())
print(name.strip())     # removes the spaces from both the ends 

var = "python programming"

print(var.isalnum())   # returns True as there is a space involved. Hence it identifies as alphanumeric 
# if there are only alphabets without any spaces then it will identify as alpha 



str = "pypypypypy"

print(str.count("p"))   # returns 5 

