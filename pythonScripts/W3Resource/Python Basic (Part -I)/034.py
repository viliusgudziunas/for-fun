# 34.
#
# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))


def sum31(x, y):
    if 15 < x + y < 20:
        return print(20)
    else:
        return print(x + y)


sum31(a, b)
