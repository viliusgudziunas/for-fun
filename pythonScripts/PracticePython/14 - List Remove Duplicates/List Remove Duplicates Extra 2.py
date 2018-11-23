# Exercise 14

# Write a program (function!)
# that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# 1. Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# 2. Go back and do Exercise 5 using sets, and write the solution for that in a different function.

def a_list(x, y):
    new_list = set()
    for element in x:
        if element in y:
            new_list.add(element)
    return new_list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(a_list(a, b))