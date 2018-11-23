# 59.
#
# Write a Python program to convert height (in feet and inches) to centimeters.

print("Please input your height: ")
height_ft = int(input("Feet: "))
height_inch = int(input("Inches: "))

height_inch += height_ft * 12
height_cm = round(height_inch * 2.54, 1)

print("Your height is: "+str(height_cm)+" cm.")
