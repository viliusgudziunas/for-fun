# 40.
#
# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math

point1 = [int(x) for x in input("Please enter the first coordinate: ").split()]
point2 = [int(x) for x in input("Please enter the second coordinate: ").split()]


def distance40(x, y):
    x1 = x[0]
    y1 = x[1]
    x2 = y[0]
    y2 = y[1]
    return round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)),2)


print(distance40(point1, point2))
