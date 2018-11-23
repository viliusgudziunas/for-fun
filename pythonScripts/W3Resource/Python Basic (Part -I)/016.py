# 16.
#
# Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

num = int(input("Please enter a number: "))
if num > 17:
    print("The double absolute difference between the number and 17 is " + str(2*abs(17-num)))
else:
    print("The difference between the number and 17 is " + str(17-num))
