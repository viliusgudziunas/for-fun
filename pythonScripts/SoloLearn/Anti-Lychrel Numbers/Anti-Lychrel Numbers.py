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

import random
number = str(random.randint(1, 9999999999))
def anti_lychrel():
    count = 0
    current_number = number
    reverse_number = number[::-1]
    sum = 0
    while count != 30:
        count = count + 1
        sum = str(int(current_number) + int(reverse_number))
        if sum == sum[::-1]:
            break
        else:
            current_number = sum
            reverse_number = current_number[::-1]
    if sum != sum[::-1]:
        return "The number generated did not become palindrome after 30 iterations so it is not an Anti-Lychrel number"
    else:
        print("The number of iterations for the above number to become an Anti-Lychrel was " + str(count))
        return "The palindromic number reached is " + sum
print("The random number generated is " + number)
print(anti_lychrel())