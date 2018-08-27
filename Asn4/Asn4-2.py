"""
2.	Modify Asn4-2.py as follows: change only the main() and printMessage()
functions. Change printMessage() so that it takes a string argument and prints
it. Change main() so that it gets a string from the user (use input()) and
calls printMessage() with the user’s string as an argument.

#Asn4-2.py: Print a string entered by the user
#Input:  A string typed by the user
#Output: The user's string, printed to the screen
"""
def printMsg(user):
    '''Change this function so it takes an argument and prints it'''
    print("Your name is ", user)

def main():
    '''Change this function so it gets a string from the user and passes
       it to printMsg'''
    user = input("What is your name? ")
    printMsg(user)

main()

