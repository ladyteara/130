"""
Tara Walton
Assignment 2, Part 2

Calculates the area of a pizza (3x).

Input : diameter
Output: area (rounded to 2 places)

Notes:  Allow 3 iterations for full credit
        area = pi * r^2
"""
sum = 0
for pizza in range(3):
#input
	diameter = input("What size pizza did you order (diameter in inches)? ")
	diameter = int(diameter)
#calculations
        import math
        radius = diameter / 2
	area = round(math.pi * radius**2, 2)
#output
	print("That's", area, "square inches of pizza!")
	sum = round(sum + area, 2)
print("\nThat's a total of", sum, "square inches of pepperoni goodness!")
print("I hope you're hungry!")



