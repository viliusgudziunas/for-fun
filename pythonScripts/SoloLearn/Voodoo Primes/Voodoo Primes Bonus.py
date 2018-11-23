# Voodoo Primes

# A Voodoo prime is a prime number whose reciprocal (in decimal) has the same number in its digits.
# For example, 7 is a voodoo prime because its reciprocal 1/7=0/14285714285 contains 7.

# Examples:
# Input: 3
# Output: true (1/3=0.33333333333 contains 3)

# Input: 11
# Output: false (1/11=0.0909090909 doesn't contain 11)

# Write a program to check if the user input is a Voodoo prime or not.

# Bonus:

# Print all the Voodoo primes in a given range.

import random
num = random.randint(2, 10000)

def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True
def voodoo():
    primes = []
    voodoo_primes = []
    for i in range(2, num):
        if prime(i) == True:
            primes.append(i)
    for i in primes:
        fraction = str(1 / i)
        if str(i) in fraction:
            voodoo_primes.append(i)
    return "The list of Voodoo primes in the given range is: " + str(voodoo_primes)

print("The range is 2 to " + str(num))
print(voodoo())