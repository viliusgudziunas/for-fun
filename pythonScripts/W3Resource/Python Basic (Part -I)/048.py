# 48.
#
# Write a Python program to parse a string to Float or Integer.

string1 = "20135.33"


def parsing48(x):
    print("String = "+x)
    float1 = float(x)
    int1 = int(float(x))
    return "Float = "+str(float1)+"\nInteger = "+str(int1)


print(parsing48(string1))
