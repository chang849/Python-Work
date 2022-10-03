# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:48:17 2021

@author: sethc
"""

#Author:Seth Chang
#Date:4/22/21

#ask user the number of elements and store that to variable n
z=int(input("enter number of elements:"))
             

#run a loop until n and ask n numbers as an input from user. Store the given numbers in a list mylist using append()
mylist=[]
for i in range (0,z):
    z1=int(input("Enter numbers:"))
    mylist.append(z1)

#define the function  calculate_sum() here
def calculate_sum (mylist,z):
    for mister in range (0, len(mylist)):
        if(z==0):
            return 0
        else:
            return mylist[z-1]+calculate_sum(mylist,z-1) 
total=calculate_sum(mylist, len(mylist))
print ("sum of list:", total)

        
#write code that will run a loop on the list and store the sum in a variable sum and return sum in the last statement of the function.
    

#define the function  calculate_average() here
def calculate_average (mylist,z):
    for mister in range (0, len(mylist)):
        if(z==0):
            return 0
        else:
            return mylist[z-1]+calculate_average(mylist,z-1)/5
average=calculate_average(mylist, len(mylist))
print ("average of list:", average)

#define the function  calculate_range() here
def calculate_range (mylist,z):
    for mister in range (0, len(mylist)):
       return max(mylist)-min(mylist)
Range=calculate_range(mylist, len(mylist))
print ("range of list:", Range)
print ( "Max number:", max(mylist))
print ( "Minimum number:", min(mylist))
#write code that will run a loop on the list and store the range in a variable range, minimum in a variable min, maximum in a variable max and return range, min, and max in the last statement of the function.
# you can return multiple value from a function as a set.



#call calculate_sum()
callable(calculate_range(mylist, z))
print(Range,max(mylist),min(mylist))

#print sum
callable(calculate_sum(mylist, z))
print(total)

#call calculate_average()
callable(calculate_average(mylist, z))


#print average
print(average)

#call calculate_range()
#print range, minimum, maximum 


