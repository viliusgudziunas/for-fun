# Exercise 9

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
number = random.randint(1, 9)
count = 0
guess = 0
while guess != number and guess != "exit":
    guess = (input("Guess a number between 1 and 9 "))
    if guess == "exit":
        break
    guess = int(guess)
    count += 1
    if guess < number:
        print("You guessed too low")
    elif guess > number:
        print("You guessed too high")
    else:
        print("Well done, you got it in",count,"tries!")