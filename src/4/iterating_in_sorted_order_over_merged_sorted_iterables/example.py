# Iterating over merged sorted iterables

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
'''Merge multiple sorted inputs into a single sorted output.'''
for c in heapq.merge(a, b):
    print(c)
