# 23.
#
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

str = str(input("Please enter a string: "))
num = int(input("Please enter a non-negative integer: "))

if len(str) < 2:
    for i in range(num):
        print(str, end="")
else:
    for i in range(num):
        char = str[:2]
        print(char, end="")
