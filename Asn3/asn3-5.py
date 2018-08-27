"""
5. Write a program to read a text file and remove all punctuation.
Make the file name a variable called fname and give it a value near
the beginning of your program. For practice, use the file gb.txt,
provided in the AssignmentDescriptions\Asn3 folder.
Your program should print the contents of the file to the screen,
with all punctuation removed. Save your program as Asn3-5.py

6. Additional challenge for no extra credit:
Extend Asn3-5.py to count and print the number of words in the file.
For our purpose, a word is anything with a space before or after it.
Hint: There is a way to count the number of words using the string split()
method but it involves information from chapter 5.
Another way to do it is to use a loop to count the number of spaces
and newlines in the text.

Input : gb, fname
Output: gb (revised)

NOTE:string.punctuation contains all punctuation
"""
#necessary tools
import string
print("Please enter the name of a .txt file without the extension. File must be located in the same folder as this program.")
fname = input("What file would you like to read? ")

#reading file
f = open(fname + ".txt", 'r')
text = f.read()
#count double hyphens to remove extra "words" in word count
hyphens = text.count('--')

#display old text
print("BEFORE: With Punctuation")
print(text)

#removing punctuation (loop)
charDel= string.punctuation
for char in charDel:  
    text = text.replace(char, '')

#display new text
print("AFTER: Without Punctuation")
print(text)

#writing file
#fchanged = open(fname + "_changed.txt", 'w')    
#fchanged.write(text)
#print ("Writing complete to file: ", fname + "_changed.txt")

#closing files
f.close()
#fchanged.close()

#challenge - word count
print ("Word Count: ", text.count(' ') - hyphens)

