"""
4.	Complete Asn4-4.py to calculate the shooting percentages of all the NBA
teams in the 2009 season (use the file 2009_shots.csv). Use the shots programs
written in class that use a dictionary as a model. For full credit, use a dictionary
in which the keys are the NBA teams (from the first column) and the values are lists
([shots_made, shots_attempted]). Print the teams and their shooting percentages in
alphabetical order (the team names are the ones in column 1 of the spreadsheet).
The structure of the program is provided in the given Asn4-4.py.

5.	Modify Asn4-4.py to print the teams in order of shooting percentage, from
highest to lowest.
6.	Extend Asn4-4.py to print the teams’ overall shooting percentages and
also their 3 point shooting percentages
(three_point_shots_made/three_point_shots_attempted)


#Asn4-4.py: Calculate and print the shooting percentages of NBA teams in 2009
#Input:  A file holding a record of all shots taken during the 2009 season
#Output: A list of NBA teams, in alphabetical order and their shooting
#        percentages.
"""
filename = "2009_shots.csv"

def readfile(fname):
    '''Read the input file, return a list with all lines from the file'''
    f= open(fname, 'r')
    lines = f.readlines()
    f.close()
    
    return lines 

def build_dict(lines):
    '''Build and return a dictionary with shots for each team. The format is:
       {team: [shots_made, shots_attempted, 3pts made, 3pts attempted]
    from file [0:team, 1:player, 2:result, 3:shot, 4:x pos, 5:y pos]
       '''
    shots_dict = {}
    for i in range(1, len(lines)):
        data = lines[i].strip().split(',')
        shot = data[3].replace('a moute ', '')
        team = data[0]
        if team not in shots_dict:
            shots_dict[team] = [0, 0, 0, 0]
        result = data[2]
        if result == "made":
            shots_dict[team][0] += 1
            shots_dict[team][1] += 1
            if data[3] == "3pt":  
                shots_dict[team][2] += 1
                shots_dict[team][3] += 1 
        if result != "made":     
            shots_dict[team][1] += 1
            shots_dict[team][3] += 1

    return shots_dict

def calc_pct(shots_dict):
    '''Calculate the shooting percentages using the shots dictionary.
       Store the percentages in another dictionary, and return it.
       The format of the pct dictionary is {team: pct, 3pt pct}'''
    pct_dict = {}
    teams_list = list(shots_dict.keys())
    teams_list.sort()
    #print(teams)   #(test code)
    for j in range(len(teams_list)):
        team = teams_list[j]
        #print(team)    #(test code)
        if team not in pct_dict:
            pct_dict[team] = [0, 0]
            for t in pct_dict:
                pct_dict[team][0] = round(int(shots_dict[team][0])/int(shots_dict[team][1])*100, 1)
                pct_dict[team][1] = round(int(shots_dict[team][2])/int(shots_dict[team][3])*100, 1) 
#key error
    return pct_dict

def show_pct(pct_dict):
    '''Print the teams in alphabetical order and their shooting percentages'''
    teams = list(pct_dict.keys())   #list keys
    teams.sort()                       #alphabetize
    print("In alphabetical order...")
    for t in teams:                #use our list instead of the dictionary
        print(t + ': Shooting Percentage: ', pct_dict[t][0])
        print(t + ':  3 Point Percentage: ', pct_dict[t][1])
    
    #shooting = list(pct_dict.values())  #list values
    #shooting.sort()
    '''print("\nIn order of shooting percentage...")
    for s in sorted(pct_dict.values()):                #sorted by values
        print(pct_dict[s] + ': Shooting Percentage: ', pct_dict[s][0])
        print(pct_dict[s] + ':  3 Point Percentage: ', pct_dict[s][1])'''
    #unsure of listing by value. code crashes

def main():
    lines = readfile(filename)      #Get the lines from the file
    shots_dict = build_dict(lines)  #Get a dictionary of teams and shots
    #print(shots_dict)                  #(test code)
    pct_dict = calc_pct(shots_dict) #Get a dictionary of teams and pct
    #print(pct_dict)                    #(test code)
    show_pct(pct_dict)              #Print the teams and percentages

main()  #Start execution by calling main()
