# 39.
#
# Write a Python program to compute the future value of a specified principal amount,
# rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

amt = 10000
roi = 3.5
years = 7


def future39(x, y, z):
    return round(x * ((1 + (y / 100)) ** z),2)


print(future39(amt, roi, years))
