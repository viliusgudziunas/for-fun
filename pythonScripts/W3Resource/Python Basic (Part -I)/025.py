# 25.
#
# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

a = 3
b = -1
set1 = [1, 5, 8, 3]

if a in set1:
    print(str(a)+" is in the set "+str(set1))
else:
    print(str(a) + " is not in the set " + str(set1))

if b in set1:
    print(str(b)+" is in the set "+str(set1))
else:
    print(str(b) + " is not in the set " + str(set1))
