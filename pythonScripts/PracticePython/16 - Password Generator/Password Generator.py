# Exercise 16

# Write a password generator in Python.
# Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import random
a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()-_=+[{]};:',<.>/?`~"
passwordlenght = 8
p = "".join(random.sample(a,passwordlenght ))
print(p)