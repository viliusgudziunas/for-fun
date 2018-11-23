# Fisher Number

# A Fisher number is an integer whose multipliers are equal to the number;s cube.
# For example, 12 is a Fisher number,because 12^3 = 2 x 3 x 6 x 12.

# For example:
# Input: 12
# Output: true (12^3 = 3 x 3 x 4 x 6 x 12)

# Input: 8
# Output: false (8^3 != 2 x 4 x 8)

# Write a program to check if the user input is a Fisher number or not.

# Bonus:

# Print all the Fisher numbers in a given range.

def fisher_number(number):
    number_cube = number ** 3
    number_multipliers_product = 1
    for i in range(2, number + 1):
        if number % i == 0:
            number_multipliers_product *= i
    if number_cube == number_multipliers_product:
        return True
    else:
        return False

def fisher_numbers():
    fisher_range = int(input("Please enter a number "))
    fisher_list = []
    for number in range(2, fisher_range + 1):
        if fisher_number(number) == True:
            fisher_list.append(number)
        else:
            continue
    print("Here is the list of all fisher numbers in the given range:")
    return fisher_list
print(fisher_numbers())