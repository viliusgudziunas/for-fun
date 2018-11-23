# 61.
#
# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

dist_feet = float(input("Please enter a distance in feet: "))


def convert61(x):
    dist_inch = round(x * 12, 2)
    dist_yard = round(dist_inch / 36, 2)
    dist_mile = round(dist_yard / 1760, 2)
    print("The given distance in inches is "+str(dist_inch))
    print("The given distance in yards is "+str(dist_yard))
    print("The given distance in miles is "+str(dist_mile))


convert61(dist_feet)
