import random

# Get the user's input
n = input("Enter rock, paper, or scissors: ").lower()

# Define the options
rock = "rock"
paper = "paper"
scissors = "scissors"

# List of valid options
game = [rock, paper, scissors]

# Check if the user's input is valid
if n not in game:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    # Randomly choose for the computer
    a = random.choice(game)
    
    print(f"Computer chooses {a} and you choose {n}")
    
    # Determine the winner
    if n == rock and a == paper:
        print("You lose!")
    elif n == rock and a == scissors:
        print("You win!")
    elif n == paper and a == scissors:
        print("You lose!")
    elif n == paper and a == rock:
        print("You win!")
    elif n == scissors and a == paper:
        print("You win!")
    elif n == scissors and a == rock:
        print("You lose!")
    elif a == n:
        print("It's a tie!")
