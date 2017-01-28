# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 19:05:18 2017

@author: Niranjan
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:27:45 2017

@author: Niranjan
"""

from __future__ import print_function

grades = []
num = float(input("Enter marks:"))
grades.append(num)

num = float(input("Enter marks:"))
grades.append(num)

num = float(input("Enter marks:"))
grades.append(num)

num = float(input("Enter marks:"))
grades.append(num)

num = float(input("Enter marks:"))
grades.append(num)

minimumgrades = min(grades)
grades.remove(minimumgrades)

minimumgrades = min(grades)
grades.remove(minimumgrades)

avg = sum(grades)/ len(grades)
print("Average Grades: {0:.2f}".format(avg))

# with for loop 
for i in range(6):
    num = float(input("Enter Marks:"))
    grades.append(num)
    i= i + 1

minimumgrades = min(grades)
grades.remove(minimumgrades)

minimumgrades = min(grades)
grades.remove(minimumgrades)

avg = sum(grades)/ len(grades)
print("Average Grades: {0:.2f}".format(avg))    


#Split and Join method
line = ["To","Be","or", "not","to","be"]
print(" ".join(line))

line1 = ["Snap","Crackle","Pop"]
print(", ".join(line1))

t = 5,7,6,2
print(t)
print(len(t),max(t),min(t),sum(t))
print(t[0],t[-1],t[:2])

#swap numbers
x = 6
y =5
y,x = x,y
print(x,y)

#Nested List
regions = [("TX",55),("DC",24.5),("NY",32),("CA",63.7)]
print("The 2010 Population of the region "+  str(regions[1][0]) + " was " +  str(regions[1][1]))
total_population = regions[0][1] + regions[1][1] + regions[2][1] + regions[3][1]
print("Total Population of US in 2010: {0:.1f} million.".format(total_population))

#Mutable list
list1 = ['a','b']
list2 = list1
list2[1] = 'c'
print(list1)

#Copying List
list1 = ['a','b']
list2 = list(list1)
list2[1] = 'c'
print(list1)

#Sorting
list1 = [6,4,-5,4.5]
list1.sort(reverse = True)
list1.sort()
print(list1)
list2 = ["ha","hi","B","7",'a']
list2.sort()
print(list2)

list1 = [ chr(177),"cat","cAr","Dog","EGG","5" + chr(162)]
list1.sort()
print(list1)

list2 = [("G",5),("E",6),("G",4),("E",10)]
list2.sort()
print(list2)


#if statement
num1 = input("Enter 1st number:")
num2 = input("Enter 2nd number:")
if num1 > num2:
    larger_num = num1
else:
    larger_num = num2

print("The larger number is:" + str(larger_num))    

ans = input("Enter number of gallons:")
if(0.5<= ans <= 1):
    print("Good,",end=" ")
else:
    print("No,",end =" ")

print("3/4th gallon")    

#multiple if
first_num = input("1st number:")
second_num = input("2nd number:")
third_num = input("3rd number")   

max_num = first_num

if second_num > max_num:
    max_num = second_num
if third_num > max_num:
    max_num = third_num

print("max number :" + str(max_num))   

#nested if-else
color = input("red or blue:")
mode = input("steady or flashy:")

result = ""

if color == "blue":
    if mode == "steady":
        result = "Clear"
    else:
        result = "Unclear"

else:
    if mode == "steady":
        result = "Rainy"
    else:
        result = "Snow"

print(result)

#nested if-else
cost = input("input cost:")
revenue = input("input revenue:")

if cost == revenue:
    result = "Break Even"
else:
    if cost < revenue:
        profit = revenue - cost
        result = "Profit is ${0:,.2f}".format(profit)
        
    else:
        loss = cost - revenue
        result = "Loss is ${0:,.2f}".format(loss)
        
print(result)        
        
        
 
    