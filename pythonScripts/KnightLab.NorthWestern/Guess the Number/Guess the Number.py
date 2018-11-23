# 2. Guess the Number

# The Goal:
# Similar to the first project, this project also uses the random module in Python.
# The program will first randomly generate a number unknown to the user. The user needs to guess what that number is.
# (In other words, the user needs to be able to input information.)
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear.
# You’ll need functions to check if the user input is an actual number,
# to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.

# Concepts to keep in mind:

# Random function
# Variables
# Integers
# Input/Output
# Print
# While loops
# If/Else statements


# Jumping off the first project,
# this project continues to build up the base knowledge and introduces user-inputted data at its very simplest.
# With user input, we start to get into a little bit of variability.

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