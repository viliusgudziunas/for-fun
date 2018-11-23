# 38.
#
# Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49


def math38(x, y):
    return "("+str(x)+" + "+str(y)+")"+" ^ 2) = "+str((x + y) ** 2)


print(math38(3, 4))
