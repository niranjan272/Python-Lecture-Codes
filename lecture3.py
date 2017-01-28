# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:06:59 2017

@author: Niranjan
"""

from __future__ import print_function

#elif loop
num1 = input("enter 1st number:")
num2 = input("enter 2nd number:")

if num1 > num2 :
    print("The larger value is:",str(num1))
elif num2 > num1:
    print("The larger value is:", str(num2))
else:
    print("Numbers are equal") 

#elif    
num1 = str(input("enter 1st number:"))
num2 = str(input("enter 2nd number:"))

if num1.isdigit() and num2.isdigit():
    print(int(num1) + int(num2))
elif not num1.isdigit():
    if not num2.isdigit():
        print("enter numbers")
    else:
        print("first number is not digit")
else:
    print("2nd number is not digit")        
    
    
#while loop
num = 1
while num <=5:
    print num
    num += 1
    
responses = ('1','2','3')
response = '0'
while response not in responses:
    response = str(input("Enter 1,2, or 3:"))
    if response == '1':
        print ("Plastic")
    if response == '2':
        print("Risebud")
    if response == '3':
        print("That's all")
        

count = 0
total = 0
        
print("enter -1 to terminate:")
num = input("enter number:")
min_num = num 
max_num = num
while num!= -1:
    count +=1
    total += num
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    num = input("enter -1 to terminate:")   
    
if count > 0:
    print("min:",min_num)
    print("max:",max_num)
    print("avg:",total/count)
else:
    print("No nonnegative numbers entered")   
    
    
#Countinue and Break
list1 = ["one",23,"two",7]
i = 0
flag = False
while i <len(list1):
    x = list1[i]
    i +=1
    if not isinstance(x,int):
        continue
    else:
        if x % 11 == 0:
            flag = True
            print(x," is the interger divisible by 11")
            break
    
if not flag:
    print("No number is divisible by 11") 

#for loop    
for i in range(2,6):
    print (i,i*i)    


for m in range(1,6):
    for n in range(1,6):
        print(m," * ",n, "=",m*n,"\t",end = "")
    print()        

#for loop for list
months = ["Jan","Feb","Mar","Apr","May"]
for month in months:
    if 'r' in month.lower():
        print (month)
        
        
#fucntion
def ftoc(t):
    convertedtemp = int((5/9)*(t-32))
    print(convertedtemp)
    return convertedtemp

temp = input("enter temp:")
celciustem = ftoc(temp)       
print (str(celciustem))
    