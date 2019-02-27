# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:43:12 2019

@author: SRathod2
"""

#Input = input("Enter the password : ")



# Operators in python: 
    #Special operator
    
alist = [10,20,30,40]
30 in alist
    
    

pswd = input("Enter the password : ")

if "#" in pswd or "$" in pswd or "@" in pswd:
    if len(pswd) >= 6 and len(pswd) <= 12:
        print("Valid Password")
    else:
        print("Invalid Password")


###################    
ip = input("Enter the IP : ")
if ip.count(".") = 3:
    

## Break commnad 
# Break : To come out of the loop if some condition is met



userinput = int(input("Enter the value :"))
For val in range(1,10):
    if val == userinput:
        break
    print(val)
    
    
## continue - it skips the current iteration 
userinput = int(input("Enter the value :"))
For val in range(1,10):
    if val == userinput:
        continue
    print(val)
 


    
    