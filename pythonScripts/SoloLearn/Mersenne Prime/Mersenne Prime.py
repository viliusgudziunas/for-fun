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

import random
num = random.randint(1, 99)
def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True
def mersenne():
    x = num
    set = []
    if prime(x) == True:
        for i in range(2, 7):
            if x == 2 ** i - 1:
                set.append(i)
        if set == []:
            return "The number is not a Mersenne Prime"
        else:
            print("The number is a Mersenee Prime")
            return str(num) + " = 2 ^ " + str(set[0]) + " - 1"
    else:
        return "The number is not a prime"
print(num)
print(mersenne())
