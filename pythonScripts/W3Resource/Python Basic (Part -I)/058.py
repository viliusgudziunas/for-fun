# 58.
#
# Write a python program to sum of the first n positive integers.

num = int(input("Please enter a number up to which we are summing: "))


def sum58(x):
    result = 0
    for i in range(x+1):
        result += i
    return result


print(sum58(num))
