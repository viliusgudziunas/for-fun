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
    sum = 0
    if prime(num) == True:
        num_str = str(num)
        for i in num_str:
            digit = int(i)
            sum = sum + digit
        if prime(sum) == True:
            return str(num) + " is a howling prime, because " + str(sum) + " is also a prime."
        else:
            return str(num) + " is not a howling prime because " + str(sum) + " is not a prime."
    else:
        return "The number is not a prime"

print("The number is " + str(num))
print(howling())