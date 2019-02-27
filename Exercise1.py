# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:38:56 2019

@author: SRathod2
"""

#Write a program to capture any filename from keyboard(data.csv) and display filename and extension separately 


Filename = input("Enter the filename: ")
#Var = "Data.csv"
File = Filename.split(".")
print(File[0])
print(File[1])



# Write program to capture string and the output in terms of list




# 
name = "python is general purpose and python is interactive and python is cross platform language"
print(name.count("python"))
word = name.split(" ")
print(word)
print(len(word))
print()


# Write a program to remove all the  duplicates from the list

alist = [10,20,10,20,30,40,50,20,30,40,60,70,80,10]
alist.pop()
#sort()
print(alist)