# Fisher Number

# A Fisher number is an integer whose multipliers are equal to the number;s cube.
# For example, 12 is a Fisher number,because 12^3 = 2 x 3 x 6 x 12.

# For example:
# Input: 12
# Output: true (12^3 = 3 x 3 x 4 x 6 x 12)

# Input: 8
# Output: false (8^3 != 2 x 4 x 8)

# Write a program to check if the user input is a Fisher number or not.

def fisher_number():
    number = int(input("Please enter a number "))
    number_cube = number ** 3
    number_multipliers = []
    number_multipliers_product = 1
    for i in range(2, number + 1):
        if number % i == 0:
            number_multipliers.append(i)
            number_multipliers_product *= i
    if number_cube == number_multipliers_product:
        print("The multipliers = " + str(number_multipliers))
        print("The number's cube = " + str(number_cube))
        print("The product of all number's multipliers = " + str(number_multipliers_product))
        return "The number you have entered is a fisher number!"
    else:
        print("The multipliers = " + str(number_multipliers))
        print("The number's cube = " + str(number_cube))
        print("The product of all number's multipliers = " + str(number_multipliers_product))
        return "The number you have entered is not a fish number!"
print(fisher_number())