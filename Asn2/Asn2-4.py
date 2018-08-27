"""
Tara Walton
Assignment 2, Part 4

Calculate and print all numbers between 250 and 400 divisble by 5 OR 6.
Not both.

Output: index
"""

for index in range(250, 401, 1):
    div5 = index %5  #divisible by 5 =0
    div6 = index %6  #divisible by 6 =0
    if div5==0 and div6!=0:
        print (index, end = " ")
    elif div5!=0 and div6==0 :
        print (index, end = " ")
    else: print ("*", end = " ")

    
    
