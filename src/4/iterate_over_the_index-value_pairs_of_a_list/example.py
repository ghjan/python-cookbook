# Example of iterating over lines of a file with an extra lineno attribute
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))


parse_data('sample.dat')

from collections import defaultdict

word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(n, x, y)
