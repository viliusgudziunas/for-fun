# 60.
#
# Write a Python program to calculate the hypotenuse of a right angled triangle.

import math

a = int(input("Please enter the size of first edge: "))
b = int(input("Please enter the size of second edge: "))


def hypotenuse60(x, y):
    return "The length of the hypotenuse is "+str(round(math.sqrt((x**2)+(y**2)), 2))


print(hypotenuse60(a, b))
