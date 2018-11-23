# Exercise 14

# Write a program (function!)
# that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# 1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.

def a_list(x):
    return list(set(x))
a = [1, 1, 2, 1, 4, 5, 1, 7, 7, 8, 9, 9, 12, 13, 13, 12]
print(a_list(a))