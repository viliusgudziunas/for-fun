# 10.
#
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

n = int(input("Please enter a number: "))
nn = int(str(n) + str(n))
nnn = int(str(nn) + str(n))
print(n + nn + nnn)