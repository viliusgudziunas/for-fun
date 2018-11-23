# 4.
#
# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi


def area(r):
    if r < 0:
        print("The radius cannot be negative.")
        exit(1)
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
    exit(0)


radius = float(input("Please enter the radius of a circle: "))
area(radius)
