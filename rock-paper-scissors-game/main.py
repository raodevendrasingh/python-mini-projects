import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    rand_num = random.randint(0, 2)
    # rock: 0   paper: 1    scissors: 2

    comp_pick = options[rand_num]
    print("Computer picked: ",comp_pick + ".")

    if user_input == "rock" and comp_pick == "scissors":
        user_wins += 1
        print("You Won!")
    elif user_input == "scissors" and comp_pick == "paper":
        user_wins += 1
        print("You Won!")
    elif user_input == "paper" and comp_pick == "rock":
        user_wins += 1
        print("You Won!")
    elif user_input == comp_pick:
        print("Same choice. Pick again!")
    else:
        print("You Lost!")
        comp_wins += 1

print("\nYou won", user_wins, "times")
print("Computer won", comp_wins, "times")
