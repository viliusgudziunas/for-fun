# Marsenne Prime

# A Mersenne prime is a prime number that is one less than a power of two.
# It is a prime number of the form 2^n - 1 for some integer n.

# For example:
# Input: 3
# Output: true (3 is a prime number and 3=2^2-1)

# Input: 31
# Output: true (31 is a prime number and 31=2^5-1)

# Input: 17
# Output: false (17 is a prime number but it is not of the form 2^n-1)

# Write a program to check if the user input is a Mersenne prime or not.

# Bonus:

# Print all the Mersenne primes in a given range.

import random
num = random.randint(3, 999)
def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True

def mersenne():
    primes = []
    set1 = []
    for i in range(2, num - 1):
        x = i
        if prime(x) == True:
            primes.append(x)
    for i in primes:
        num_prime = i
        for element in range(2, 100):
            if num_prime == 2 ** element -1:
                set1.append(i)
    return "The Mersenne Primes in the given range are: " + str(set1)
print("The range for Mersenne Primes is 0 to " + str(num))
print(mersenne())
