import random

from dice import diceD4, diceD6, diceD8, diceD12, diceD20, dice100

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:

player1_wins = 0
player2_wins = 0

player1_roll_list = []
player2_roll_list = []

while player1_wins < 3 and player2_wins < 3:

# Round 1
    input("\nPress ENTER to roll the dice...")

    player1_roll = diceD8() + diceD12()
    print("Player 1 rolled: ",player1_roll)
    player1_roll_list.append(player1_roll)

    player2_roll = diceD6() + diceD20()
    print("Player 2 rolled: ",player2_roll)
    player2_roll_list.append(player2_roll)

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
        print(f"The summery of the game is Player1 Roll List: {player1_roll_list} and " +
                        f"Player2 Roll list: {player2_roll_list}:")
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        print(f"The summery of the game is Player1 Roll List: {player1_roll_list} and " +
                        f"Player2 Roll list: {player2_roll_list}:")

    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")

# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.