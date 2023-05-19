import random

name = input("Please enter yor name: ")
print(f"Welcome {name}, to the number guessing game!")
print("\nRULES: You have to guess the number, if your guess is higher or lower, a hint will be given!\n")
user_range = int(input("Please enter the upper bound of the range: "))
guesses = 0
rand_num = random.randint(0, user_range)

while True:
    guesses += 1
    guess = int(input("Guess the number: "))
    if guess > rand_num:
        print("Go lower")
        continue
    if guess < rand_num:
        print("Go higher")
        continue
    if guess == rand_num:
        print(f"You got it! The number is {rand_num}")
        print(f"It took you {guesses} guesses")
        break
