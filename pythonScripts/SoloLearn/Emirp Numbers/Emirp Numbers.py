# Emirp Numbers

# An emirp is a prime number that results in a different prime when its decimal digits are reversed.
# For example, 13 is an emirp number because both 13 and 31 are prime numbers.

# For example:
# Input: 17
# Output: true (17 and 71 are prime numbers)

# Input: 113
# Output: true (113 and 311 are prime numbers)

# Input: 113
# Output: false (23 is a prime number, but 32 is not)

# Write a program to check if the user input is an emirp number or not.

import random
num = random.randint(1, 100)

def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True

def emirp():
    rev = 0
    if prime(num) == True:
        rev = int(str(num)[::-1])
        if prime(rev) == True:
            return "This is an emirp number because " + str(num) + " is a prime and " + str(rev) + " is also a prime."
        else:
            return "This isn't an emirp number bacause " + str(num) + " is a prime but " + str(rev) + " is not a prime."
    else:
        return "This is not an emirp number bacause " + str(num) + " is not a prime."


print("The number is " + str(num))
print(emirp())