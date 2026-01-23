# Import Random
import random 

# Set up Your Variables
options = ["rock", "paper", "scissors"]
user_win = 0
computer_win = 0
draw = 0

# Make your while loop, set to TRUE
# Take in input from user set it to variable
while True:
    user_choice = input("Type Rock/Paper/Scissors or 'q' for Quit: ").lower()
# Create your if/else statements for your player choices
    if user_choice == 'q' or user_choice == 'quit':
        print("Ok, Goodbye")
        break

    if user_choice not in options:
        continue
# Bring in random.randint()
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
# Make your if\else statements for win or lose
    if user_choice == 'rock' and computer_pick == 'scissors':
        print("You Win!")
        user_win += 1
        continue

    elif user_choice == 'rock' and computer_pick == 'rock':
        print("It's a Draw")
        draw += 1

    elif user_choice == 'paper' and computer_pick == 'rock':
        print("You Win!")
        user_win += 1
        continue

    elif user_choice == 'paper' and computer_pick == 'paper':
        print("It's a Draw")
        draw += 1

    elif user_choice == 'scissors' and computer_pick == 'paper':
        print("You Win!")
        user_win += 1
        continue

    elif user_choice == 'scissors' and computer_pick == 'scissors':
        print("It's a Draw")
        draw += 1
    else:
        print("You Lose")
        computer_win += 1
        continue
    
# Print out the result of game
print(f"You won: {user_win} times")
print(f"The computer won {computer_win} times")
print(f"You drew {draw} times")


