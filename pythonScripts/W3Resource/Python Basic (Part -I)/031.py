# 31.
#
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
gcd = []

for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        gcd.append(i)

print(max(gcd))