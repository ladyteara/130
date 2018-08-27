"""
Tara Walton
2.	Asn5-2.py: complete this program that uses a dictionary to count the number of medals won
by countries at the Summer Olympics between 1896 and 2008. Designs are included in comments inside
the functions—write the code to carry out the designs. Your completed program should: 
a.	print the number of countries winning medals (according to this data set)
b.	print the countries and their medal counts in alphabetical order
c.	print the country with the most medals and its count
d.	allow the user to query the program to find out the medal count of any country.

Additional challenges for no extra credit
-Print the countries in order of the number of medals won, with the most medals first.
=Print the countries in order of “medal points” won, where a country receives 3 points
for a gold medal, 2 points for a silver medal, and 1 point for a bronze medal.
Also list the number of each kind of medal won by the country.

"""
#Use a dictionary to count the number of medalists from each country
input_fname = 'Summer Olympic medallists 1896 to 2008.csv'

#Fields
#city: 0, year: 1, sport: 2, discipline: 3, last_name: 4, first_name: 5
#country: 6, gender: 7, event: 8, event_gender: 9, medal: -1

def readfile(fname):
    '''Return a list of lines from the file (each line is a string)'''
    f= open(fname, 'r')
    lines = f.readlines()
    f.close()

    return lines

def build_country_dict(lines):
    '''Return a dictionary in form of {country: count}, where country is
       the country code and count is the number of medals won by athletes
       from that country'''
    
    country_dict = {}       
    for i in range(1, len(lines)):  
        data = lines[i].strip().split(',')
        country = data[6]   
        if country not in country_dict:
            country_dict[country] = 1
        else:
            country_dict[country] += 1

    return country_dict

def show_country_counts(country_dict):
    '''Show the country names and medal counts in alphabetical order'''

    noc_list = list(country_dict.keys())
    noc_list.sort()
    print(len(noc_list), "countries have won medals in the Olympics")
    pause = input("Press enter to continue...")
    for noc in noc_list:
        print(noc, ":", country_dict[noc])
    pause = input("Press enter to continue...")

    #Don't return anything

def show_highest_count(country_dict):
    '''Use country_dict to print the country with the highest medal count
       and its number of medals'''
    
    max_count = 0       #Set max_count to 0
    max_country = None  #Set max_country to None
    for country in country_dict:
        if country_dict[country] > max_count:
            max_count = country_dict[country]   #Set max_count to the country's count
            max_country = country              #Set max_country to the country
    print("The highest count goes to: ", max_country, "with", max_count, "medals.")
    
    #Don't return anything

def query_country(country_dict):
    '''Allow user to type in a country code; print how many medals
       that country has won; quit when the user types q'''
    
    query = input("What country code would you like to search for? (enter 'q' to quit)")
    query = query.upper()
    while query != 'Q':
        print(query, ":", country_dict[query])
        query = input("What country code would you like to search for? (enter 'q' to quit)")
        query = query.upper() 
        
    #Don't return anything

def rank_countries(country_dict):  #OPTIONAL
    '''Extra challenge: print the countries in order of number
       of medals won, with most medals first'''
    pass  #You can leave this statement or take it out - it doesn't matter

def super_challenge(country_dict):  #OPTIONAL
    #data[10] medal type
    '''Super extra challenge: print the countries in order of "medal points",
       where a country gets 3 points for gold, 2 for silver, and 1 for bronze,
       then list the number of each kind of medal won by the country'''
    pass  #You can leave this statement or take it out - it doesn't matter

def main():  #Don't change anything below here
    lines = readfile(input_fname)
    country_dict = build_country_dict(lines)
    show_country_counts(country_dict)
    show_highest_count(country_dict)
    query_country(country_dict)
    rank_countries(country_dict)
    super_challenge(country_dict)

main()

