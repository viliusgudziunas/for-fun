# 22.
#
# Write a Python program to count the number 4 in a given list.

list = [int(a) for a in input("Please enter a list of numbers: ").split()]

count = 0

for i in list:
    if i == 4:
        count = count + 1

print(count)
