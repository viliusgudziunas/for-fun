# 21.
#
# Write a Python program to find whether a given number (accept from the user) is even or odd,
# print out an appropriate message to the user.

num = int(input("Please enter a number: "))

if num % 2 == 0:
    print("The number you entered is even.")
else:
    print("The number you entered is odd.")