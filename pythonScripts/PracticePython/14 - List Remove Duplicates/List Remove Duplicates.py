# Exercise 14

# Write a program (function!)
# that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def a_list(x):
    new_list = []
    for element in x:
        if element not in new_list:
            new_list.append(element)
    return new_list
a = [1, 1, 2, 1, 4, 5, 1, 7, 7, 8, 9, 9, 12, 13, 13, 12]
print(a_list(a))