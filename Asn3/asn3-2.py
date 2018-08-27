"""
Tara Walton
Assignment 3, Part 2
Description:
2. Modify your Asn3-1 program to print only the odd numbered characters
from the same string (character 1, character 3, etc).
Use a loop – do not use string slicing. Save your program as Asn3-2.py.

Input:  userString
Output: odd characters in userString
"""

userString = input("What string would you like to dissect? ")
for index in range(1, len(userString), 2):
    print(userString[index], end = "-")
