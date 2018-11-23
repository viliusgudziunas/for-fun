# Exercise 16

# Write a password generator in Python.
# Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random
a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-_=+[{]};:',<.>/?`~"
passwordlenght = int(input("How many symbols would you like to be in the password? "))
p = "".join(random.sample(a,passwordlenght ))
print(p)