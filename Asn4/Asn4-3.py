"""
3.	Complete Asn4-3.py to calculate the shooting percentages of the Dallas Mavericks
(DAL), the San Antonio Spurs (SAS) and the Houston Rockets (HOU) during the 2009 NBA
season. Shooting percentage is calculated by dividing the number of shots made by the
total number of shots attempted (shots made + shots missed). You will use three variables
to sum the total number of shots attempted for each team, and three more variables to
total the number of shots made for each team. Use the file 2009_shots.csv and model your
program after shots.py, the program we wrote in class to print shots made or attempted by
individual players. Your program, though, will use these three team names instead of player
names. For each team, print the number of shots attempted, the number made, and the shooting
percentage.

#Asn4-3.py: Calculate and print the shooting percentages of 3 NBA teams in 2009
#Input:  A file holding a record of all shots taken during the 2009 season
#Output: Number of shots attempted, number of shots made, and shooting percentages
#        for the Dallas Mavericks (DAL), San Antonio Spurs (SAS) and Houston
#        Rockets (HOU)
"""

filename = "2009_shots.csv"

def readfile(fname):
    '''Read the input file, return a list with all lines from the file'''
    f = open(fname, 'r')
    lines = f.readlines()
    f.close()
    return lines

def show_pct(lines):
    '''Print the teams in alphabetical order and their shooting percentages'''
    shotsDAL = 0  #shots attempted by DAL
    shotsSAS = 0  #shots attempted by SAS
    shotsHOU = 0  #shots attempted by HOU
    madeDAL = 0   #shots made by DAL
    madeSAS = 0   #shots made by SAS
    madeHOU = 0   #shots made by HOU
    
    #Add code here to go through the list of lines and add up shots attempted
        #and made by the three teams
    #Then calclulate and print shots attempted, shots made and shooting
        #percentages for the teams
    for i in range(1, len(lines)):
        data = lines[i].strip().split(',')
        if data[0] == 'DAL':
            shotsDAL += 1
            if data[2] == 'made':
              madeDAL += 1  
        if data[0] == 'SAS':
            shotsSAS += 1
            if data[2] == 'made':
              madeSAS += 1 
        if data [0] == 'HOU':
            shotsHOU += 1
            if data[2] == 'made':
              madeHOU += 1
        
    DALper = round((madeDAL/shotsDAL)*100, 2)
    SASper = round((madeSAS/shotsSAS)*100, 2)
    HOUper = round((madeHOU/shotsHOU)*100, 2)
              
    print('The Dallas Mavericks attempted', shotsDAL, 'shots. They made', madeDAL, 'of them.')
    print('     The Mavericks have a ', DALper, '% chance of making the shot.')
    print('The Houston Rockets attempted', shotsHOU, 'shots. They made', madeHOU, 'of them.')
    print('     The Rockets have a ', HOUper, '% chance of making the shot.')
    print('The San Antonio Spurs attempted', shotsSAS, 'shots. They made', madeDAL, 'of them.')
    print('     The Spurs have a ', SASper, '% chance of making the shot.')

def main():
    lines = readfile(filename)      #Get the lines from the file
    show_pct(lines)                 #Print the teams and percentages

         
main()  #Start execution by calling main()
