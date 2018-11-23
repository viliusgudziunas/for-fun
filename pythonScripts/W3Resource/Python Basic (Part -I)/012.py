# 12.
#
# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
y = int(input("Please enter a year: "))
m = int(input("Please enter a month: "))
print(calendar.month(y, m))