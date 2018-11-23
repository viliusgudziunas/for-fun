# 62.
#
# Write a Python program to convert all units of time into seconds.

days = int(input("Please enter a number of days: ")) * 3600 * 24
hours = int(input("Please enter a number of hours: ")) * 3600
minutes = int(input("Please enter a number of minutes: ")) * 60
seconds = int(input("Please enter a number of seconds: "))

all_seconds = days + hours + minutes + seconds
print("All of this amounts to "+str(all_seconds)+" seconds.")
