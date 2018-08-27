"""
Tara Walton
1.	Asn5-1.py: complete this program that uses a dictionary to count the pronouns in gb.txt.
Asn5.py reads a file holding a list of pronouns (pronouns.txt).
Complete the functions in the programin order to count the number of times each pronoun occurs in gb.txt.
Complete the function show_counts() to print the number of times each pronoun occurs.
For full credit, print the pronouns in alphabetical order and only print the ones that have a
count greater than 0. Extra challenge for no extra credit: Print the pronouns in order of frequency,
with the most frequent first.
"""

#Count pronouns in a text file
import string

text_filename = 'gb.txt'  #Count pronouns in this file
pronoun_filename = 'pronouns.txt'  #List of pronouns

def readfile_string(fname):
    '''Return contents of a text file as a lower-case string'''
    pass  #You can take this out or leave it - it doesn't matter
    #Open the file for reading
    f= open(fname, 'r')
    text = f.read()
    f.close()
    for punc in string.punctuation:
        text = text.replace(punc, '')  
    return text.lower()  

def count_pronouns(word_list, pronoun_list):
    '''Returns a dictionary with words and their counts
       word_list is a list of words from the text file
       pronoun_list is a list of English pronouns'''
    
    #print(word_list)       #If you want to see what word_list and...
    #print()
    #print()
    #print(pronoun_list)    #pronoun_list look like you can print them here
    pronoun_dict = {}       
    for word in word_list:  #For each word in word_list
        if word in pronoun_list:#  If the word is a pronoun then
            if word not in pronoun_dict:    
                pronoun_dict[word] = 1
            else:                           
                pronoun_dict[word] += 1

    return pronoun_dict

def show_counts(pronoun_dict):
    '''Print prounouns and their counts; print only those with counts > 0
       pronoun_dict is the dictionary of pronouns with their counts'''
    print("The pronouns (and their counts) used in alphabetical order: ")
    keys = list(pronoun_dict.keys())    #Sort the list of keys
    keys.sort()                         #For each key in the key list
    for key in keys:
        if pronoun_dict[key] > 0:
            print(key + ': ', pronoun_dict[key])

#Don't change anything below this point
def main():
    gb = readfile_string(text_filename) #gb is the contents of the text file (a string)
    gb_words = gb.split()  #Split file contents into a list of words
    pronouns = readfile_string(pronoun_filename)
    pronoun_list = pronouns.split()
    pronoun_dict = count_pronouns(gb_words, pronoun_list)
    show_counts(pronoun_dict)

main()
