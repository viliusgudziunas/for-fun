# 18.
#
# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.

a = int(input("Please enter a number: "))
b = int(input("Please enter a second number: "))
c = int(input("Please enter a final number: "))

if a == b == c:
    sum = (a + b + c)*3
else:
    sum = a + b + c

print(sum)
