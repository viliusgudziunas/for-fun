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

# Bonus:
# Print all the emirp numbers in a given range.

import random
num = random.randint(10, 1000)

def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True

def emirp_numbers():
    rev = 0
    primes = []
    emirp_set = []
    emirp_set1 = []
    for i in range(10, num + 1):
        if prime(i) == True:
            primes.append(i)
    for i in primes:
        rev = int(str(i)[::-1])
        if prime(rev) == True:
            emirp_set.append(rev)
            rev1 = int(str(rev)[::-1])
            emirp_set1.append(rev1)
    print("The set of emirp numbers in the range is: ")
    return emirp_set1

print("The range is 10 to " + str(num))
print(emirp_numbers())