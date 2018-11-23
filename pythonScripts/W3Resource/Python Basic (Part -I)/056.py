# 56.
#
# Write a Python program to get height and width of the console window.

import shutil

wh = shutil.get_terminal_size()
print("Terminal size is %d x %d" % wh)
