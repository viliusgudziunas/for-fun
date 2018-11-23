# Exercise 12

# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a_list = [5, 10, 15, 20, 25]
def list_ends(a_list):
    return [a_list[0], a_list[-1]]
print([a_list[0], a_list[-1]])