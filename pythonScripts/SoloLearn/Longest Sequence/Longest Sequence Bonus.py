# Longest Sequence

# Given a series of numbers, find the longest sequence in the series.
# A sequence could be one of the following:

# An ascending sequence
# Example:
# Input: 836926
# Output: 369

# A descending sequence
# Example:
# Input: 2995316
# Output: 9531

# An equal sequence
# Example:
# Input: 255566
# Output: 555

# Write a program that reads a series of numbers from the input and finds the longest ascending, descending or equal
# sequence in the series.

# Bonus:

# Write a program to find all of the sequences above.

import random
random_integer = random.randint(1000000000, 9999999999)
random_number = list(str(random_integer))
def longest_sequence(random_number):
    current_sequence = random_number[0]
    equal_list = []
    ascending_list = []
    descending_list = []
    for i in range(1, len(random_number)):
        if random_number[i - 1] == random_number[i]:
            current_sequence += random_number[i]
        else:
            equal_list.append(int(current_sequence))
            current_sequence = random_number[i]
    equal_list.append(int(current_sequence))
    for i in range(1, len(random_number)):
        if random_number[i-1] < random_number[i]:
            current_sequence += random_number[i]
        else:
            ascending_list.append(int(current_sequence))
            current_sequence = random_number[i]
    ascending_list.append(int(current_sequence))
    for i in range(1, len(random_number)):
        if random_number[i-1] > random_number[i]:
            current_sequence += random_number[i]
        else:
            descending_list.append(int(current_sequence))
            current_sequence = random_number[i]
    descending_list.append(int(current_sequence))
    last = [max(equal_list), max(ascending_list), max(descending_list)]
    print("The sequences are:")
    print("Longest equal sequence is " + str(max(equal_list)))
    print("Longest ascending sequence is " + str(max(ascending_list)))
    print("Longest descending sequence is " + str(max(descending_list)))
    return ("Thus the longest sequence is " + str(max(last)))
print("The random integer is " + str(random_integer))
print(longest_sequence(random_number))