# 63.
#
# Write a Python program to get an absolute file path.

import os


def absolute_file_path(path_fname):
    return os.path.abspath(path_fname)


print("Absolute file path: ", absolute_file_path("test.txt"))
