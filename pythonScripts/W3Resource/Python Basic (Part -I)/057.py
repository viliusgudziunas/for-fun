# 57.
#
# Write a program to get execution time for a Python method.

import timeit

print(timeit.timeit("sum(range(1,5))",number=1))
