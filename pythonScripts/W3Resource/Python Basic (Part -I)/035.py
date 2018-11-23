# 35.
#
# Write a Python program that will return true if the two given integer values are equal
# or their sum or difference is 5.

a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))


def boolean35(x, y):
    if x == y or x + y == 5 or x - y == 5:
        return print(True)
    else:
        return print(False)


boolean35(a, b)
