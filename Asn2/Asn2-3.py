"""
Tara Walton
Assignment 2, Part 3

Calculates the future tuition of a university

Input : tuition
Constants (3%)
Output: tuition (after 10 years)
"""
tuition = input("What is the current tuition at the school? ")
tuition = int(tuition)
for dummy in range(10):
	tuition = round(tuition * 1.03, 2)
	
print("\nAfter 10 years, and given a 3% increase each year, the tuition will be $" + str(tuition))

