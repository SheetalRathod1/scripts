# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:12:26 2019

@author: SRathod2
"""
'''
###File Handling############

Flat Files - Files (log csv conf txt) Files having purely data 

Third Party Files - (pdf xls xlsx doc ppt mp4)



How to open files in python

obj = open(filename, mode)

eg: fobj open("customers.txt","r")      ---> file opened in read mode
fobj open("customers.txt","w")          ---> file opened in write mode
fobj open("customers.txt","a")          ---> file opened in append mode



Read mode 

case 1 : if file is not found .... it displays error message
case 2 : if file exists ...it displays the file content

Write Mode 
case1: If file is not available ... it creates the files and writes the data
case2: If file exists ... it overwrites the data and starts from scratch 


Append Mode 
case1: If file is not available ... it creates the files and writes the data
case2: If file exists ... it appends the data at the end of the file



'''

#string = input("The String is : ")
#
#
#fobj = open("demo.txt","w")    # if path is not given it take sthe path where the program is stored
## fobj = open("C:\\Python\\Programs\\demo.txt") ----- use \\ (double backslash) for giving complete file path
## fobj = open("C:/Python/Programs/demo.txt") ----- use / (single forwardslash) for giving complete file path
#fobj.write(string)
#
##fobj.write("python programming\n")
##fobj.write("perl programming\n")
##fobj.write("ruby programming\n") 
# 
#fobj.close

#
#fobj = open("demo.txt","a")
#fobj.write("\n")
#odd = range(700,400,1)
#fobj.write(odd)
#fobj.close()
#
#
#
#
## File reading operations 
#
##Reading line by line .....
#fobj = open("demo.txt")             # Default mode is read mode... so if mode is not mentioned, it will open the file in read mode
#for line in fobj:
#    line = line.strip() #...............removes the whitespace at end of each line
#    data = line.split(",")   # ...........splits the line with , as delimiter
#    print(data)
#    print(data[0])   #....... displays 1st field
#    
    

# Reading data from csv file 

fobj = open("C:\\Python\\datasets\\employees.csv")

#fcount = 0
#mcount = 0
#for line in fobj:
#    line = line.strip()
#    if "Female" in line:
#        fcount = int(fcount) + 1
#    if "Male" in line: 
#        mcount = int(mcount) + 1
#print(fcount)
#print(mcount)
#fobj.close()
#
#
#line = fobj.readline()    #....reads the line and moves the cursor to next line ...reads the header and moves to next line
#for line in fobj: 
#    line = line.strip()
#    line = line.split(",")
#    if int(line[4]) > 100000:
#        print(line)
#fobj.close()



fr = open("C:\\Python\\datasets\\employees.csv")
fw = open("demo.txt","w")


for line in fr:
    line = line.strip()
    line = line.replace("Business Development","Information Technology")
    fw.write(line)
    fw.write("\n")
fw.close
fr.close




#
#import time
#filename = time.strftime("%d_%b_%Y.log")
#print(filename)
#
#
#
#import time
#filename = time.strftime("%d_%b_%Y.csv")
#print(filename)
#





# Context Manager
#
#with open("employees.csv","r") as fobj:
#    for line in fobj:
#        print(line)
#        
#data = fobj.readlines()    
#for line in data[4:10]
#    print(line)
#    

        