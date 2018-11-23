# Voodoo Primes

# A Voodoo prime is a prime number whose reciprocal (in decimal) has the same number in its digits.
# For example, 7 is a voodoo prime because its reciprocal 1/7=0/14285714285 contains 7.

# Examples:
# Input: 3
# Output: true (1/3=0.33333333333 contains 3)

# Input: 11
# Output: false (1/11=0.0909090909 doesn't contain 11)

# Write a program to check if the user input is a Voodoo prime or not.

import random
num = random.randint(2, 100)

def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True

def voodoo():
    if prime(num) == True:
        fraction = str(1/num)
        if str(num) in fraction:
            return "The number is a Voodoo prime, as " + fraction + " does contain " + str(num)
        else:
            return "The number is not a Voodoo prime, because " + fraction + " does not contain " + str(num)
    else:
        return "The number is not a prime."

print("The number is " + str(num))
print(voodoo())