# Exercise 6

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = str(input("Please enter a word "))
reverse = word[::-1]
if word == reverse:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")