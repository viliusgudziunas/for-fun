# Exercise 22

# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# and print out the results to the screen. I have a .txt file for you, if you want to use it!

with open("nameslist.txt", "r") as open_file:
    all_text = open_file.read()
    print(all_text)