# Howling Primes

# A howling prime is a prime number if the sum of its digits is also a prime number.

# For Example:
# Input: 113
# Output: true (113 is a prime number, 1+1+3=5 is also a prime number)

# Input: 89
# Output: true (89 is a prime number, 8+9=17 is also a prime number)

# Input: 19
# Output: false (19 is a prime number, but 1+9=10 is not a prime number)

# Write a program to check if the user input is a howling prime or not.

# Bonus:

# Print all the howling prime numbers in a given range

import random
num = random.randint(2, 100)

def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True

def howling():
    primes = []
    howling_primes = []
    for i in range(2, num):
        if prime(i) == True:
            primes.append(i)
    for i in primes:
        sum = 0
        num_str = str(i)
        for element in num_str:
            digit = int(element)
            sum = sum + digit
        if prime(sum) == True:
            howling_primes.append(i)
    print("The list of howling primes in the given range is: ")
    return howling_primes

print("The range is 1 to " + str(num))
print(howling())