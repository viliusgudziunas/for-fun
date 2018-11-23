# 52.
#
# Write a Python program to print to stderr.

from __future__ import print_function
import sys


def eprint52(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint52("abc", "efg", "xyz", sep="--")
