# Exercise 1

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Please enter your name ")
age = int(input("Please enter how old you will be at the end of this year "))
time = 100 - age
turn = str(2018 + time)
print(name + ", you will turn 100 years old in the year " + turn)