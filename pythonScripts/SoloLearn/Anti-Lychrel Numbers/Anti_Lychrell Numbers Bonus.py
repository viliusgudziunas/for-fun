# Anti-Lychrel Numbers

# An anti-Lychrel number is a number that forms a palindrome through the iterative process of repeatedly reversing its
# digits and adding the resulting numbers. For example, 56 becomes palindromic after one iteration: 56+65=121.
# If the number doesn't become palindromic after 30 iterations, then it is not an anti-Lychrel number.

# Examples
# Input: 12
# Output: true (12 + 21 = 33, a palindrome)

# Input: 57
# Output: true (57+ 75 = 132, 132 + 231 = 363, a palindrome)

# Input: 10911
# Output: false (10911 takes 55 iterations to reach a palindrome)

# Write a program to check if the user input is an anti_Lychrel number or not

# Bonus:

# Print all the anti-Lychrel numbers in a given range.

import random
number = str(random.randint(10, 99))
number_set = []
def all_anti_lychrell():
    for i in range(1, int(number) + 1):
        count = 0
        current_number = str(i)
        reverse_number = current_number[::-1]
        sum = 0
        while count != 30:
            count = count + 1
            sum = str(int(current_number) + int(reverse_number))
            if sum == sum[::-1] and int(sum) <= int(number):
                number_set.append(int(current_number))
                break
            else:
                current_number = sum
                reverse_number = current_number[::-1]
        if sum != sum[::-1]:
            continue
    print("The set of all anti_Lychrell numbers in the given range:")
    return number_set
print("The range in which to look for anti-Lychrell numbers is from 1 to " + number)
print(all_anti_lychrell())