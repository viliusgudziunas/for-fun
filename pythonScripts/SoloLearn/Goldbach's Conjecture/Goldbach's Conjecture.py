# Goldbach's Conjecture

# Goldbach's conjecture is a rule in math that states the following:
# every even number greater than 3 can be expressed as the sum of two prime numbers.

# Write a program that finds every possible pair of prime numbers,
# whose sum equals the given number or a set of numbers withing a range.

# For example:
# Input: 16
# Output:
# 3 + 13
# 5 + 11

# Input: 32
# Output:
# 3 + 29
# 13 + 19

# Input: 4, 8
# Output:
# 4: 2 + 2
# 6: 3 + 3
# 8: 3 + 5

import random
num = random.randint(2, 50) * 2
def prime(x):
    dummy = []
    for i in range(2, x - 1):
        if x % i == 0:
            dummy.append(i)
    if dummy == []:
        return True

def goldbach():
    primes = []
    set = []
    for i in range(2, num - 1):
        x = i
        if prime(x) == True:
            primes.append(x)
    for i in primes:
        take_away = num - i
        if take_away in primes:
            set.append([i, take_away])
    if len(set) % 2 == 0:
        del set[len(set) // 2:]
    else:
        del set[len(set) // 2 + 1:]
    return set
print(num)
print(goldbach())