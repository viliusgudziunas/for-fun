# 26.
#
# Write a Python program to create a histogram from a given list of integers.

integers = [int(x) for x in input("Please enter a list of numbers: ").split()]

for n in integers:
    hist = ""
    while n > 0:
        hist += "*"
        n = n - 1
    print(hist)
