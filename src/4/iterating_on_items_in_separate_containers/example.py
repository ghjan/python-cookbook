# Example of iterating over two sequences as one

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)

# strength
# 1. save memery;
# 2. chain can work even if items in a and b are not same type;
