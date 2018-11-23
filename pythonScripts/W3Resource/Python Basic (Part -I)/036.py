# 36.
#
# Write a Python program to add two objects if both objects are an integer type.


def sum36(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Inputs must be integers")
    else:
        return x + y


print(sum36(10, 3))
print(sum36("Hey", 10))
