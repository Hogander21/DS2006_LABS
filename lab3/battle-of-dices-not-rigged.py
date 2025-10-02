import random

from dice_lab3 import diceD4, diceD6, diceD8, diceD12, diceD20, dice100

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:

player1_wins = 0
player2_wins = 0

player_1_rolls = []
player_2_rolls = []



while player1_wins < 3 and player2_wins < 3:

# Round 1
    input("\nPress ENTER to roll the dice...")

    player1_roll = diceD6()
    print("Player 1 rolled: ",player1_roll)
    player_1_rolls.append(player1_roll)

    player2_roll = diceD6()
    print("Player 2 rolled: ",player2_roll)
    player_2_rolls.append(player2_roll)



    input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins = player1_wins + 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll," is greater than ", player2_roll)
        print("Player1 wins:", player1_wins)
    elif player1_roll == player2_roll:
        print("WOW!, This round has a tie!")
    else:
        player2_wins = player2_wins + 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll," is greater than ", player1_roll)
        print("Player2 wins: ", player2_wins)


    # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.

    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

print("PLAYER 1 ROLLS:")        
n = 1
for i in player_1_rolls:
    print(f"ROUND: |{n} round roll: {i}|")
    n += 1

print("PLAYER 2 ROLLS:")      
l = 1
for i in player_2_rolls:
    print(f"ROUND: |{l} round roll: {i}|")
    l += 1

n = 1
l = 1
filename = input("Enter file name to save summary: ")
with open(filename + ".txt", 'w') as f:
    
    f.write("Player1 rolls:\n")
    for i in player_1_rolls:
        f.write(f"ROUND: |{n} round roll: {i}|\n")
        n += 1
    
    f.write("Player2 rolls:\n")
    for i in player_2_rolls:
        f.write(f"ROUND: |{l} round roll: {i}|\n")
        l += 1
        
    

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.