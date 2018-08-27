"""
Tara Walton
Assignment 3, Part 4
Description:
4. It is a little known fact that when Jack took his fateful fall,
with Jill tumbling closely after, they were irresponsibly racing down
that infamous hill. Now you will immortalize that event.
Write a program to simulate Dice Race! Dice Race! is a game with two players,
Jack and Jill, and a board with 20 squares.
The players advance by rolling a die and moving forward the number of squares
shown on the die; if a player lands on the same square as his or her opponent,
the opponent tumbles back one square. The first player to reach the top of the
hill (square 20) wins. Use random numbers to simulate throws of the die.
For each turn, print the roll and the positions of both players.
Use the variables jack and jill to keep player positions.
When a player wins, print the name of the winner.
Save your program as Asn3-4.py.

7.Another additional challenge for twice as much extra credit
(which is still none):
Extend Asn3-4 to ask the user how many games he or she wants to play,
then simulate that number of games.

Input : games
Output: dieJack, dieJill, spotJack, spotJill
"""
#necessary tools
import random
hillJack = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #visual game board
hillJill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #visual game board

#variable initialization
spotJack = 0
spotJill = 0

print("It's a race to the top of the hill!")
print("First player to 20 wins, but don't land on your opponent or you'll fall back down the hill!")
print()
games = int(input("How many games would you like to play? "))
for race in range(games):
    print("NEW GAME!")
    while spotJack < 20 and spotJill <20:
        #Jack plays
        dieJack = random.randint(1,6)
        spotJack += dieJack
        print("Jack rolls a ", dieJack, " for a position at ", spotJack)
        if spotJack >= 20:
            print("Jack Wins!")
            print()
            break
        #Jack movement
        if spotJack == spotJill:
            spotJill -= 1
            print("\tJill falls back a space, landing at ", spotJill)
                      
        #Jill plays
        dieJill = random.randint(1,6)
        spotJill += dieJill
        print("Jill rolls a ", dieJill, " for a position at ", spotJill)
        if spotJill >= 20:
            print("Jill Wins!")
            print()
            break
        #Jill movement
        if spotJill == spotJack:
            spotJack -= 1
            print("\tJack falls back a space ,landing at ", spotJack)
    spotJack = 0  #reset game pieces
    spotJill = 0
