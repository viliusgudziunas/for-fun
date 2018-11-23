# Exercise 20

# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.

# Extras:

# Use binary search.

import random
ordered_list = []
i_to_find = 0

def binary(ordered_list, i_to_find):
    start_index = 0
    end_index = len(ordered_list) - 1
    while True:
        middle_index = int((end_index + start_index) / 2)
        if middle_index == start_index or middle_index == end_index:
            if ordered_list[middle_index] == i_to_find or ordered_list[end_index] == i_to_find:
                return True
            else:
                return False
        middle_element = ordered_list[middle_index]
        if middle_element == i_to_find:
            return True
        elif middle_element > i_to_find:
            end_index = middle_index
        else:
            start_index = middle_index

if __name__ == "__main__":
    ordered_list = sorted(random.sample(range(10), 5))
    i_to_find = random.randint(0, 9)

print(ordered_list)
print(i_to_find)
print(binary(ordered_list, i_to_find))