import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:

player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll_1 = random.randint(1, 6)
#print("Player 1 rolled: ",player1_roll_1)

player2_roll_1 = random.randint(1, 6)
#print("Player 1 rolled: ",player2_roll_1)

# Round 2
player1_roll_2 = random.randint(1, 6)
#print("Player 2 rolled: ",player1_roll_2)

player2_roll_2 = random.randint(1, 6)
#print("Player 1 rolled: ",player2_roll_2)

# Round 3
player1_roll_3 = random.randint(1, 6)
#print("Player 2 rolled: ",player1_roll_3)

player2_roll_3 = random.randint(1, 6)
#print("Player 1 rolled: ",player2_roll_3)

# Round 4
player1_roll_4 = random.randint(1, 6)
#print("Player 2 rolled: ",player1_roll_4)

player2_roll_4 = random.randint(1, 6)
#print("Player 1 rolled: ",player2_roll_4)

# Round 5

player1_roll_5 = random.randint(1, 6)
#print("Player 2 rolled: ",player1_roll_5)

player2_roll_5 = random.randint(1, 6)
#print("Player 1 rolled: ",player2_roll_5)

# Round 6
player1_roll_6 = random.randint(1, 6)

player2_roll_6 = random.randint(1, 6)


## ROUND 1
# So far so good right? But how to check who got the highest roll?

if player1_roll_1 > player2_roll_1:
    player1_wins  += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_1," is greater than ", player2_roll_1)
    print("Player1 wins:", player1_wins)
elif player1_roll_1 == player2_roll_1:
    print("WOW!, This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_1," is greater than ", player1_roll_1)
    print("Player2 wins: ", player2_wins)


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

## ROUND 2
input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_2 > player2_roll_2:
    player1_wins  += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_2," is greater than ", player2_roll_1)
    print("Player1 wins:", player1_wins)
elif player1_roll_1 == player2_roll_2:
    print("WOW!, This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_2," is greater than ", player1_roll_1)
    print("Player2 wins: ", player2_wins)


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")


## ROUND 3
input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_3 > player2_roll_3:
    player1_wins  += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_3," is greater than ", player2_roll_3)
    print("Player1 wins:", player1_wins)
elif player1_roll_3 == player2_roll_3:
    print("WOW!, This round has a tie!")
else:
    player2_wins  += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_3," is greater than ", player1_roll_3)
    print("Player2 wins: ", player2_wins)


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

input("\nPress ENTER to continue...")
## ROUND 4
# So far so good right? But how to check who got the highest roll?

if player1_roll_4 > player2_roll_4:
    player1_wins  += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_4," is greater than ", player2_roll_4)
    print("Player1 wins:", player1_wins)
elif player1_roll_4 == player2_roll_4:
    print("WOW!, This round has a tie!")
else:
    player2_wins  += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_4," is greater than ", player1_roll_4)
    print("Player2 wins: ", player2_wins)


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

## ROUND 5

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_5 > player2_roll_5:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_5," is greater than ", player2_roll_5)
    print("Player1 wins:", player1_wins)
elif player1_roll_5 == player2_roll_5:
    print("WOW!, This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_5," is greater than ", player1_roll_5)
    print("Player2 wins: ", player2_wins)


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

## ROUND 6

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll_6 > player2_roll_6:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll_6," is greater than ", player2_roll_6)
    print("Player1 wins:", player1_wins)
elif player1_roll_6 == player2_roll_6:
    print("WOW!, This round has a tie!")
else:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll_6," is greater than ", player1_roll_6)
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
    
print("PLAYER1 ROLLS:")    
print(f"ROUND: |1 round roll: {player1_roll_1}|",
                f"|2 round roll: {player1_roll_2}|",
                f"|3 round roll: {player1_roll_3}|",
                f"|4 round roll: {player1_roll_4}|",
                f"|5 round roll: {player1_roll_5}|",
                f"|6 round roll: {player1_roll_6}|")


print("PLAYER2 ROLLS:")
print(f"ROUND: |1 round roll: {player2_roll_1}|",
                f"|2 round roll: {player2_roll_2}|",
                f"|3 round roll: {player2_roll_3}|",
                f"|4 round roll: {player2_roll_4}|",
                f"|5 round roll: {player2_roll_5}|",
                f"|6 round roll: {player2_roll_6}|")

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.