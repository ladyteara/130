"""
Tara Walton
Assignment 3, Part 3
Description:
3. Modify your Asn3-2 program to print the first character from the string;
after that, it should print every 3rd character.
Use a loop – do not use string slicing. Name the program Asn3-3.py.

Input : userString
Output: every third character in userString
"""

userString = input("What string would you like to dissect? ")
for index in range(0, len(userString), 3):
    print(userString[index], end = "-")

