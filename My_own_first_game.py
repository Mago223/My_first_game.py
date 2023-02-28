import random 

program_wins = 0
user_wins = 0 
options = ["rock", "paper", "scissors"]

print("Welcome to my rock, paper, scissors game!")

while True:
    if user_wins == 3:
        break
    elif program_wins == 3:
        break

    user_pick = input("Type either rock/paper/scissors or Q to quit: ").lower()

    if user_pick == "q":
        break 

    if user_pick not in options:
        print("Please type a valid response!")
        continue

    random_pick = random.randint(0, 2)
    program_pick = options[random_pick]

    print(f"The computer picked {program_pick}.")

    if user_pick == program_pick:
        print("The answers were the same! Try again!")
    elif user_pick == "rock" and program_pick == "scissors":
        print("You won!")
        user_wins += 1 
    elif user_pick == "paper" and program_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_pick == "scissors" and program_pick == "paper":
        print("You won!")
        user_wins += 1 
    else:
        print("You lost!")
        program_wins += 1
        

if user_wins == program_wins:
    print("Thank you for playing")
elif user_wins > program_wins:
    print(f"Congrats! You won {user_wins} times, while the computer won {program_wins} times!")
else:
    print(f"Sorry you lost! The computer won {program_wins} times, while you won {user_wins} times!")
