# 20.
#
# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

str = str(input("Please enter a string: "))
n = int(input("Please enter a non-negative integer: "))

for i in range(n):
    print(str, end="")