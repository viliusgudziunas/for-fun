# Birthday Json

# This exercise is Part 2 of 4 of the birthday data exercise series.
# The other exercises are: Part 1, Part 3, and Part 4.

# In the previous exercise we created a dictionary of famous scientists’ birthdays.
# In this exercise, modify your program from Part 1
# to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.

# Bonus:
# Ask the user for another scientist’s name and birthday to add to the dictionary,
# and update the JSON file you have on disk with the scientist’s name.
# If you run the program multiple times and keep adding new names,
# your JSON file should keep getting bigger and bigger.

import json
import time


def p34():
    with open("birthdays.json") as file:
        birthdays = json.load(file)

    print("\nWelcome to the birthday dictionary. We know the birthdays of:")

    for person in birthdays.keys():
        print(f" - {person}")

    print("\nWho's birthday would you like to lookup?")
    name = input(" > ")

    if name not in birthdays:
        print("\nUnfortunately, the name you entered was not in our list.")
        print("Please try again!")
        time.sleep(2)
        p34()

    print(f"\n{name}'s birthday is {birthdays[name]}'")
    time.sleep(2)

    print("\nWould you like to add a new person to our list? (Y/n)")
    decision = input(" > ")

    if decision != "Y":
        return "\nThanks for using this program!"

    print("\nPlease enter the name of a person you would like to add")
    name = input(" > ")
    time.sleep(1)
    print("\nPlease enter the date of birth of the person (DD/MM/YYYY)")
    dob = input(" > ")
    time.sleep(1)

    with open("birthdays.json", "w") as file:
        birthdays[name] = dob
        json.dump(birthdays, file)


p34()
