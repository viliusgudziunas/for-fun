# Longest Sequence

# Given a series of numbers, find the longest sequence in the series.
# A sequence could be one of the following:

# A descending sequence
# Example:
# Input: 2995316
# Output: 9531

# Write a program that reads a series of numbers from the input and finds the longest descending sequence in the series.

import random
random_integer = random.randint(1000000000, 9999999999)
random_number = list(str(random_integer))
def descending_sequence(random_number):
    current_sequence = random_number[0]
    output_list = []
    for i in range(1, len(random_number)):
        if random_number[i-1] > random_number[i]:
            current_sequence += random_number[i]
        else:
            output_list.append(int(current_sequence))
            current_sequence = random_number[i]
    output_list.append(int(current_sequence))
    return max(output_list)
print(random_integer)
print(descending_sequence(random_number))