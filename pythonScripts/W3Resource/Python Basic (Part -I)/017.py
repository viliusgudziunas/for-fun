# 17.
#
# Write a Python program to test whether a number is within 100 of 1000 or 2000.

from random import randint

num = randint(1, 2000)

print(num)
if num < 100:
    print("The number is within 100")
elif num < 1000:
    print("The number is within 1000")
else:
    print("The number is within 2000")