# 24.
#
# Write a Python program to test whether a passed letter is a vowel or not.

a = str(input("Please enter a letter: "))
a.lower()

if a in ["a", "e", "i", "o", "u"]:
    print("The letter you entered is a vowel.")
else:
    print("The letter you entered is not a vowel.")
