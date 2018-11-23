# 29.
#
# Write a Python program to print out a set containing all the colors from color_list_1
# which are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
color_list_3 = []

for i in color_list_1:
    if i not in color_list_2:
        color_list_3.append(i)

print(color_list_3)
