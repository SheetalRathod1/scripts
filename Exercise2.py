# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:31:29 2019

@author: SRathod2
"""

Filename = input("Enter the filename: ")
FileExt = Filename.split(".")

if FileExt[1] == "py":
    print("python file")
    
elif FileExt[1] == "txt":
    print("Text file")
    
elif FileExt[1] == "csv":
    print("csv file")
    
elif FileExt[1] == "pl":
    print("perl file")

elif FileExt[1] == "ksh":
    print("korn shell file")
    
else:
    print("none")
    
    
 ######
str1 = input("Enter the String: ")
if str1.isupper():
    
    print("This is upper")
    print("Converted to Lower : ", str1.lower())
elif str1.islower():
    print("This is lower")
    print("Converted to Upper : ", str1.upper())
    

#######


if len(string) < 10:
    print("String is too small")
    
elif len(string) > 30:
    print("String is too big")





    
    