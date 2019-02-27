# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:58:21 2019

@author: SRathod2
"""

# List Methods


alist = [10,20,30]

print(alist.append(40))   # To add single element to the list

print(alist)

alist.extend([50,60,70])   # To add multiple elements to the list

print("After Extending: ", alist)


#print(alist.reverse())  # Returns None as reverse happens in place hence first reverse and then print 

alist.reverse()
print(alist)

alist.sort()
print(alist)

popitem = alist.pop(5)
print("removed item: " alist)