# Exercise 4

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Please enter a number ")
number = int(input())
a = range(2, number + 1)
b = []
for element in a:
    if number % element == 0:
        b.append(element)
print(b)