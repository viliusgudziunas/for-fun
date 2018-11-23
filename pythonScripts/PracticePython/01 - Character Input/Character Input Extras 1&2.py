# Exercise 1

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# 1. Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Please enter your name ")
age = int(input("Please enter how old you will be at the end of this year "))
time = 100 - age
turn = str(2018 + time)
number = int(input("Please enter a number "))
for element in range(1, number):
    print(name + ", you will turn 100 years old in the year " + turn)