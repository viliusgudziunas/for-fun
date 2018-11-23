# 65.
#
# Write a Python program to convert seconds to day, hour, minutes and seconds.

seconds = int(input("Please enter a number of seconds: "))

day = int(seconds / 86400)
rem1 = seconds % 86400

hour = int(rem1 / 3600)
rem2 = rem1 % 3600

minute = int(rem2 / 60)
second = rem2 % 60

print("The amount of seconds equals to: ")
print(str(day)+" days")
print(str(hour)+" hours")
print(str(minute)+" minutes")
print(str(second)+" seconds")
