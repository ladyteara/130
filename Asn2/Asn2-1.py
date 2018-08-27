"""
Tara Walton
Assignment 2, Part 1

Print a short quote 1000X using a loop

Input : pause #used as a place holder for any user input
Output: quote
"""
print("What did the Dalek say to the human?")
pause = input("Give up? ")
quote = "EXTERMINATE!"
for index in range(1, 1001, 1): #print from 1 to 1000
    print(index, quote)
