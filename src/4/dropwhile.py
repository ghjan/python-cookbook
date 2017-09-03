from itertools import dropwhile

with open('passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
print("\n-------")

from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
