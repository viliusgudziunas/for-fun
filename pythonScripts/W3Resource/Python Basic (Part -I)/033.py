# 33.
#
# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
c = int(input("Please enter the third integer: "))


def sum1(x, y, z):
    if x == y or x == z or y == z:
        return print(0)
    else:
        return print(x + y + z)


sum1(a, b, c)
