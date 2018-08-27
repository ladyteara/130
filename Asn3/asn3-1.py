"""
Tara Walton
Assignment 2, Part 1
Description:
1.Write a program that accepts an input string from the user and
uses a loop to print each individual character from the string.
Name your program Asn3-1.py and save it in your Asn3 folder.

Input:  userString
Output: userString slices
"""

userString = input("What string would you like to dissect? ")
for index in range(len(userString)):
    print(userString[index], end = "-")

