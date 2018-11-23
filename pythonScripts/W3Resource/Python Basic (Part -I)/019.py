# 19.
#
# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

string = input("Please enter a string: ")

if string.find("I") == 0 and string.find("s") == 1:
    print(string)
else:
    print("Is "+string)