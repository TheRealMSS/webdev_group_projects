import random

def roll():
    pc_choice_one = random.randint(1, 6)
    pc_choice_two = random.randint(1, 6)
    result = f"You rolled {pc_choice_one} and {pc_choice_two}"
    return result

while True:
    print("Welcome to Dice Roller")
    user_choice = input("Would you like to roll a pair of dice?\n" \
    "'Y' for yes, 'N' for no: ").lower()

    if user_choice in ['yes', 'y']:
        print("Ok, Let's go")
        print(roll())
    elif user_choice in ['no', 'n']:
        print("Ok, see you later")
        exit()
    else:
        print("Invaild Option, Please try again")
        continue
