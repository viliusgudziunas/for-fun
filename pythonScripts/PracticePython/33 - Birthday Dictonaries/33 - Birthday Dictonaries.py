# Exercise 33
#
# For this exercise, we will keep track of when our friend’s birthdays are,
# and be able to find that information based on their name.
# Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
# The interaction should look something like this:
#
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.
# Happy coding!

import time


def bdays():
    dates = {
        "Albert Einstein": "14/03/1879",
        "Benjamin Franklin": "17/01/1706",
        "Ada Lovelace": "10/12/1815"
    }
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    time.sleep(1)
    for i in dates:
        print(i)
    print("Who's birthday do you want to look up?")
    inp = input()
    if inp not in dates:
        print("The name is not in the list")
        return
    else:
        print(inp + "'s birthday is " + dates[inp] + ".")
        return


bdays()
