# Exercise 20

# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.

import random

def find(ordered_list, i_to_find):
    for i in ordered_list:
        if i == i_to_find:
            return True
    return False

ordered_list = []
i_to_find = 0

if __name__ == "__main__":
    ordered_list = sorted(random.sample(range(10), 5))
    i_to_find = random.randint(0, 9)
print(ordered_list)
print(i_to_find)
print(find(ordered_list, i_to_find))