from dice_lab6 import diceD6

player_names = []

# Array storing the number of wins for each player:
player_wins = []

# Initialize player rolls as empty lists for each player
player_rolls_history = []

# Initialize Gameover
gameover = False

# Initialize rounds
rounds = 0

# Number of wins needed to win the game:
winning_score = 3

#Obtain the number of players and their names
number_of_players = int(input("How many players?: "))

for i in range(number_of_players):
    name = input(f"What is the name of player {i+1}: ")
    player_names.append(name)

for i in range(number_of_players):
        player_wins.append(0)

for i in range(number_of_players):
        player_rolls_history.append([])

while gameover is False:
    print(f"Round {rounds+1}")
    
    # Dice roll for each player in the current round
    current_rolls = []
    
    # We need to roll the dice for each player
    for i in range(number_of_players):
        roll = diceD6()
        current_rolls.append(roll)
        player_rolls_history[i].append(roll)
        print(f"Player {player_names[i]} rolled: {roll}")
        
    input("\nPress ENTER to continue")
    
    # Obtain the highest roll this round
    max_roll = max(current_rolls)
    
    # Winners will store information about who won this round
    winners = []
    
    # Search for all players who got the highest roll:
    for j in range(len(current_rolls)):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1
    print(f"Winners of this round are: {winners}")
    
    
    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n{player_names[z]} is the newest Battle of Dices Champion!")
            gameover = True
            
    if gameover is False:
        print("This heated Battle of Dices is till going on! Who will win in the end?")

    rounds += 1


filename = input("Enter the filename to save the results: ")
with open(filename, 'w') as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""
        
        for i in range(number_of_players):
            rolls_str += (f"{player_names[i]} rolled {player_rolls_history[i][round_number]}")
            if i < number_of_players - 1:
                rolls_str += ", "
        print(f"Saving {rolls_str}")
        
        file.write(rolls_str + "\n")    
