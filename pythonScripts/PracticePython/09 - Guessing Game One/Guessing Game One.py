# Exercise 9

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

import random
number = random.randint(1, 9)
print("Guess the number ")
guess = int(input())
if number == guess:
    print("Well done, you guessed right!")
elif number < guess:
    print("Sorry, you guessed too high.")
else:
    print("Sorry, you guessed too low.")