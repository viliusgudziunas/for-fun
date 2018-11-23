# Exercise 2

# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# 1. If the number is a multiple of 4, print out a different message.

number = int(input("Please enter a number "))
if number % 4 == 0:
    print("The number you have entered is divisible by 4")
elif number % 2 == 0:
    print("The number you have entered is even but not divisible by 4")
else:
    print("The number you have entered is odd")