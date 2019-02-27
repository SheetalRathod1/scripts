# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:15:42 2019

@author: SRathod2
"""
#
#import os
#print(os.listdir("C:\\Python"))
#
#print(os.extsep)



#for file in os.listdir():
    
# program to     
#import csv
#with open("employees.csr","r") as fobj:
#    reader = csv.reader(fobj)
#    for line in reader:
#        print(line)
#        
        
    
    
    
import os 
for file in os.listdir():
    if os.path.isfile(file):
        filesize = os.path.getsize(file)
        print("Filename : ",file)
        print("Filesize : ",filesize, "bytes")
            