# 7.
#
# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

file = input("Please enter a name of a file: ")
ext = file.split(".")[1]
print("Extension: " + ext)