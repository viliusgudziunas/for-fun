# 6.
#
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list
# and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

values = input("Please enter a set of numbers separated by commas: ")
list = values.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple)
