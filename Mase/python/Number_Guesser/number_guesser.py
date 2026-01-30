import random

print("Hey there, welcome to our game")
# user_input = input("Please type 'a' to play or 'q' to quit: ").lower()



while True:
   user_guesses = 0

   user_input = input("choose from the options below\n"
                      "a. start the game\n"
                      "q. to quit: ").lower()
   if user_input in ['q','quit']:
      print("Ok, Goodbye!")
      break
   elif user_input == 'a':
      pc_choice = random.randint(0, 10)
      user_guess = int(input("Please enter a number between 1 - 10 to make a guess: "))
     

      if user_guess < pc_choice:
         user_guesses += 1
         print("Too low!, guess again")
         print(f"The computer chose {pc_choice}")
         print(f"You chose {user_guess}")
         print(f"You guessed {user_guesses} times")
         continue
      elif user_guess > pc_choice:
         user_guesses += 1
         print("Too High!, guess again")
         print(f"The computer chose {pc_choice}")
         print(f"You chose {user_guess}")
         print(f"You guessed {user_guesses} times") 
         continue 
      elif user_guess == pc_choice:
         user_guesses += 1
         print("Spot On!")
         print(f"The computer chose {pc_choice}")
         print(f"You chose {user_guess}")
         print(f"You guessed {user_guesses} times")  
         break
   else:
       print("Please enter in valid input")

   if user_guesses > 3:
         print("Too many attemps")
         break
     



  
       

   

    
   