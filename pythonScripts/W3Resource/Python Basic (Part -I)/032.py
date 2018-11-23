# 32.
#
# Write a Python program to get the least common multiple (LCM) of two positive integers.

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = a * b

for i in range(a, c+1):
    if i % a == 0 and i % b == 0:
        print("The lowest common is "+str(i))
        exit(0)
