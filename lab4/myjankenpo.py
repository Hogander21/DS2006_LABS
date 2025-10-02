'''
Python file to create my jankenpo game
'''
import random



print("**** Hello and welcome to Karls Jankenpo game ****")

# New rules for Jankenpo
'''
Choices:
    (1): Chicken
    (2): Cow 
    (3): Eagle
    
What beats what:
    Cow beats Chicken 
    
    Eagle beat Cow 
    
    Chicken beats Eagle

'''

def play_rps():
    '''
    Args: None
    
    Function for the game Rack Papers and Scissors.
    
    '''
    user_wins = 0
    computer_wins = 0
    elements = ['chicken', 'cow', 'eagle']

    print(f"These are the elemtens to choose from:")
    print(f"If element not entered, eagle will be standard")
    for i in elements:
        print(f"| {i} |")
        
        
    user_input = input("""Enter the element you want to use this round: \n""").lower()
    computer_choice = random.choice(elements)
    
    print(f"You choose: {user_input}")
    print(f"Computer choose: {computer_choice}")
    
    # Game Logic
    
    if user_input == computer_choice:
        print("Its a tie, no points awarded to anyone")
    
    if (
        (user_input == "chicken" and computer_choice == "eagle")
        or (user_input == "eagle" and computer_choice == "cow")
        or (user_input == "cow" and computer_choice == "chicken")
        ):
        user_wins += 1
        print("User wins! Point awarded to User!")
    
    else:
        computer_wins += 1
        print("Computer wins! Point awarded to Computer!")
    
    print("\n")
    print("*"*4, f"SCOREBOARD", "*" *4)
    print(f"User Score: {user_wins}")
    print(f"Computer Score: {computer_wins}")


while True:
    
    play_rps()
    one_more_round = input("One more round?: (y/n)")
    if one_more_round != "y":
        print("Another time!")
        break